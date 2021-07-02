# coding=utf-8
import logging

import flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from core.extensions.exception import NotFoundException, \
    UnauthorizedException, BadRequestException, ForbiddenException
from core.extensions.sentry import before_send

_logger = logging.getLogger(__name__)

SENTRY_DSN = 'SENTRY_DSN'


def create_app():
    import config
    import logging.config
    import os

    from . import api, models
    from core import helpers

    def load_app_config(app):
        """
        Load app's configurations
        :param flask.Flask app:
        :return:
        """
        app.config.from_object(config)
        app.config.from_pyfile('config.py', silent=True)

    app = flask.Flask(
        __name__,
        instance_relative_config=True,
        instance_path=os.path.join(config.ROOT_DIR, 'instance')
    )
    app.json_encoder = helpers.JSONEncoder
    load_app_config(app)

    # Register new flask project here and get new dsn: https://sentry.io
    dns = SENTRY_DSN if os.environ.get('SEND_REPORT') == 'true' else None

    app.config['SENTRY_CONFIG'] = {
        'ignore_exceptions': [NotFoundException, UnauthorizedException,
                              BadRequestException, ForbiddenException],
        'level': logging.ERROR,
    }

    app.config['ERROR_404_HELP'] = False

    sentry_sdk.init(
        dsn=dns,
        integrations=[FlaskIntegration()],
        environment=app.config['ENV_MODE'],
        in_app_exclude=['app.extensions.exceptions'],
        before_send=before_send
    )

    # setup logging
    logging.config.fileConfig(app.config['LOGGING_CONFIG_FILE'],
                              disable_existing_loggers=False)

    app.secret_key = config.FLASK_APP_SECRET_KEY
    models.init_app(app)
    api.init_app(app)
    return app


app = create_app()

# Config for mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'nowhere2405@gmail.com'
app.config['MAIL_PASSWORD'] = 'mayduataodayak?'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

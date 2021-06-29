# coding=utf-8
import logging

from flask import Blueprint
from flask_restplus import Api

from core.extensions.exception import global_error_handler
from .user import user_namespace
from .email_verification import email_verification_namespace

_logger = logging.getLogger(__name__)

api_bp = Blueprint("api", __name__)

api = Api(
    app=api_bp,
    version='1.0',
    title='Login App API',
    validate=False,
    # doc='' # disable Swagger UI
)


def init_app(app, **kwargs):
    """
    :param flask.Flask app: the app
    :param kwargs:
    :return:
    """
    api.add_namespace(user_namespace)
    api.add_namespace(email_verification_namespace)
    app.register_blueprint(api_bp)
    api.error_handlers[Exception] = global_error_handler

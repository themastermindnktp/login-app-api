# coding=utf-8
import logging

import pytest

_logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def app(request):
    from core import app
    from core.models import db

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    # test db initializations go below here
    db.create_all()

    def teardown():
        db.session.remove()
        db.drop_all()
        ctx.pop()

    request.addfinalizer(teardown)
    return app

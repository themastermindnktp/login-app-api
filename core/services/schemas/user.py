import logging

from marshmallow import Schema, validates_schema

from core.validators.user import UserValidator

_logger = logging.getLogger(__name__)


class UserCreateSchema(Schema):
    @validates_schema
    def age(self, payload, **kwargs):
        UserValidator.check_is_mature(payload.get('age'))


class UserUpdateSchema(Schema):
    @validates_schema
    def age(self, payload, **kwargs):
        if payload.get('age'):
            UserValidator.check_is_mature(payload.get('age'))

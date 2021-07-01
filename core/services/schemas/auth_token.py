from marshmallow import Schema, validates_schema

from core.validators.auth_token import AuthTokenValidator


class AuthTokenCreateSchema(Schema):
    @validates_schema
    def not_existed(self, payload, **kwargs):
        AuthTokenValidator.check_not_existed(payload.get('token_id'))


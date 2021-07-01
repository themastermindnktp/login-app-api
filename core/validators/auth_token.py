from marshmallow import ValidationError

from core.repositories.auth_token import AuthTokenRepository
from core.validators.base import ValidationErrorCode


class AuthTokenValidator:
    @staticmethod
    def check_existed(token_id):
        user = AuthTokenRepository.get_by_id(token_id)
        if user is None:
            raise ValidationError(field_name='id', message=ValidationErrorCode.NOT_FOUND)

    @staticmethod
    def check_not_existed(token_id):
        user = AuthTokenRepository.get_by_id(token_id)
        if user is not None:
            raise ValidationError(field_name='id', message=ValidationErrorCode.DUPLICATED)


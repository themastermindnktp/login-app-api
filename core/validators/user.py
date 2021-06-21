import logging

from marshmallow import ValidationError

from core.repositories.user import UserRepository
from core.validators.base import ValidationErrorCode

_logger = logging.getLogger(__name__)


class UserValidator:
    @staticmethod
    def check_existed(id):
        user = UserRepository.get_by_id(id)
        if user is None:
            raise ValidationError(field_name='id', message=ValidationErrorCode.NOT_FOUND)

    @staticmethod
    def check_is_mature(age):
        if age < 18:
            raise ValidationError(field_name='age', message=ValidationErrorCode.MIN_VALUE)

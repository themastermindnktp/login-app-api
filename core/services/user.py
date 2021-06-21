import logging

from core import NotFoundException
from core.helpers.accepts_logic import accepts_logic
from core.repositories.user import UserRepository
from core.services.schemas.user import UserCreateSchema

_logger = logging.getLogger(__name__)


class UserService:
    @staticmethod
    def create(**kwargs):
        payload = accepts_logic(
            payload=kwargs,
            schema=UserCreateSchema
        )

        user = UserRepository.create(**payload)

        return user

    @staticmethod
    def get(id):
        user = UserRepository.get_by_id(id)

        if user is None:
            raise NotFoundException

        return user


class UsersService:
    @staticmethod
    def get_list():
        users = UserRepository.get_list()

        return users

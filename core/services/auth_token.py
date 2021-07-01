import logging

from core.helpers.accepts_logic import accepts_logic
from core.repositories.auth_token import AuthTokenRepository
from core.services.schemas.auth_token import AuthTokenCreateSchema

_logger = logging.getLogger(__name__)


class AuthTokenService:
    @staticmethod
    def create(**kwargs):
        payload = accepts_logic(payload=kwargs, schema=AuthTokenCreateSchema)
        auth_token = AuthTokenRepository.create(**payload)
        return auth_token

    @staticmethod
    def get_by_id(token_id):
        auth_token = AuthTokenRepository.get_by_id(token_id)
        if auth_token is None:
            # TODO: search about returning bad request ('token_id not found')
            return ""
        # TODO: add logic for validating expired auth_token
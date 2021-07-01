import logging

from core.models import AuthToken, db

logger = logging.getLogger(__name__)


class AuthTokenRepository:
    @staticmethod
    def create(**kwargs):
        token = AuthToken(**kwargs)
        db.session.add(token)
        db.session.commit()
        return token

    @staticmethod
    def get_by_id(id):
        token = AuthToken.query.filter(AuthToken.id == id).first()
        return token

    @staticmethod
    def update(id, **kwargs):
        user = AuthToken.query.filter(AuthToken.id == id).first()
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()

import logging

from core.models import User, db

logger = logging.getLogger(__name__)


class UserRepository:
    @staticmethod
    def create(**kwargs):
        user = User(**kwargs)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_by_id(id):
        user = User.query.filter(User.id == id).first()
        return user

    @staticmethod
    def get_by_email(email):
        user = User.query.filter(User.email == email).first()
        return user

    @staticmethod
    def get_list():
        users = User.query.all()
        return users

    @staticmethod
    def update(id, **kwargs):
        user = User.query.filter(User.id == id).first()
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()

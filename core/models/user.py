import logging

from flask_restplus import fields

from core.helpers.common import refine_dict
from core.models import db, TimestampMixin

logger = logging.getLogger(__name__)


class User(db.Model, TimestampMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.VARCHAR(128), nullable=False, unique=True)
    password = db.Column(db.VARCHAR(128), nullable=False)
    first_name = db.Column(db.VARCHAR(128))
    last_name = db.Column(db.VARCHAR(128))
    last_login = db.Column(db.TIMESTAMP)
    date_joined = db.Column(db.TIMESTAMP)
    is_active = db.Column(db.Boolean, default=False)
    is_superuser = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    avatar = db.Column(db.VARCHAR(100))

    def to_dict(self):
        return refine_dict(
            {
                'id': self.id,
                'name': self.name,
                'age': self.age,
                'information': self.information,
            }
        )


class UserSchema:
    user = {
        'id': fields.Integer(required=True, description='id'),
        'name': fields.String(required=True, description='name'),
        'age': fields.Integer(requried=True, description='age'),
        'information': fields.String(required=False, description='information'),
    }

    user_edit_req = {
        'name': fields.String(required=True, description='name'),
        'age': fields.Integer(requried=True, description='age'),
        'information': fields.String(required=False, description='information')
    }

import enum
import logging

from flask_restplus import fields

from core.helpers.common import refine_dict
from core.models import db, TimestampMixin

logger = logging.getLogger(__name__)


class User(db.Model, TimestampMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(512), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    information = db.Column(db.Text)

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

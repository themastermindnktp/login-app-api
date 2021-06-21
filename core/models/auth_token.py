import logging

from core.models import db, TimestampMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

logger = logging.getLogger(__name__)

class AuthToken(db.Model, TimestampMixin):
    __tablename__ = 'auth_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    access_token = db.Column(db.VARCHAR(128), nullable=False, unique=True)
    refresh_token = db.Column(db.VARCHAR(128), nullable=False, unique=True)
    expired_in = db.Column(db.Integer, nullable=False)
    token_type = db.Column(db.VARCHAR(128), nullable=False)

    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User')

import logging

from core.models import db, TimestampMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

logger = logging.getLogger(__name__)


class EmailVerification(db.Model, TimestampMixin):
    __tablename__ = 'email_verifications'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.VARCHAR(128), nullable=False, unique=True)
    is_verified = db.Column(db.Boolean, nullable=False, default=False)
    expired_in = db.Column(db.TIMESTAMP, nullable=False)
    token_type = db.Column(db.VARCHAR(128), nullable=False)
    token = db.Column(db.VARCHAR(128), nullable=False, unique=True)

    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User')

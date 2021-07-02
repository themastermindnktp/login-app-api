import logging

from core.models import EmailVerification, db

logger = logging.getLogger(__name__)


class EmailVerificationRepository:
    @staticmethod
    def create(**kwargs):
        email = EmailVerification(**kwargs)
        db.session.add(email)
        db.session.commit()
        return email

    @staticmethod
    def get_by_token(token):
        email = EmailVerification.query.filter(EmailVerification.token == token).first()
        return email

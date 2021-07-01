import logging

from itsdangerous import URLSafeTimedSerializer

from core import NotFoundException
from core.repositories.user import UserRepository

_logger = logging.getLogger(__name__)
s = URLSafeTimedSerializer('my_scr3t_k3y')


class EmailVerificationService:
    @staticmethod
    def forgot_password(email):
        tokenValue = s.dumps(email, salt='email-forgot-password')
        _logger.warning("my token: " + tokenValue)
        user = UserRepository.get_by_email(email)
        if user is None:
            raise NotFoundException
        _logger.warning(user)
        # TODO: finish all logics
        # create instance, add to db email_verifications
        # - is-verified: 0
        # - email: email
        # - expired-in: get current timestamp
        # - token: tokenValue
        # - token-type: FORGOT-PASSWORD
        # - user-id: get by querying user from email
        # send link to email using flask-mail?
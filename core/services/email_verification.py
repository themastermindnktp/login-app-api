import logging

# import flask_mail
from itsdangerous import URLSafeTimedSerializer

from core import NotFoundException, app, BadRequestException
from core.helpers import get_current_timestamp
from core.helpers.time_utils import add_hours_to_time
from core.repositories.email_verification import EmailVerificationRepository
from core.repositories.user import UserRepository

_logger = logging.getLogger(__name__)
s = URLSafeTimedSerializer('my_scr3t_k3y')
# mail = Mail(app)


class EmailVerificationService:
    @staticmethod
    def forgot_password(user_email):
        # get matched user
        user = UserRepository.get_by_email(user_email)
        if user is None:
            raise NotFoundException('No account matched your email.')

        # create email_verification instance, then store in DB
        token_value = s.dumps(user_email, salt='email-forgot-password')
        _logger.warning("my token: " + token_value)
        confirm_email = EmailVerificationRepository.create(
            email=user_email,
            is_verified=0,
            expired_in=add_hours_to_time(get_current_timestamp(), 1),
            token_type="RESET-PASSWORD",
            token=token_value,
            user_id=user.id
        )

        # TODO: finish all logics
        # send link to email using flask-mail? but I can't import it :)

    @staticmethod
    def reset_password(token):
        # get matched email_verification
        email_verification = EmailVerificationRepository.get_by_token(token)
        if email_verification is None:
            raise NotFoundException('Token is not existed.')
        # validate if expired
        if email_verification.expired_in < get_current_timestamp():
            raise BadRequestException('Token is expired.')
        # TODO: search for logic of validating. should we create confirmation link in frontend or backend ?
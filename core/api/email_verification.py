import logging

from flask import request
from flask_restplus import Resource

from core.extensions import Namespace
from core.models import EmailVerificationSchema
from core.services.email_verification import EmailVerificationService

_logger = logging.getLogger(__name__)

email_verification_namespace = Namespace('email_verifications')

# TODO: ...
_email_verify_forgot_password_req = email_verification_namespace.model(
    'email_verify_forgot_password_req', EmailVerificationSchema.email_verify_forgot_password_req)
_email_verify_forgot_password_resp = email_verification_namespace.model(
    'email_verify_forgot_password_resp', EmailVerificationSchema.email_verify_forgot_password_resp)


@email_verification_namespace.route('/forgot-password', methods=['POST'])
class ForgotPassword(Resource):
    @email_verification_namespace.expect(_email_verify_forgot_password_req, validate=True)
    @email_verification_namespace.marshal_with(_email_verify_forgot_password_resp)
    def post(self):
        payload = request.json
        email = payload.get('email')
        EmailVerificationService.forgot_password(email)


@email_verification_namespace.route('/reset-password/<string:token>', methods=['GET'])
class ResetPassword(Resource):
    def get(self, token):
        # TODO: call service here
        _logger.warning(token)

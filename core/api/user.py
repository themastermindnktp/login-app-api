import logging

from flask import request
from flask_restplus import Resource

from core.extensions import Namespace
from core.models import UserSchema
from core.services.user import UserService, UsersService

_logger = logging.getLogger(__name__)

user_namespace = Namespace('users')

_user_res = user_namespace.model('user_res', UserSchema.user)
_user_edit_req = user_namespace.model('user_create_req', UserSchema.user_edit_req)


@user_namespace.route('/', methods=['GET', 'POST'])
class Users(Resource):
    @user_namespace.marshal_with(_user_res, as_list=True)
    def get(self):
        users = UsersService.get_list()
        return users
    
    @user_namespace.expect(_user_edit_req, validate=True)
    @user_namespace.marshal_with(_user_res)
    def post(self):
        payload = request.json
        user = UserService.create(**payload)
        return user


@user_namespace.route('/<int:id>', methods=['GET'])
class User(Resource):
    @user_namespace.marshal_with(_user_res)
    def get(self, id):
        user = UserService.get(id)
        return user

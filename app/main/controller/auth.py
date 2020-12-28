from flask import request
from flask_restx import Resource

from app.main.service.auth_helper import Auth
from ..util.dto_auth import AuthDto

from ..util.decorator import token_required

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
    User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    def post(self):
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)

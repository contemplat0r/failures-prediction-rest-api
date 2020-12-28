from flask import request
from flask_restx import Resource

from ..util.dto_user import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user, turn_user_to_admin

from ..util.decorator import token_required, admin_token_required

api = UserDto.api
_user = UserDto.user
_user_extended = UserDto.user_extended

@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @token_required
    @api.marshal_list_with(_user_extended, envelope='data')
    def get(self, *args, **kwargs):
        """List all registered users"""
        return get_all_users(kwargs['user_info'])

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get_user_by_public_id', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @token_required
    @api.marshal_with(_user_extended)
    def get(self, public_id, *args, **kwargs):
        """get a user given its identifier"""
        user = get_a_user(kwargs['user_info'], public_id)
        if not user:
            api.abort(404)
        else:
            return user


@api.route('/<user_public_id>')
@api.param('public_id', 'The user public_id')
@api.response(404, 'User not found.')
class Admin(Resource):
    @api.doc('turn_user_to_admin_by_public_id', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @token_required
    @api.marshal_with(_user)
    def put(self, user_public_id, *args, **kwargs):
        """turn user to admin """
        return turn_user_to_admin(kwargs['user_info'], user_public_id)

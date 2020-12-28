import uuid
import datetime

from app.main import db
from app.main.model.failures import User

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401

def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users(user_info):
    if user_info['admin']:
        return User.query.all()
    else:
        return User.query.filter(User.public_id==user_info['public_id']).all()


def get_a_user(user_info, public_id):
    if user_info['admin']:
        return User.query.filter_by(public_id=public_id).first()
    else:
        return User.query.filter_by(public_id=user_info['public_id']).first()

def turn_user_to_admin(user_info, public_id):
    if user_info['public_id'] == public_id:
        user =  User.query.filter_by(public_id=public_id).first()
        user.admin = True
        save_changes(user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'public_id and your public_id don\'t mathc',
        }
        return response_object, 409

def save_changes(data):
    db.session.add(data)
    db.session.commit()

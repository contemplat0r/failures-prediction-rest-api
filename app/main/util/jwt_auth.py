import datetime
from functools import wraps

from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

import jwt

secrect_key = 'iabc--'

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            jwt_data = jwt.decode(token, secrect_key)
        except:
            return jsonify({'message': 'token is invalid'})

        return f(*args, **kwargs)
    return decorator

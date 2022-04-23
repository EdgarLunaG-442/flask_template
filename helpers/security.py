
import jwt
from flask import request, jsonify
from functools import wraps
from config import default

PREFIX = 'Bearer '


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({'message': 'A valid token is missing'})

        if not token.startswith(PREFIX):
            raise ValueError('The token format is invalid.')

        token = token[len(PREFIX):]

        try:
            data = jwt.decode(token, default.SECRET_KEY, algorithms="HS256")
            if data["app_uuid"] != default.API_UUID:
                raise ValueError('app_uuid is not authorized')
        except Exception as e:
            return jsonify({'message': 'token is invalid', 'error': str(e)})

        return f(*args, **kwargs)

    return decorator

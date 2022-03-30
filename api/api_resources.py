from flask import Blueprint
from flask_restful import Api
from api.resources import SignInResource, LogInResource


api_bp = Blueprint('api_bp', __name__)

api = Api(api_bp)

api.add_resource(SignInResource, '/api/auth/signup')
api.add_resource(LogInResource, '/api/auth/login')
from flask import Blueprint
from flask_restful import Api
from api.resources import BlackListAdd, BlackListVerify

api_bp = Blueprint('api_bp', __name__)

api = Api(api_bp)
api.add_resource(BlackListAdd, '/blacklist')
api.add_resource(BlackListVerify, "/blacklist/<string:email>")

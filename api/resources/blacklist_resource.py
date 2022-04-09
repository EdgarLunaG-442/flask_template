from flask_restful import Resource
from flask import request
from models import BlackList
from schemas import BlacklistSchema
from marshmallow.exceptions import ValidationError
from common.error_handling import ModelConflict
from helpers import filter_object, token_required

blacklist_schema = BlacklistSchema()


class BlackListAdd(Resource):

    @token_required
    def post(self):
        blocked_email = BlackList.query.filter(BlackList.email == request.json["email"]).first()
        if blocked_email:
            raise ModelConflict("El email ya hace parte de la lista negra")
        payload = filter_object(request.json, ["app_uuid"])
        payload["ip"] = request.remote_addr
        new_blocked_email = BlackList(**payload)
        new_blocked_email.add()
        return {"msg": f"El correo {new_blocked_email.email} fue añadido a la lista negra exitosamente"}, 200


class BlackListVerify(Resource):

    @token_required
    def get(self, email):
        try:
            blocked_email = BlackList.query.filter(BlackList.email == email).first()
            if not blocked_email:
                return {"msg": "El correo NO hace parte de la lista negra", "in_list": False}, 404
            else:
                return {"msg": "El correo SI hace parte de la lista negra",
                        "in_list": True, **filter_object(blacklist_schema.dump(blocked_email), ["ip", "id"])}
        except ValidationError as e:
            return {"msg": e.messages[0]}, 401


class HealthCheck(Resource):
    def get(self):
        return "Im alive!!", 200

import os
from flask import request
from common.error_handling import NotAllowed

API_UUID = os.getenv("API_UUID", "")
def validar_uuid():
    app_uuid = request.json.get("app_uuid", "")
    if app_uuid:
        if app_uuid != API_UUID:
            raise NotAllowed("No puede realizar esta operacion sin un token valido")
    else:
        raise NotAllowed("Debe ingresar el token de acceso")

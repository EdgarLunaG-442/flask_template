from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError
from common.error_handling import ObjectNotFound, AppErrorBaseClass, NotAllowed, NotReady, ModelConflict
from db import db
from api.api_resources import api_bp
from ext import marshmallow, migrate


def create_app(settings_module, test_mode: bool = False):
    application = Flask(__name__)
    application.config.from_object(settings_module)
    application.app_context().push()

    # Init extensions
    db.init_app(application)
    db.create_all()
    CORS(application)
    marshmallow.init_app(application)
    migrate.init_app(application, db)

    # Catch all errors 404
    Api(application, catch_all_404s=True)

    # Disable strict URL finishing mode with /
    application.url_map.strict_slashes = False

    # Register the blueprints
    application.register_blueprint(api_bp)

    # Register custom error handlers
    register_error_handlers(application)
    if test_mode:
        application = application.test_client()
    else:
        print("-------------Application runs ok------------------")
    return application


def register_error_handlers(application):
    @application.errorhandler(Exception)
    def handle_exception_error(e):
        db.session.rollback()
        return jsonify({'msg': 'No disponible', 'error': str(e)}), 400

    @application.errorhandler(IntegrityError)
    def handle_integrity_error(e):
        db.session.rollback()
        return jsonify({'msg': 'El usuario ya existe', 'error': str(e)}), 400

    @application.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': 'Method not allowed'}), 405

    @application.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg': 'Forbidden error'}), 403

    @application.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'msg': 'Not Found error'}), 404

    @application.errorhandler(AppErrorBaseClass)
    def handle_application_base_error(e):
        return jsonify({'msg': str(e)}), 400

    @application.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'msg': str(e)}), 404

    @application.errorhandler(NotAllowed)
    def handle_not_allowed(e):
        return jsonify({'msg': str(e)}), 401

    @application.errorhandler(NotReady)
    def handle_not_ready(e):
        return jsonify({'msg': str(e)}), 400

    @application.errorhandler(ModelConflict)
    def handle_conflict(e):
        return jsonify({'msg': str(e)}), 409

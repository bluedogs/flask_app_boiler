from flask import Blueprint
import logging
import traceback
from flask_restx import Api
from app.api.test import api as test_api
from sqlalchemy.orm.exc import NoResultFound

log = logging.getLogger(__name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp, version='1.0', title='Windwave API', description='Useful collections of APIs')

api.add_namespace(test_api)


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404

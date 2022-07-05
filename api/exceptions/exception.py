"""Exceptions"""
from flask import Blueprint, jsonify
from core.logger_config import logger


bp_errors = Blueprint('errors', __name__)


class InvalidParamsUsage(Exception):
    status_code = 30001

    def __init__(self, msg='Invalid params', status_code=None, **payload):
        super().__init__()
        self.msg = msg
        if status_code is None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict()
        rv['msg'] = self.msg
        rv['required'] = list(self.payload.keys())
        return rv


@bp_errors.app_errorhandler(InvalidParamsUsage)
def invalid_user_param(e):
    logger.exception(f'{e}, code: {e.status_code}')
    return jsonify(e.to_dict()), e.status_code


@bp_errors.app_errorhandler(400)
def bad_request(e):
    logger.exception(f'msg: {e.args}, code: {400}')
    return jsonify({'errorCode': 400, 'errorType': 'Bad Request'})


@bp_errors.app_errorhandler(404)
def invalid_route(e):
    logger.exception(f'args: {e}, code: {404}')
    return jsonify({'errorCode': 404, 'errorType': 'Route not found'})


@bp_errors.app_errorhandler(Exception)
def handle_exception(e):
    try:
        message = e.errors()
        logger.error(f'message: {message}')
    except:
        message = "Something wrong."
        logger.error(f'except message: {message}')
    res = {'errorCode': 500,
           'errorType': 'Internal Server Error',
           'errorMessage': message}
    logger.exception(f'{res}, code:{500}')
    return jsonify(res), 500

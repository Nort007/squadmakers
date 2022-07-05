from flask import Blueprint, request
from api.mathematico.service import get_lcm, increment_value


bp_math = Blueprint('api_math', __name__, url_prefix='/api/math')


@bp_math.route('/lcm', methods=['GET'])
def route_lcm():
    """lowest common multiple"""
    return get_lcm(request.args.get('numbers'))


@bp_math.route('/increment-number', methods=['GET'])
def route_increment_number():
    """Increment number"""
    return increment_value(request.args.get('number'))

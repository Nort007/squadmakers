from flask import Blueprint, request, jsonify
from api.joke.service import get_random_joke
from api.joke.service import service_save_joke, service_update_joke, service_delete_joke

bp_joke = Blueprint('api', __name__, url_prefix='/api/joke')


@bp_joke.route('/get-joke', methods=['GET'])
def route_joke():
    _joke: dict = {}
    if request.method == 'GET':
        _joke = get_random_joke(request.args.get('jokeFrom'))
    return jsonify(_joke)


@bp_joke.route('/add-joke', methods=['POST'])
def route_add_joke():
    return service_save_joke(**request.json)


@bp_joke.route('/update-joke', methods=['PUT', 'UPDATE'])
def route_update_joke():
    return service_update_joke(**request.json)


@bp_joke.route('/delete-joke', methods=['DELETE'])
def route_delete_joke():
    return service_delete_joke(request.json['number'])


from flask import Flask, Response
from core import logger
from api.joke.views import bp_joke
from api.home import bp_home
from api.mathematico.views import bp_math
from api.exceptions import bp_errors
from api.extensions import engine

app = Flask(__name__)

if app.env == 'development':
    app.config['DEBUG'] = True

    def add_cors_headers(response):
        response.headers.set('Access-Control-Allow-Origin', '*')
        response.headers.set('Access-Control-Allow-Headers', '*')
        response.headers.set('Access-Control-Allow-Methods', '*')
        return response

    @app.after_request
    def after_request(response):
        add_cors_headers(response)
        return response

    def handle_exception(e):
        logger.exception('request_error')
        response = Response(str(e))
        add_cors_headers(response)
        return response, 500


    app.config['TRAP_HTTP_EXCEPTIONS'] = True
    app.register_error_handler(Exception, handle_exception)


def register_blueprints():
    app.register_blueprint(bp_errors)
    app.register_blueprint(bp_joke)
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_math)


engine.connect()
register_blueprints()


if __name__ == '__main__':
    app.run(host='0.0.0.0')


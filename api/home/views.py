from flask import Blueprint, redirect, url_for
bp_home = Blueprint('home', __name__)


@bp_home.route('/home', methods=['GET'])
def home():
    return '<div align="center"><h1>Squadmakers</h1></div>'


@bp_home.route('/', methods=['GET'])
def index():
    return redirect(url_for('home.home'))

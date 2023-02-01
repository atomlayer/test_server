from flask import Blueprint
from flask import jsonify

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET'])
def login():
    return jsonify(message='test')




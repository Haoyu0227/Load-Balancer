import json
from flask import request, jsonify
from bson.json_util import dumps
from . import api

seed = ['0']


@api.route('', methods=['GET'])
def get_seed():
    """
    Get the num
    :return: json response
    """
    try:
        return seed[0]
    except Exception as e:
        return str(e)



@api.route('', methods=['POST'])
def update_seed():
    """
    Update the seed
    :return: json response
    """
    try:
        body = json.loads(request.get_data(), encoding='utf-8')
        seed[0] = body['num']
        return jsonify(dict(code=200))
    except Exception as exception:
        return str(exception)

from flask import jsonify


def jsonResponse(data, code, msg):
    return jsonify({'code': code, 'msg': msg, 'data': data})

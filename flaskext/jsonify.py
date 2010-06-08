# -*- coding: utf-8 -*-
from functools import wraps
from flask import Response

from json import dumps

def jsonify(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return Response(dumps(f(*args, **kwargs)), mimetype='application/json')
    return decorated_function


# -*- coding: utf-8 -*-
try:
    from json import dumps
except ImportError:
    from simplejson import dumps

from flask import Response

def jsonify(f):
    def inner(*args, **kwargs):
        return Response(dumps(f(*args, **kwargs)), mimetype='application/json')
    return inner


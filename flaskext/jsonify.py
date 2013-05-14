# -*- coding: utf-8 -*-
try:
    from json import dumps
except ImportError:
    from simplejson import dumps

from flask import Response
from functools import wraps, partial

def jsonify(method=None, cls=None):

    if method is None:
        return partial(jsonify, cls=cls)

    @wraps(method)
    def inner(*args, **kwargs):
        retval = method(*args, **kwargs)
        if cls is not None:
            return Response(dumps(retval, cls=cls), mimetype='application/json')
        return Response(dumps(retval), mimetype='application/json')
    return inner

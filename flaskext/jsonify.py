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

        # if the user is trying to return an error, we want to preserve
        # the error code in the HTTP response, but still send the intended data
        response_obj = retval
        if isinstance(retval, JSONStatusResponse):
            response_obj = retval.body

        if cls is not None:
            response = Response(dumps(response_obj, cls=cls), mimetype='application/json')
        else:
            response = Response(dumps(response_obj), mimetype='application/json')

        # if the user is trying to return an error, we need to manually
        # set the error code
        if isinstance(retval, JSONStatusResponse):
            response.status_code = retval.status_code

        return response

    return inner


class JSONStatusResponse(object):

    def __init__(self, status_code=200, body={}):
        self.status_code = status_code
        self.body = body;
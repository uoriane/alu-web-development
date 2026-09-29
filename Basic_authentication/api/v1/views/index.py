#!/usr/bin/env python3
""" Index of views
"""
from api.v1.views import app_views
from flask import jsonify, abort


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ Status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats() -> str:
    """ Statistic of all objects
    """
    from models.user import User
    return jsonify({"users": User.count()})


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def get_unauthorized() -> str:
    """ Raises a 401 Unauthorized error
    """
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def get_forbidden() -> str:
    """ Raises a 403 Forbidden error
    """
    abort(403)



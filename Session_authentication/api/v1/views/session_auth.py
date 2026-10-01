#!/usr/bin/env python3
""" Module for Session Authentication views
"""
from os import getenv
from flask import jsonify, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - User object jsonified with cookie set
    """
    email = request.form.get('email')
    if email is None or len(email) == 0:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if password is None or len(password) == 0:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(user.id)
    cookie_name = getenv("SESSION_NAME")

    response = jsonify(user.to_json())
    response.set_cookie(cookie_name, session_id)

    return response

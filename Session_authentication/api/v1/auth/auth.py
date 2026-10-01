#!/usr/bin/env python3
"""
Auth module for the API
"""
from os import getenv
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if path requires authentication
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        for excluded in excluded_paths:
            if excluded.endswith('*'):
                if path.startswith(excluded[:-1]):
                    return False
            elif path == excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method to check authorization header
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to check current user
        """
        return None

    def session_cookie(self, request=None):
        """ Returns a cookie value from a request
        """
        if request is None:
            return None

        cookie_name = getenv("SESSION_NAME")
        return request.cookies.get(cookie_name)

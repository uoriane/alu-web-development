#!/usr/bin/env python3
""" Auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns True if path requires authentication, False otherwise
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # Ensure path ends with a slash for consistent comparison
        normalized_path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            # Handle wildcard matching (e.g., /api/v1/stats/*)
            if excluded_path.endswith('*'):
                base_path = excluded_path[:-1]
                if normalized_path.startswith(base_path):
                    return False
            
            # Normalize excluded path for exact matching
            normalized_excluded = excluded_path if excluded_path.endswith('/') else excluded_path + '/'
            if normalized_path == normalized_excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Returns the Authorization header from the request, or None
        """
        if request is None:
            return None
        
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None - request will be used later
        """
        return None

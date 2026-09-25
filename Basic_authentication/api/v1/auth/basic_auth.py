#!/usr/bin/env python3
""" BasicAuth module for the API
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Returns the Base64 part of the Authorization header for a Basic Authentication
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        
        parts = authorization_header.split()
        if len(parts) != 2 or parts[0] != 'Basic':
            return None
        
        return parts[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """ Returns the decoded value of a Base64 string base64_authorization_header
        """
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None
        
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None 
 
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """ Returns the user email and password from the decoded Base64 value
        """
        if decoded_base64_authorization_header is None or not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        
        parts = decoded_base64_authorization_header.split(':', 1)
        return (parts[0], parts[1])

    def user_object_from_credentials(self, user_email: str, user_password: str) -> TypeVar('User'):
        """ Returns the User instance based on his email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_password is None or not isinstance(user_password, str):
            return None
        
        try:
            users = User.search({'email': user_email})
            if not users:
                return None
            for user in users:
                if user.is_valid_password(user_password):
                    return user
        except Exception:
            return None
        
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Overloads Auth current_user and retrieves the User instance for a request
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        
        b64_header = self.extract_base64_authorization_header(auth_header)
        if b64_header is None:
            return None
        
        decoded_header = self.decode_base64_authorization_header(b64_header)
        if decoded_header is None:
            return None
        
        email, password = self.extract_user_credentials(decoded_header)
        if email is None or password is None:
            return None
        
        return self.user_object_from_credentials(email, password)

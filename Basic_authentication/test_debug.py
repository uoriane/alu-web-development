#!/usr/bin/env python3
from api.v1.auth.basic_auth import BasicAuth
from flask import Flask, request

app = Flask(__name__)
auth = BasicAuth()

with app.test_request_context('/api/v1/users', headers={'Authorization': 'Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh'}):
    h = auth.authorization_header(request)
    print("1. authorization_header:", h)
    
    b64 = auth.extract_base64_authorization_header(h)
    print("2. extract_base64_authorization_header:", b64)
    
    dec = auth.decode_base64_authorization_header(b64)
    print("3. decode_base64_authorization_header:", dec)
    
    email, pwd = auth.extract_user_credentials(dec)
    print(f"4. extract_user_credentials -> email: {email}, pwd: {pwd}")
    
    u = auth.user_object_from_credentials(email, pwd)
    print("5. user_object_from_credentials:", u)

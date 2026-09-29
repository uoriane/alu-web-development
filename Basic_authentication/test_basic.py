#!/usr/bin/env python3
from api.v1.auth.basic_auth import BasicAuth
from models.user import User
from flask import Flask, request

app = Flask(__name__)

# Create a test user in storage
user = User()
user.email = "bob@hbtn.io"
user.password = "H0lbertonSchool98!"
user.save()

auth = BasicAuth()

with app.test_request_context('/api/v1/users', headers={'Authorization': 'Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh'}):
    current = auth.current_user(request)
    print("Found user:", current.email if current else "None")

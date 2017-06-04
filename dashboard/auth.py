from functools import wraps
from flask import request, Response

def check_auth(username, password):
    # This function is called to check if a username / password combination is valid.
    return username == "admin" and password == "password"

def authenticate():
    # Sends a 401 response that enables basic auth
    return Response("You cannot access this page without proper authentication", 401, {
        "WWW-Authenticate": "Basic realm='Dashboard Login'"
    })

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

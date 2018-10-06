import requests, json
import os, time
from functools import wraps
from flask import Flask, request, abort, jsonify

# API_KEY = b'HahaTeehee'
#
# def require_apikey(api_function):
#     @wraps(api_function)
#     def decorated_function(*args, **kwargs):
#         if request.headers.get("X-API-KEY") == API_KEY:
#             return api_function(*args, **kwargs)
#         else:
#             abort(401)
#     return decorated_function


app = Flask(__name__)

@app.route("/submit", methods=["GET", "POST"])
def submit_form():
    if request.method == "GET":
        abort(405, "method not allowed")
    if request.method == "POST":
        response = {
            "status": "ok",
            "result": "wow you submitted a form congrats omg!"
        }
        return jsonify(response)

@app.errorhandler
def custom_error_handler():
    pass

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=False)

import requests, json
import os, time
from functools import wraps
from flask import Flask, request, abort, jsonify
import MySQLdb

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

def insert_into_db():
    pass

def update_to_db(conn, table_name, info_dict, condition):
    try:
        keys, values = zip(*[kv for kv in info_dict.items() if kv[1] not in (None, "", "null")])
        temp = []
        for v in values:
            try: formated = v.replace('\\', '\\\\').replace('"', '\\"').encode('utf-8')
            except Exception: formated = v
            temp.append('"{}"'.format(formated))
        pairs = zip(keys, temp)
        if pairs:
            update = " , ".join("{} = {}".format(kv[0], kv[1]) for kv in pairs)
            query = "update {} set {} where {}".format(table_name, update, condition)
            cur = conn.cursor()
            conn.set_character_set('utf8')
            cur.execute('SET NAMES utf8;')
            cur.execute('SET CHARACTER SET utf8;')
            cur.execute('SET character_set_connection=utf8;')
            cur.execute(query)
            conn.commit()
        return True
    except Exception as e:
        print "\033[91mException:", condition, e, '\033[0m'
        return False


@app.route("/submit", methods=["GET", "POST"])
def submit_form():
    if request.method == "GET":
        abort(405, "method not allowed")
    if request.method == "POST":

        # Gets the current user in session and value they gave
        form_data = request.form.get("data")
        user_id = request.form.get("user_id")

        # Establish connection to sql db
        conn = MySQLdb.connect('localhost', 'root', 'password', 'ser')
        cur = conn.cursor()
        conn.set_character_set('utf8')
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')

        # new user, create row in database
        try:
            if (user_id == "new_user"):
                pass
            else:
                update_to_db(conn, 'USERS', info_dict, 'user_id = "{}"'.format(user_id))
                response = {
                    "status": "ok",
                    "result": {
                        "user_id": user_id,
                        "message": "Successfully updated user info to database!"
                    }
                }
        except Exception as e:
            response = {
                "status": "error",
                "result": "Could not save user to database!"
            }
            abort(400, response)
        return jsonify(response)

@app.errorhandler
def custom_error_handler():
    pass

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=False)

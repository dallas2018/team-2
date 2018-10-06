import requests, json
import os, time
from functools import wraps
from flask import Flask, request, abort, jsonify
import MySQLdb
from flask_cors import CORS

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
CORS(app)

def insert_dict_toDB(connection, table_name, info_dict):
    features = []
    values = []
    for x in info_dict.items():
        field = x[0]
        value = x[1]
        features.append("{}".format(str(field)))
        values.append("'{}'".format(str(value)))

    f = ",".join(features)
    v = ",".join(values)
    #try:
    if values:
        #print "values:  ", values
        cur = connection.cursor()
        cur.execute("SELECT COUNT(*) FROM USER")
        res = cur.fetchone()

        query = "insert into {}({}) values({});".format(table_name, f, v)

        cur.execute(query)
        connection.commit()
        return (res[0] + 1)

def update_to_db(conn, table_name, info_dict, condition):
    try:
        keys, values = zip(*[kv for kv in info_dict.items() if kv[1] not in (None, "", "null")])
        temp = []
        for v in values:
            temp.append('"{}"'.format(v))
        pairs = zip(keys, temp)
        if pairs:
            update = " , ".join("{} = {}".format(kv[0], kv[1]) for kv in pairs)
            query = "update {} set {} where {}".format(table_name, update, condition)
            cur = conn.cursor()
            # conn.set_character_set('utf8')
            # cur.execute('SET NAMES utf8;')
            # cur.execute('SET CHARACTER SET utf8;')
            # cur.execute('SET character_set_connection=utf8;')
            cur.execute(query)
            conn.commit()
        return True
    except Exception as e:
        print("\033[91mException:", condition, e, '\033[0m')
        return False



@app.route("/submit", methods=["GET", "POST"])
def submit_form():
    if request.method == "GET":
        abort(405, "method not allowed")
    if request.method == "POST":

        # Gets the current user in session and value they gave
        user_id = request.get_json().get("user_id")
        form_data = request.get_json().get("data")

        # Establish connection to sql db
        conn = MySQLdb.connect('localhost', 'root', '@JPMC_team2_2018', 'jpmc', port=3306)
        cur = conn.cursor()
        conn.set_character_set('utf8')

        # new user, create row in database
        try:
            if (str(user_id) == "new_user"):
                user_id = insert_dict_toDB(conn, "USER", form_data)
                response = {
                    "status": "ok",
                    "result": {
                        "user_id": str(user_id),
                        "message": "Successfully inserted user info to database!"
                    }
                }
            else:
                # info_dict = json.loads(form_data)
                update_to_db(conn, 'USER', form_data, 'user_id = "{}"'.format(user_id))
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
                "error": e
            }
            abort(400, response)
        return jsonify(response)

@app.errorhandler
def custom_error_handler():
    pass

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=False)

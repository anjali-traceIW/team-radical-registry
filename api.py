from flask import Flask, jsonify
from core.classes import Person
import pymysql
from param import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_all_people_info():
    query = "SELECT * FROM tb_People"
    connection = pymysql.connect(
        hostname,
        username,
        password,
        database_name,
        autocommit=True
    ) 
    try:
        with connection.cursor() as db:
        # Want another try?
            db.execute(query)
            results = db.fetchall()
            print(results)
    except Exception as e:
        print(e)
    finally:
        connection.close()
    

    return jsonify(results)

@app.route("/person/<person_id>", methods=["GET"])
def get_person_info(person_id):
    # Get person info from db
    return person

if __name__ == "__main__":
    app.run(host="localhost", port=8081, debug=True)
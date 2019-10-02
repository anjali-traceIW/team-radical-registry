from flask import Flask, jsonify
from core.classes import Person
import pymysql
# from param import *
from os import environ

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_all_people_info():
    query = "SELECT * FROM tb_People"
    connection = pymysql.connect(
        environ.get('DB_HOST'), #host
        environ.get('DB_USER'), #username
        environ.get('DB_PASSWORD'), #password
        "teams", #database
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
    query = f"SELECT * FROM tb_People WHERE P_Id={person_id}"
    connection = pymysql.connect(
        environ.get('DB_HOST'), #host
        environ.get('DB_USER'), #username
        environ.get('DB_PASSWORD'), #password
        "teams", #database
        autocommit=True
    ) 
    try:
        with connection.cursor() as db:
            db.execute(query)
            person = db.fetchone()
            print(person)
            return jsonify(person)
    except Exception as e:
        print(e)
    finally:
        connection.close()

if __name__ == "__main__":
    app.run(host="localhost", port=8081, debug=True)
from flask import Flask, jsonify
from json import JSONEncoder
from core.classes import Person
import pymysql
from param import *
from datetime import datetime



class MyJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Person):
            return {
                "id": o.id,
                "name": o.name,
                "team": o.team,
                "fave_drink": o.fave_drink,
                "personality_trait": o.trait,
                "height": o.height,
                "date_of_birth": o.dob.strftime("%Y-%m-%d %H:%M:%S.%f"),
                "most_likely_to": o.most_likely_to,
                "fav": o.fave.__dict__
            }

app = Flask(__name__)
app.json_encoder = MyJSONEncoder

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
    app.run(host="0.0.0.0", port=8081, debug=True)

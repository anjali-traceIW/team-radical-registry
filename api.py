from flask import Flask, jsonify
import Person

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_all_people_info():
    # Get all people from db
    return people

@app.route("/person", methods=["GET"])
def get_person_info(name):
    # Get person info from db
    return person

if __name__ == "__main__":
    app.run(host="localhost", port=8081, debug=True)
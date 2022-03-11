"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")
# add default members
jackson_family.add_member({ "name": "Jhon", "age": 33, "lucky_numbers": [ 7, 13, 22 ]})
jackson_family.add_member({ "name": "Jane", "age": 35, "lucky_numbers": [ 10, 14, 3 ]})
jackson_family.add_member({ "name": "Jimmy", "age": 5, "lucky_numbers": [ 1 ]})

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET', 'POST'])
def members():
    members = jackson_family.get_all_members()

    response_body = members

    return jsonify(response_body), 200

@app.route('/members/<int:id>', methods=['GET'])
def member(id):
    member = jackson_family.get_member(id)

    if member == None:
        return jsonify({ "message": "Member not found" }, 400)

    return jsonify({ "member": member }, 200)

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

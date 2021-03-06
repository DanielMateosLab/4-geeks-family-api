"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")
# add default members
jackson_family.add_member({ "id": 1, "name": "Jhon", "age": 33, "lucky_numbers": [ 7, 13, 22 ]})
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

@app.route('/members', methods=['GET'])
def get_members():
    members = jackson_family.get_all_members()

    response_body = members

    return jsonify(response_body), 200

@app.route('/member', methods=['POST'])
def add_member():    
    if request.method == "POST":
        member = request.json
        required_fields = ["first_name", "age", "lucky_numbers" ]
        
        for field in required_fields:
            if field not in member:
                return jsonify({ "message": f"All members must have {field!r}"}), 400 
        
        jackson_family.add_member(member)

        return jsonify({}), 200

@app.route('/member/<int:id>', methods=['GET', 'DELETE'])
def get_or_delete_member(id):
    member = jackson_family.get_member(id)

    if member == None:
        return jsonify({ "message": "Member not found" }, 400)

    if request.method == "GET":
        return jsonify(member), 200
    
    jackson_family.delete_member(id)
    
    return jsonify({ "done": True })


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

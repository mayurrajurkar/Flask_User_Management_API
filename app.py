from flask import Flask,redirect,url_for,render_template,request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify

from werkzeug.security import generate_password_hash,check_password_hash
app=Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/corider_pro"
mongo = PyMongo(app)

@app.route('/users',methods=["GET"])
def users():
    users = mongo.db.user.find( )
    resp = dumps(users)
    return resp


@app.route('/users/<id>',methods=["GET"])
def user(id):
    user = mongo.db.user.find_one({'_id':ObjectId(id)})
    resp = dumps(user)
    return resp




@app.route("/users", methods=["POST"])
def adduser():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password and request.method == 'POST':
        haspa = generate_password_hash(_password)

        id =mongo.db.user.insert_one({'name':_name ,'email': _email , 'password': haspa})
        resp = jsonify("user added successfully")
        resp.status_code = 200

        return resp
        
    else:
        return not_found()

@app.route('/users/<id>', methods=["DELETE"])
def deleteuser(id):
    mongo.db.user.delete_one({'_id':ObjectId(id)})
    resp = jsonify("user deleted sucessfully")
    resp.status_code = 200
    return resp

@app.route('/users/<id>', methods=["PUT"])
def updateuser(id):
    _id = id
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password and _id and request.method == 'PUT':
        haspa = generate_password_hash(_password)

        mongo.db.user.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},{'$set':{'name' : _name,'email' : _email,'password' : haspa}})

        resp = jsonify("user updated successfully")
        resp.status_code = 200

        return resp
    else:
        return not_found()
        
@app.errorhandler(404)
def not_found(error = None):
    mess = {
        'status':404,
        'message' :'Not Found   ' + request.url
    }

    resp = jsonify(mess)
    resp.status_code = 404

    return resp
    
@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(debug=True)
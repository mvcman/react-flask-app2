from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import psycopg2
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from models import app, db, Users

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

@app.route('/users/register', methods=['POST'])
def register():
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    created = datetime.utcnow()
    print(first_name, last_name, email, password)
    user = Users(first_name=first_name, last_name=last_name, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    result = {
      "first_name" : first_name,
      "last_name" : last_name,
      "email" : email,
      "password" : password,
      "created" : created
      }
    return jsonify({"result" : result})


@app.route('/users/login', methods=['POST'])
def login():
    email = request.get_json()['email']
    password = request.get_json()['password']
    result = ""

    user = Users.query.filter_by(email=email).first()
    if bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity = {'first_name' : user.first_name, 'last_name' : user.last_name, 'email': user.email })
        result = jsonify({"token": access_token})
    else:
        result = jsonify({"error": "Invalid username and password"})
    return result

if __name__ == "__main__":
    app.run(debug=True)

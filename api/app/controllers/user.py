from flask import jsonify, request, json
from app import app, db
from app.models.users import User


@app.route("/api/user/", methods=['POST'])
def create_user():
    name = request.json['name']
    phone = request.json['phone']
    user_name = request.json['user_name']
    password = request.json['password']
    user = User(name, phone, user_name, password)
    db.session.add(user)
    db.session.commit()
    return str(user), 200


@app.route("/api/user/<int:user_id>", methods=['GET', 'PUT'])
def find_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if request.method == 'GET':
        if user:
            return str(user), 200
        else:
            return jsonify({"error": "There is no user with this id"}), 404
    else:
        if request.json['name']:
            new_name = request.json['name']
            user.name = new_name
        if request.json['phone']:
            new_phone = request.json['phone']
            user.phone = new_phone
        db.session.add(user)
        db.session.commit()
        return str(user), 200


@app.route("/api/user/<login>", methods=['GET'])
def find_user_by_login(login):
    user = User.query.filter_by(user_name=login).first()
    if user:
        return str(user), 200
    else:
        return jsonify({"error": "There is no user with this User_Name"}), 404


@app.route("/api/users/", methods=['GET'])
def show_all_users():
    users = User.query.order_by(User.id).all()
    if len(users) > 0:
        return str(users), 200
    else:
        return "[]", 200

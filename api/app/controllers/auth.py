from flask import jsonify, request, json
from flask_jwt_extended import create_access_token
from app import app, bcrypt
from app.models.userSchema import User


@app.route('/api/auth/local', methods=['POST'])
def login_local():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    login = request.json.get('user_name', None)
    password = request.json.get('password', None)
    if not login:
        return jsonify({"error": "Missing username parameter"}), 400
    if not password:
        return jsonify({"error": "Missing password parameter"}), 400

    user = User.query.filter_by(user_name=login).first()
    if user:
        if bcrypt.check_password_hash(user.password, password.encode('utf-8')):
            access_token = create_access_token(identity=user.id)
            return jsonify(user=json.loads(str(user)), token=access_token), 200

    return jsonify({"error": "Bad username or password"}), 401

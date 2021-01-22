from flask import jsonify, request, json
from app import app, db
from app.models.userSchema import User
from app.models.saleSchema import Sale
from flask_jwt_extended import jwt_required
from sqlalchemy.sql import func


@app.route("/api/user", methods=['POST'])
# @jwt_required
def create_user():
    name = request.json['name']
    phone = request.json['phone']
    user_name = request.json['user_name']
    password = request.json['password']
    user = User(name, phone, user_name, password)
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as inst:
        print(inst.args)
        return jsonify({"error": "Cannot process the request because it is malformed or incorrect"}), 400
    return jsonify(user=json.loads(str(user))), 201


@app.route("/api/user/<int:user_id>", methods=['GET', 'PUT'])
@jwt_required
def find_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if request.method == 'GET':
        if user:
            return jsonify(user=json.loads(str(user))), 200
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
        return jsonify(user=json.loads(str(user))), 200


@app.route("/api/user/<int:id>/sales/", methods=['GET'])
@jwt_required
def find_sales_by_userId(id):
    sales = Sale.query.filter_by(user_id=id).all()
    if sales:
        return jsonify(sales=json.loads(str(sales))), 200
    else:
        return jsonify({"error": "There is no sales with this id"}), 404


@app.route("/api/topUsers/", methods=['GET'])
@jwt_required
def show_top_users():
    join = db.session.query(User, func.sum(Sale.total)).outerjoin(
        Sale, User.id == Sale.user_id).group_by(User).all()
    result = []
    for target_list in join:
        sale = 0.00
        if target_list[1]:
            sale = target_list[1]
            sale = round(sale, 2)
        new_result = {"user": json.loads(str(target_list[0])), "sale": sale}
        result.append(new_result)

    def funcSortSale(e):
        return e['sale']
    result.sort(reverse=True, key=funcSortSale)
    del result[5:]
    if len(result) > 0:
        return jsonify(users=result), 200
    else:
        return jsonify(users=[]), 200


@app.route("/api/users/", methods=['GET'])
@jwt_required
def show_all_users():
    join = db.session.query(User, func.sum(Sale.total)).outerjoin(
        Sale, User.id == Sale.user_id).group_by(User).order_by(User.id).all()
    result = []
    for target_list in join:
        sale = 0.00
        if target_list[1]:
            sale = target_list[1]
            sale = round(sale, 2)
        new_result = {"user": json.loads(str(target_list[0])), "sale": sale}
        result.append(new_result)
    if len(result) > 0:
        return jsonify(users=result), 200
    else:
        return jsonify(users=[]), 200

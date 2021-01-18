from flask import jsonify, request, json
from app import app, db
from app.models.saleSchema import Sale
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route("/api/sale", methods=['POST'])
@jwt_required
def create_sale():
    product_id = request.json['product_id']
    quantity = request.json['quantity']
    total = request.json['total']
    user_id = get_jwt_identity()
    sale = Sale(product_id, quantity, total, user_id)
    db.session.add(sale)
    db.session.commit()
    return jsonify(sale=json.loads(str(sale))), 201


@app.route("/api/product/<int:sale_id>", methods=['GET', 'PUT'])
@jwt_required
def find_sale_by_id(sale_id):
    sale = Sale.query.filter_by(id=sale_id).first()
    if request.method == 'GET':
        if sale:
            return jsonify(sale=json.loads(str(sale))), 200
        else:
            return jsonify({"error": "There is no sale with this id"}), 404
    else:
        if request.json['quantity']:
            new_quantity = request.json['quantity']
            sale.quantity = new_quantity
        if request.json['total']:
            new_total = request.json['total']
            sale.total = new_total
        if request.json['total']:
            new_total = request.json['total']
            sale.total = new_total
        db.session.add(sale)
        db.session.commit()
        return jsonify(sale=json.loads(str(sale))), 200


@app.route("/api/sales/", methods=['GET'])
@jwt_required
def show_all_sales():
    sales = Sale.query.order_by(Sale.id).all()
    if len(sales) > 0:
        return jsonify(sales=json.loads(str(sales))), 200
    else:
        return jsonify(sales=[]), 200

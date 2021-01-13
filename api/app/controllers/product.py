from flask import jsonify, request, json
from app import app, db
from app.models.productShema import Product
from flask_jwt_extended import jwt_required


@app.route("/api/product", methods=['POST'])
@jwt_required
def create_product():
    name = request.json['name']
    value = request.json['value']
    product = Product(name, value)
    db.session.add(product)
    db.session.commit()
    return str(product), 200


@app.route("/api/product/<int:product_id>", methods=['GET', 'PUT'])
###@jwt_required
def find_product_by_id(product_id):
    product = Product.query.filter_by(id=product_id).first()
    if request.method == 'GET':
        if product:
            return str(product), 200
        else:
            return jsonify({"error": "There is no product with this id"}), 404
    else:
        if request.json['name']:
            new_name = request.json['name']
            product.name = new_name
        if request.json['value']:
            new_value = request.json['value']
            product.value = new_value
        db.session.add(product)
        db.session.commit()
        return str(product), 200


@app.route("/api/products/", methods=['GET'])
###@jwt_required
def show_all_products():
    products = Product.query.order_by(Product.id).all()
    if len(products) > 0:
        return jsonify(products=json.loads(str(products))), 200
    else:
        return "[]", 200

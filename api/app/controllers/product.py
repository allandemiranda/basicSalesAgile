import jsonpickle
from flask.globals import request
from app import app, db
from app.models.products import Product


@app.route("/api/product/", methods=['POST'])
def create_product():
    name = request.json['name']
    value = request.json['value']
    product = Product(name, value)
    db.session.add(product)
    db.session.commit()
    new_product = Product.query.filter_by(id=product.id).first()
    frozen_product = jsonpickle.encode(new_product)
    return frozen_product, 200


@app.route("/api/product/<int:product_id>", methods=['GET', 'PUT'])
def find_product_by_id(product_id):
    product = Product.query.filter_by(id=product_id).first()
    if request.method == 'GET':
        if product:
            frozen_product = jsonpickle.encode(product)
            return frozen_product, 200
        else:
            return "", 404
    else:
        if request.json['name']:
            new_name = request.json['name']
            product.name = new_name
        if request.json['value']:
            new_value = request.json['value']
            product.value = new_value
        db.session.add(product)
        db.session.commit()
        frozen_product = jsonpickle.encode(product)
        return frozen_product, 200


@app.route("/api/products/", methods=['GET'])
def show_all_users():
    products = Product.query.order_by(Product.id).all()
    if len(products) > 0:
        frozen_product = jsonpickle.encode(products)
        return frozen_product, 200
    else:
        return "[]", 200

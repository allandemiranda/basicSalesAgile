from datetime import datetime
from flask import json
from app import db
from app.models.userSchema import User
from app.models.productShema import Product


class Sale(db.Model):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        "products.id"), nullable=False)
    product = db.relationship("Product", foreign_keys=product_id)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", foreign_keys=user_id)

    def __init__(self, product_id, quantity, total, user_id):
        self.product_id = product_id
        self.quantity = quantity
        self.total = total
        self.user_id = user_id

    def __repr__(self):
        if not self.user:
            user = User.query.filter_by(id=self.user_id).first()
            product = Product.query.filter_by(id=self.product_id).first()
            sale = json.dumps({"id": self.id,  "quantity": self.quantity, "total": self.total, "date": self.date,
                               "product": json.loads(str(product)), "user": json.loads(str(user))})
            return sale
        sale = json.dumps({"id": self.id,  "quantity": self.quantity, "total": self.total, "date": self.date,
                           "product": json.loads(str(self.product)), "user": json.loads(str(self.user))})
        return sale

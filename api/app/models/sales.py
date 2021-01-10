from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql import func
from app import db


class Sale(db.Model):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        "products.id"), nullable=False)
    product = db.relationship("Product", foreign_keys=product_id)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", foreign_keys=user_id)

    def __init__(self, product_id, quantity, total, user_id):
        self.product_id = product_id
        self.quantity = quantity
        self.total = total
        self.user_id = user_id

    def __repr__(self):
        return "<Sale %r>" % self.id

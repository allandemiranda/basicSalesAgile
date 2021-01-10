from flask import json
from app import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        product = json.dumps(
            {"id": self.id, "name": self.name, "value": self.value})
        return product

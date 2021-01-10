from flask import json
from app import db, bcrypt


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    user_name = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __init__(self, name, phone, user_name, password):
        self.name = name
        self.phone = phone
        self.user_name = user_name
        pw_hash = bcrypt.generate_password_hash(password)
        self.password = pw_hash

    def __repr__(self):
        user = json.dumps({"id": self.id, "name": self.name, "phone": self.phone,
                           "user_name": self.user_name})
        return user

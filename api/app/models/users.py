from app import db


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
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.user_name

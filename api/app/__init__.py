from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config')

jwt = JWTManager(app)

bcrypt = Bcrypt(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(ssl_crt="cert.pem", ssl_key="key.pem"))

from app.models import productShema, saleSchema, userSchema

from app.controllers import default, auth, user, product, sale

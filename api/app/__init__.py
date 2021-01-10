from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object('config')

bcrypt = Bcrypt(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server())

from app.models import products, sales, users

from app.controllers import default, user

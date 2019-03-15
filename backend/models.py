from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import psycopg2
from flask_migrate import Migrate, MigrateCommand
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://classname:password@localhost/practodatabase'
app.config['SECRET_KEY'] = 'mandarwaghe'

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=True, nullable=False)
    last_name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)


if __name__ == "__main__":
    manager.run()

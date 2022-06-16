import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from user import user


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.register_blueprint(user)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

if __name__ == '__main__':
    app.run(debug=True)
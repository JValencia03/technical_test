from flask import Flask
from routes.routes import techTest
from flask_sqlalchemy import SQLAlchemy
from config.configdb import db
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # Documentation key

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'mysql+mysqldb://root:1234@localhost:3306/technicalTest')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(techTest)

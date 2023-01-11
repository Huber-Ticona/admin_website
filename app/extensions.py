from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import current_app
import pymysql

def obtener_conexion():
    return pymysql.connect(
        host=current_app.config['HOST'],
        user=current_app.config['USER'],
        password=current_app.config['PASSWORD'], 
        db=current_app.config['DB'])

db = SQLAlchemy()

migrate = Migrate()
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import pymysql

def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='huber123',
                                db='madenco_web')
db = SQLAlchemy()

migrate = Migrate()
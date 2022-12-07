from flask import Flask
import os
from .routes import main
from .archivo import archivo_bp
from .extensions import db , migrate 

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:huber123@localhost/madenco_web'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'madenco_website_2022'

    UPLOAD_FOLDER = r'../test_migrate/app/Productos'

    print(UPLOAD_FOLDER)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Inicializamos las extensiones
    db.init_app(app)
    migrate.init_app(app, db )

    # Registramos los modelos de base de datos
    from .models.entities.models import Categoria, Producto

    # Registramos los blueprints
    app.register_blueprint(archivo_bp)
    app.register_blueprint(main)


    return app
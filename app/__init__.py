from flask import Flask
import os
from .routes import main
from .archivo import archivo_bp
from .extensions import db , migrate 
from .config import DevelopConfig,ProductionConfig

def create_app():
    app = Flask(__name__)


    # CARGA CONFIGURACION
    if app.config['ENV'] == 'development':
        app.config.from_object(DevelopConfig)
    else:
        app.config.from_object(ProductionConfig)

    UPLOAD_FOLDER = os.path.abspath('../Productos')
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

    # si no existe la db , la crea y crea las tablas. tambien hace que sea visible globalmente en la aplicacion
    

    return app
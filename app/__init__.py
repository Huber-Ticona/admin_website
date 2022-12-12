from flask import Flask
import os
from .routes import main
from .archivo import archivo_bp
from .extensions import db , migrate 

def create_app(test_config = None):
    app = Flask(__name__)
    
    # Se carga la configuracion
    app.config.from_object(test_config)
    
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
    

    return app
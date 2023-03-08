
class Config(object):
    TEMPLATE_AUTO_RELOAD = True
    SECRET_KEY = 'maderas_enco_2023'
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024 # 20 MB
    
class DevelopConfig(Config):
    # BASE DE DATOS
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = 'huber123'
    DB = 'madenco_web'
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:huber123@localhost/madenco_web'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG  = True

class ProductionConfig(Config):
    # BASE DE DATOS
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = 'Enco$0011'
    DB = 'madenco_web'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Enco$0011@localhost/madenco_web'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG  = False
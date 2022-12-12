
class Config(object):
    TEMPLATE_AUTO_RELOAD = True
    
class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:huber123@localhost/madenco_web'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG  = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Enco$0011@localhost/madenco_web'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG  = False
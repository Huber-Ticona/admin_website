from app import create_app
from app.config import DevelopConfig,ProductionConfig

app = create_app(DevelopConfig)

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5002 )
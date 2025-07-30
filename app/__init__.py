from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():
    # Carrega el .env segons l'entorn
    env = os.getenv("FLASK_ENV", "development")
    dotenv_path = f".env.{env}"
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    app = Flask(__name__)

    # Configuració segons entorn
    if env == "production":
        from config.production import get_production_config
        app.config.from_object(get_production_config())
    else:
        from config.development import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    # 👉 Afegim això per development
    if env == "development":
        with app.app_context():
            from .models import Item
            db.create_all()

    # Registra blueprints
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app


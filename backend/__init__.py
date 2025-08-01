from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():
    env = os.getenv("FLASK_ENV", "development")
    dotenv_path = f".env.{env}"
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    app = Flask(__name__)

    if env == "production":
        from config.production import get_production_config
        app.config.from_object(get_production_config())
    else:
        from config.development import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    if env == "development":
        print("⚙️ Entorn: development – creant base de dades...")
        with app.app_context():
            import backend.models
            db.create_all()

    return app

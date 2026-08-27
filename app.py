from flask import Flask
from config import Config
from models import db, init_default_jars
from routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()
        init_default_jars()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
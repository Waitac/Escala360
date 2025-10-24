import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import db
from routes.auth import auth_blueprint
from routes.escala import escala_blueprint
from routes.dashboard import dashboard_blueprint

def create_app():
    app = Flask(__name__)

    # Carregar variáveis de ambiente ou usar defaults
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL',
        'postgresql://escala360:escala360_pass@localhost:5433/escala360_db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Autenticação
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models.profissional import Profissional
    
    @login_manager.user_loader
    def load_user(user_id):
        return Profissional.query.get(int(user_id))

    # Registro dos blueprints (rotas)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(escala_blueprint)
    app.register_blueprint(dashboard_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0')

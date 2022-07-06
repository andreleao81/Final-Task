from flask import Flask
from .config import Config
from .extensions import db, migrate


from app.funcionario.model import funcionario_api
from app.entrada.model import entrada_api
from app.saida.model import saida_api


def create_app():
    app =  Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(funcionario_api)
    app.register_blueprint(entrada_api)
    app.register_blueprint(saida_api)

    return app


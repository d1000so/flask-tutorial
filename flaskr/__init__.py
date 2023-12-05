import os

from flask import Flask


def create_app(test_config=None):
    # criar e configurar o aplicativo
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        #Carregar a configuração da instância, se ela existir, quando não estiver em fase de teste
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carregar a configuração de teste se for passada
        app.config.from_mapping(test_config)

    # garantir que a pasta da instância exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # uma página simples que diz "olá"
    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    from . import db
    db.init_app(app)

    return app
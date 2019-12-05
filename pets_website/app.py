
from flask import Flask
from flask_bootstrap import Bootstrap
from pets_website import routes


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app


app = create_app()

app.register_blueprint(routes.main_routes)
from flask import Flask
from flask_bootstrap import Bootstrap

from .models import db
from .manage import dbcli, managecli
from .views import index, upload, delete, download


def create_app():
    app = Flask(__name__, template_folder='template')
    app.config.from_pyfile('config.py')
    db.init_app(app)
    app.register_blueprint(dbcli)
    app.register_blueprint(managecli)
    app.register_blueprint(index.bp)
    app.register_blueprint(upload.bp)
    app.register_blueprint(delete.bp)
    app.register_blueprint(download.bp)
    Bootstrap(app)

    return app

import os 
from flask import Blueprint, cli, current_app

from .models import db

managecli = Blueprint('manage', __name__)
dbcli = Blueprint('db', __name__)

@managecli.cli.command("init")
@cli.with_appcontext
def init():
    """Creates media/upload folder"""
    media_folder = current_app.config['UPLOAD_FOLDER']
    if not os.path.exists(media_folder):
        os.mkdir(media_folder)

@dbcli.cli.command("init")
@cli.with_appcontext
def init_db():
    """Initialise dB"""
    db_uri = current_app.config['SQLALCHEMY_DATABASE_URI']
    if db_uri.startswith('sqlite'):
        db_path = db_uri[len('sqlite:///'):]
    if not os.path.exists(db_path):
        os.mkdir('db')
        from pathlib import Path
        Path(f"{db_path}").touch()
        db.create_all()

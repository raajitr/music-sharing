import os 
from flask import Blueprint, cli, current_app

from .models import db

dbcli = Blueprint('db', __name__)

@dbcli.cli.command("init")
@cli.with_appcontext
def init_db():
    """Initialise dB"""
    db_uri = current_app.config['SQLALCHEMY_DATABASE_URI']
    if db_uri.startswith('sqlite'):
        db_path = db_uri[len('sqlite:///'):]
    if not os.path.exists(db_path):
        os.system(f'mkdir db && touch {db_path}')
    db.create_all()

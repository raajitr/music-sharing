"""
As HTML can't send DELETE method from form, using POST method to do the same operation.
endpoint: /delete/<slug-of-the-mp3-file>
"""
import os

from flask import Blueprint, redirect, url_for, current_app
from ..models import db, Songs

bp = Blueprint('delete', __name__, url_prefix='/delete')

@bp.route('/<slug>', methods=["POST"])
def delete_song(slug):
    match = Songs.query.filter(Songs.slug == slug).one()
    if match:
        db.session.delete(match)
        db.session.commit()

        os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], match.slug))
    return redirect(url_for('index.home'))

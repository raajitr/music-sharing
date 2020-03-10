import os 

from flask import Blueprint, current_app, send_file

from ..models import Songs

bp = Blueprint('download', __name__, url_prefix='/download')

@bp.route('/<slug>', methods=["GET"])
def download_file(slug):
    audio_file = os.path.join(current_app.config['UPLOAD_FOLDER'], slug)
    song = Songs.get_song_from_slug(slug)
    filename = f"{song.title.title()} - {song.album.title()}.mp3"
    return send_file(audio_file, as_attachment=True, attachment_filename=filename)

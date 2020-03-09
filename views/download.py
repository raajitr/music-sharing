import os 

from flask import Blueprint, current_app, send_file


bp = Blueprint('download', __name__, url_prefix='/download')

@bp.route('/<slug>', methods=["GET"])
def download_file(slug):
    audio_file = os.path.join(current_app.config['UPLOAD_FOLDER'], slug)
    return send_file(audio_file, as_attachment=True, attachment_filename=slug+".mp3")

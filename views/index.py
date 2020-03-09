from flask import Blueprint, render_template, send_from_directory, current_app, url_for, request, redirect
from ..models import Songs

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', defaults={'song': None}, methods=["GET"])
@bp.route('/stream/<song>', methods=["GET"])
def home(song):
    if request.args:
        q_filter = request.args.get('f') or None  # filter: title, artist, artist or any
        q_search = request.args.get('q') or None  # search query

        if q_filter and q_filter.lower() in ['all', 'title', 'artist', 'album']:
            songs = Songs.search_songs(q_filter=q_filter, q_search=q_search)
        else:
            return redirect(url_for('index.home'))
    else:
        songs = Songs.query.all()
    current_song = url_for('index.static_audio_file', song=song) if song else None
    
    return render_template('index.html', songs=songs, current_song=current_song)


@bp.route('/cdn/<song>', methods=["GET"])
def static_audio_file(song):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], song)

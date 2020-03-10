import os 

from flask import Blueprint, render_template, current_app, redirect, url_for

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired

from wtforms import StringField, FileField, SubmitField
from wtforms.validators import InputRequired

from ..models import Songs

bp = Blueprint('form', __name__, url_prefix='/upload')

class UploadForm(FlaskForm):
    media = FileField(validators=[FileAllowed(['mp3'], 'only MP3 allowed!'),
                                  FileRequired('File was empty!')])

    title = StringField('Title', validators=[InputRequired()])
    artist = StringField('Artist', validators=[InputRequired()])
    album = StringField('Album', validators=[InputRequired()])
    submit = SubmitField('Upload')


@bp.route('/', methods=["GET", "POST"])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.media.data
        song = Songs(title=form.title.data,
                     artist=form.artist.data,
                     album=form.album.data)
        f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], song.slug))
        song.add_song()
        return redirect(url_for('index.home'))

    return render_template('form.html', form=form)

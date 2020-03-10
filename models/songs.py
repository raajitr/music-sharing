from slugify import slugify
from sqlalchemy.exc import IntegrityError
from . import db


class Songs(db.Model):
    __tablename__ = 'Songs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256))
    album = db.Column(db.String(64))
    artist = db.Column(db.String(64))
    slug = db.Column(db.String(64), unique=True)

    def __init__(self, *args, **kwargs):
        if 'slug' not in kwargs:
            title = kwargs.get('title')
            if title is None:
                raise Exception("Title can't be empty")
            # using slugify to create a slug from title - slugify handles the length and unicode string
            kwargs['slug'] = self.__class__.create_slug(title)
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return "<Song %r %r %r>" % (self.title, self.artist, self.album)

    def add_song(self):
        db.session.add(self)
        db.session.commit()

    def remove_song(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def create_slug(cls, title):
        slug = slugify(title)
        if cls.query.filter(cls.slug == slug).first():
            last_row_id = cls.query.order_by(cls.id.desc()).first().id
            slug += str(last_row_id+1)
        print(f"Debug: {slug}")
        return slug

    @classmethod
    def get_song_from_slug(cls, slug):
        return cls.query.filter(cls.slug == slug).first()

    @classmethod
    def search_songs(cls, q_filter, q_search):
        q_songs = cls.query
        search = q_search.lower()
        songs = []
        if q_filter.lower() == 'title':
            songs = q_songs.filter(cls.title.ilike("%{}%".format(search)))
        elif q_filter.lower() == 'artist':
            songs = q_songs.filter(cls.artist.ilike(f"%{search}%"))
        elif q_filter.lower() == 'album':
            songs = q_songs.filter(cls.album.ilike(f"%{search}%"))
        else:
            songs = q_songs.filter(cls.album.ilike(f"%{search}%") |
                                   cls.artist.ilike(f"%{search}%") |
                                   cls.title.ilike(f"%{search}%"))

        return songs


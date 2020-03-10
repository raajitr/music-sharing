import os
# TODO: Change this to different environments
# Currently the config is setup for development environment
SQLALCHEMY_DATABASE_URI = 'sqlite:///db/songs.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
WTF_CSRF_ENABLED = True
SECRET_KEY = os.getenv('SECRET_KEY')
UPLOAD_FOLDER = './media'
SQLALCHEMY_ECHO = False

import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///tmp/site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

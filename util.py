# The db object instantiated from the class SQLAlchemy represents the database and
# provides access to all the functionality of Flask-SQLAlchemy.
from flask import session
from flask_sqlalchemy import SQLAlchemy

from main import db


class Band(db.Model):
    # __tablename__ class variable defines the name of the table in the database
    __tablename__ = 'band'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    genre = db.Column(db.String(64))

    # give them a readable string representation that can be used for debugging and testing purposes
    def __repr__(self):
        return 'Band: %s, %s' % (self.name, self.genre)


class Song(db.Model):
    __tablename__ = 'song'

    song_id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(64))
    song_length = db.Column(db.String(64))
    song_band = db.Column(db.String(64))

    def __repr__(self):
        return 'Song %s, %s, %s' % (self.song_name, self.song_length, self.song_band)


def addBand(name, genre):
    db.session.add(Band(name=name, genre=genre))
    db.session.commit()


def addSong(name, leng, band):
    db.session.add(Song(song_name=name, song_length=leng, song_band=band))
    db.session.commit()

def doIndex():
    # locates all the subclasses of db.Model and creates corresponding tables in the database for them
    # brute-force solution to avoid updating existing database tables to a different schema
    db.drop_all()
    db.create_all()
    db.session.commit()


def getDB():
    band = Band.query.all()
    song = Song.query.all()
    return band, song



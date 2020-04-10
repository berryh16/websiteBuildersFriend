import os
from flask import Flask, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

import util

# get current app directory
basedir = os.path.abspath(os.path.dirname(__file__))

# create a Flask instance
app = Flask(__name__)
# define SQLAlchemy URL, a configuration parameter
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/database')
def index():
    bands, songs = util.getDB()
    return render_template('index.html', bands=bands, songs=songs)


@app.route('/')
@app.route('/siteBuilderFriend')
def start():
    return render_template('siteBuilderFriend.html')


@app.route('/dbstart')
def dbStart():
    util.doIndex()
    return render_template('index.html')


@app.route('/html')
def html():
    return render_template('html.html')


@app.route('/addBand', methods=['GET', 'POST'])
def addBand():
    name = ""
    genre = ""
    if request.method == 'POST':
        name = request.form['bname']
        genre = request.form['genre']
        print(name)
        print(genre)
        util.addBand(name, genre)
        return redirect('database')
    return render_template('addBand.html')


@app.route('/addSong', methods=['GET', 'POST'])
def addSong():
    name = ""
    leng = ""
    band = ""
    if request.method == 'POST':
        name = request.form['sname']
        leng = request.form['slen']
        band = request.form['band']
        util.addSong(name, leng, band)
        return redirect('database')
    return render_template('addSong.html')


@app.route('/bootstrap')
def boot():
    return render_template('bootstrap.html')


@app.route('/jquery')
def jq():
    return render_template('jquery.html')


@app.route('/javascript')
def javascript():
    return render_template('javascript.html')


@app.route('/flask')
def flask():
    return render_template('flask.html')


# default page for 404 error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404_error.html'), 404


# default page for 500 error
@app.errorhandler(500)
def server_error(e):
    print(e)
    return render_template('500_error.html'), 500


if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)

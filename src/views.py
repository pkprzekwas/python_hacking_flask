from flask import render_template, redirect, url_for, flash

from src import app, db
from src.forms import BookmarkForm
from src.models import Bookmark


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=Bookmark.newest(5))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = Bookmark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        flash('Stored bookmark: {}'.format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(err):
    return render_template('500.html'), 500

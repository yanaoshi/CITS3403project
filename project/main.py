import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import Reqs, Comment
from .forms import CreateRequestForm, SortForm, SearchForm, CommentForm
from datetime import datetime
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile/')
@login_required
def profile():
    comment_form = CommentForm()
    return render_template('profile.html', reqs=Reqs.query.all(), name=current_user.name, comment_form=comment_form)

@main.route('/create-request/', methods=['GET', 'POST'])
@login_required
def createrequest():
    form = CreateRequestForm()
    if request.method == 'GET':
        return render_template('create.html', name=current_user.name, form=form)
    
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        name = current_user.name
        image = form.file.data
        time_created = datetime.now().replace(microsecond=0)

        if image and image.filename != "":
            filename = secure_filename(name + '-' + title + '-' + image.filename)
            image.save(os.path.join('project/static/uploads/', filename))
        else:
            filename = None

        new_req = Reqs(title=title, content=content, poster=name, image=filename, time_created=time_created)
        db.session.add(new_req)
        db.session.commit()
        return redirect(url_for('main.viewrequests'))
    return render_template('create.html', form=form)

@main.route('/<int:id>/edit/', methods=['GET', 'POST'])
@login_required
def editrequest(id):
    target = Reqs.query.filter_by(id=id).first()
    form = CreateRequestForm(obj=target)

    if request.method == 'GET':
        return render_template('edit.html', req=target, form=form)
    
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        name = current_user.name
        target.title = title
        target.content = content
        target.name = name

        image = form.file.data
        if image and image.filename != "":
            filename = secure_filename(name + '-' + title + '-' + image.filename)
            image.save(os.path.join('project/static/uploads/', filename))
            target.image = filename
        elif target.image is not None:
            target.image = target.image
        else:
            target.image = None

        db.session.commit()
        return redirect(url_for('main.viewrequests'))
    return render_template('edit.html', req=target, form=form)

@main.route('/<int:id>/delete', methods=['POST'])
@login_required
def deleterequest(id):
    target = Reqs.query.filter_by(id=id).first()
    if target.image is not None:
        os.remove(os.path.join('project/static/uploads/', target.image))
    db.session.delete(target)
    db.session.commit()
    return redirect(url_for('main.viewrequests'))

@main.route('/<int:id>/deleteimage/', methods=['POST'])
@login_required
def deleteimage(id):
    target = Reqs.query.filter_by(id=id).first()
    os.remove(os.path.join('project/static/uploads/', target.image))
    target.image = None
    db.session.commit()
    return redirect(url_for('main.editrequest', id=target.id))

@main.route('/view-requests/', methods=['GET', 'POST'])
@login_required
def viewrequests():
    sort_form = SortForm()
    search_form = SearchForm()
    comment_form = CommentForm()
    
    reqs = Reqs.query
    
    if search_form.validate_on_submit() and 'search' in request.form:
        keywords = search_form.search.data
        reqs = reqs.filter(Reqs.title.like('%' + keywords + '%'))
    if sort_form.validate_on_submit() and 'sorting_method' in request.form:
        sorting_method = sort_form.sorting_method.data
        if sorting_method == 'newest':
            reqs = reqs.order_by(Reqs.time_created.desc())
        elif sorting_method == 'oldest':
            reqs = reqs.order_by(Reqs.time_created.asc())
    
    reqs = reqs.all()
    
    return render_template('view.html', reqs=reqs, name=current_user.name, sort_form=sort_form, search_form=search_form, comment_form=comment_form)

@main.route('/<int:req_id>/add-comment', methods=['POST'])
@login_required
def add_comment(req_id):
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        content = comment_form.comment_content.data
        poster = current_user.name
        time_created = datetime.now().replace(microsecond=0)
        new_comment = Comment(content=content, req_id=req_id, poster=poster, time_created=time_created)
        db.session.add(new_comment)
        db.session.commit()
    return redirect(url_for('main.viewrequests'))

@main.route('/<int:id>/delete-comment', methods=['POST'])
@login_required
def delete_comment(id):
    target = Comment.query.filter_by(id=id).first()
    db.session.delete(target)
    db.session.commit()
    return redirect(url_for('main.viewrequests'))

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/faq')
def faq():
    return render_template('faq.html')

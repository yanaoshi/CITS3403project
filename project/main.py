import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import Reqs
from datetime import datetime
# from .models import Users for use in profile functions
# import reCaptcha
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile/')
@login_required
def profile():
    return render_template('profile.html', reqs=Reqs.query.all(), name=current_user.name)

@main.route('/create-request/', methods=['GET', 'POST'])
@login_required
def createrequest():
    # returns the create request page when clicked
    if request.method == 'GET':
        return render_template('create.html', name=current_user.name)
    
    # when the form is filled out, creates a new request under the current user and redirects to view page
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        name = current_user.name
        image = request.files['file']
        time_created = datetime.now().replace(microsecond=0)

        if image.filename != "":
          filename = secure_filename(name + '-' + title + '-' + image.filename)
          image.save(os.path.join('project/static/uploads/', filename))
        else:
           filename = None

        new_req = Reqs(title=title, content=content, poster=name, image=filename, time_created=time_created)
        db.session.add(new_req)
        db.session.commit()
        return redirect(url_for('main.viewrequests'))
    
@main.route('/<int:id>/edit/', methods=['GET', 'POST'])
@login_required
def editrequest(id):
    # search for the target request in the database
    target = Reqs.query.filter_by(id=id).first()

    # returns the edit request page when clicked
    if request.method == 'GET':
        return render_template('edit.html', req=target)
    
    # when the form is filled out, edit the existing request in the databse and redirect to view page
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        name = current_user.name
        target.title = title
        target.content = content
        target.name = name

        image = request.files['file']
        if image.filename != "":
            # There is a new image uploaded to replace the old one
            filename = secure_filename(name + '-' + title + '-' + image.filename)
            image.save(os.path.join('project/static/uploads/', filename))
            target.image = filename
        elif target.image != None:
            # There is no new image, so use the old one
            target.image = target.image
        else:
            # There is no new image or old image
            filename = None

        db.session.commit()
        return redirect(url_for('main.viewrequests'))
    
@main.route('/<int:id>/delete', methods=['POST'])
@login_required
def deleterequest(id):
    # locate and delete target request in the database, along with its image
    target = Reqs.query.filter_by(id=id).first()
    if target.image != None:
      os.remove(os.path.join('project/static/uploads/', target.image))
    db.session.delete(target)
    db.session.commit()
    return redirect(url_for('main.viewrequests'))

@main.route('/<int:id>/deleteimage/', methods=['POST'])
@login_required
def deleteimage(id):
    # locate and delete target image in the database and directory
    target = Reqs.query.filter_by(id=id).first()
    os.remove(os.path.join('project/static/uploads/', target.image))
    target.image = None
    db.session.commit()
    return redirect(url_for('main.editrequest', id=target.id))

@main.route('/view-requests/', methods=['GET', 'POST'])
@login_required
def viewrequests():
    if request.method == 'GET':
        return render_template('view.html', reqs=Reqs.query.all(), name=current_user.name)
    if request.method == 'POST':
        keywords = request.form.get('search')
        reqs = Reqs.query.filter(Reqs.title.like('%' + keywords + '%'))
        reqs = reqs.order_by(Reqs.title).all()
        return render_template('view.html', reqs=reqs, name=current_user.name)

@main.route('/<string:sorting_method>/sort', methods=['POST'])
@login_required
def sortrequests(sorting_method):
    if sorting_method == 'newest':
      return render_template('view.html', reqs=Reqs.query.order_by(Reqs.time_created.desc()), name=current_user.name)
    elif sorting_method == 'oldest':
      return render_template('view.html', reqs=Reqs.query.order_by(Reqs.time_created.asc()), name=current_user.name)

@main.route('/<int:req_id>/add-comment', methods=['POST'])
@login_required
def add_comment(req_id):
    if request.method == 'POST':
        req = Reqs.query.get_or_404(req_id)
        content = request.form['comment_content']
        commenter_id = current_user.id
        new_comment = Comment(content=content, req_id=req_id, commenter_id=commenter_id, time_created=datetime.now())
        db.session.add(new_comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
    return redirect(url_for('main.viewrequests'))

@main.route('/view-request/<int:req_id>/comments')
@login_required
def view_comments(req_id):
    req = Reqs.query.get_or_404(req_id)
    comments = req.comments  # Retrieve comments associated with the request
    print(comments)  # Print comments to the console for debugging
    return render_template('view.html', req=req, comments=comments)
  

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Reqs
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

        new_req = Reqs(title=title, content=content, poster=name)
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
        db.session.commit()
        return redirect(url_for('main.viewrequests'))
    
@main.route('/<int:id>/delete', methods=['POST'])
@login_required
def deleterequest(id):
    # locate and delete target request in the database
    target = Reqs.query.filter_by(id=id).first()
    db.session.delete(target)
    db.session.commit()
    return redirect(url_for('main.viewrequests'))

@main.route('/view-requests/')
@login_required
def viewrequests():
    return render_template('view.html', reqs=Reqs.query.all(), name=current_user.name)
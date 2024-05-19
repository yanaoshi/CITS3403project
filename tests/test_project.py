import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from flask import url_for
from project import create_app, db

@pytest.fixture
def app():
    app = create_app('config.TestingConfig')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth(client):
    return AuthActions(client)

class AuthActions:
    def __init__(self, client):
        self._client = client

    def login(self, email='test@example.com', password='Password1!'):
        return self._client.post(url_for('auth.login'), data={'email': email, 'password': password}, follow_redirects=True)

    def logout(self):
        return self._client.get(url_for('auth.logout'), follow_redirects=True)

def test_registration(client):
    response = client.post(url_for('auth.signup'), data={
        'email': 'test@example.com',
        'username': 'testuser',
        'password': 'Password1!',
        'confirm_password': 'Password1!'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Please check your login details and try again." not in response.data

def test_login(client, auth):
    auth.login()
    response = client.get(url_for('main.index'), follow_redirects=True)
    assert response.status_code == 200
    assert b"Welcome" in response.data
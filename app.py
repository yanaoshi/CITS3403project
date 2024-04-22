import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'i was hiding'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_request(request_id):
    conn = get_db_connection()
    request = conn.execute('SELECT * FROM requests WHERE id = ?', (request_id,)).fetchone()
    conn.close()
    if request is None:
        abort(404)
    return request

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/request-sitter/", methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO requests (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route("/view-requests/")
def index():
    conn = get_db_connection()
    requests = conn.execute('SELECT * FROM requests').fetchall()
    conn.close()
    return render_template('index.html', requests=requests)

@app.route("/contact-us")
def contactus():
  return render_template("contactus.html")

@app.route("/FAQ")
def faq():
  return render_template("faq.html")

@app.route("/login")
def login():
  return render_template("login.html")

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    req = get_request(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')

        elif not content:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE requests SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', req=req)

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    req = get_request(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM requests WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(req['title']))
    return redirect(url_for('index'))

if __name__ == "__main__":
  app.run(debug=True)
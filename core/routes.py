import os

from flask import render_template, redirect, url_for, request, jsonify
from werkzeug.utils import secure_filename

from core import app

ALLOWED_EXTENSIONS = app.config['ALLOWED_EXTENSIONS']

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    print(request.remote_addr)

    imgs = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', imgs=imgs)


@app.route('/about')
def about():
    return render_template('about.html', about_active="active")


@app.route('/contact')
def contact():
    return render_template('contact.html', cont_active="active")


@app.route('/home')
def home():
    return redirect(url_for('index'))


@app.route('/add_new_post', methods=["GET", "POST"])
def add_new_post():
    if request.method == "POST":
        admin_password = request.form.get('pswd')
        print(admin_password)
        if admin_password:
            if admin_password == app.config['ADMIN_PASSWORD']:
                return render_template('add_new_post.html')
            else:
                return redirect(url_for('index'))
        elif admin_password == '':
            return redirect(url_for('index'))
        else:
            title = request.form.get('title')
            img = request.files["file"]
            if img and allowed_file(img.filename):
                filename = secure_filename(img.filename)
                img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    print(request.remote_addr)
    return  None

from os.path import join, dirname, realpath

from flask import Flask

from environs import Env

env = Env()
env.read_env(".env")

SECRET_KEY = env.str("SECRET_KEY")
ADMIN_PASSWORD = env.str("ADMIN_PASSWORD")
ALLOWED_EXTENSIONS = env.str("ALLOWED_EXTENSIONS")
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static\\img')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config.update(
    UPLOAD_FOLDER=UPLOAD_FOLDER,
    ADMIN_PASSWORD=ADMIN_PASSWORD,
    ALLOWED_EXTENSIONS=ALLOWED_EXTENSIONS
)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['ADMIN_PASSWORD'] = ADMIN_PASSWORD

from core import routes
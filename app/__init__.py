from flask import Flask

from app.sample.constants import Constants
from app.sample.sample_api import sample_bp

app = Flask(__name__)


def initialize_app():
    app.register_blueprint(sample_bp)
    return app

import requests
from flask import Blueprint, make_response

from app.sample.constants import Constants
from app.sample.routes import Routes

sample_bp = Blueprint('sample_bp', __name__)


@sample_bp.route(Routes.GET_SAMPLE, methods=['GET'])
def get_sample(user):
    response = requests.get(Constants.GITHUB_BASE_URL + "/users/" + user + "/gists")
    return make_response(response.json(), response.status_code)


@sample_bp.route("/", methods=['GET'])
def index():
    return "Welcome to Sample API", 200

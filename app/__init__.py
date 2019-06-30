"""Main application initialisation."""

from flask import Flask
from flask_restful import Api

from app.api import PhoneNumbers


def create_app():
    app = Flask(__name__)

    # Add app URL Routes
    api = Api(app)
    API_URL = "/api/v1/"

    # Add API resources
    api.add_resource(PhoneNumbers, API_URL + "contacts")

    return app

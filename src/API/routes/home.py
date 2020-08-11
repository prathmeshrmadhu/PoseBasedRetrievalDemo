from http import HTTPStatus
from flask import Blueprint, jsonify
from flasgger import swag_from

from schemas.home import HomeSchema
from models.home import HomeModel
from lib.logger import print_

home_api = Blueprint('api', __name__)

@home_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Retrieval Demo API is running!',
            'schema': HomeSchema
        }
    }
})
def home():
    """
    Check if API is online
    Check if API is online
    ---
    """

    print_("Route '/api' was callied...")
    result = HomeModel()
    result = HomeSchema().dump(result)
    print_(result)
    response = jsonify(result)

    return response
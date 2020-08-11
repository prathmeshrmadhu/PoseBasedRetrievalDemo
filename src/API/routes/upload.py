"""
Receiving the data from the client side and processing the image

@author: Angel Villar-Corrales
"""

import os

from http import HTTPStatus
from flask import Blueprint, jsonify, request
from flasgger import swag_from

from schemas.upload import UploadSchema
# from models.upload import UploadModel
from lib.utils import timestamp
from lib.logger import print_

upload_api = Blueprint('api/upload', __name__)
@upload_api.route('/', methods=['POST'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Data processed successfully!',
            'schema': UploadSchema
        }
    }
})
def receive_data():
    """
    Receives the image and metadata from a JSON and processing it
    Receives the image and metadata from a JSON and processing it
    ---
    """

    print_("Route '/api/upload' was callied...")
    data = request.form
    files = request.files

    # saving data in directory, cause why not?
    storage_element = files["file"]
    file_path = os.path.join(os.getcwd(), "data", "imgs", storage_element.filename)
    storage_element.save(file_path)

    return response, 200


#
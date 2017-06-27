from satellite import app
from satellite.extensions.jsonp import jsonp
from flask_jwt import jwt_required, current_identity
import uuid


# --------------------------------------------------------------------------
# GET DOCUMENT
# --------------------------------------------------------------------------
# Gets the complete list of document available in the system
@app.route('/api/v1/document', methods=['GET'])
@jwt_required()
@jsonp
def get_document():
    pass


# --------------------------------------------------------------------------
# GET DOCUMENT/ID
# --------------------------------------------------------------------------
# If exists, returns a json representation of an specific instance of a
# document
@app.route('/api/v1/document/<doc_id>', methods=['GET'])
@jwt_required()
@jsonp
def get_document_by_id(doc_id):
    pass


# --------------------------------------------------------------------------
# POST /DOCUMENT
# --------------------------------------------------------------------------
# If exists, returns a json representation of an specific instance of a
# document
@app.route('/api/v1/document', methods=['POST'])
@jwt_required()
@jsonp
def post_document():
    pass


# --------------------------------------------------------------------------
# PUT /DOCUMENT/<doc_id>
# --------------------------------------------------------------------------
# If exists, returns a json representation of an specific instance of a
# document
@app.route('/api/v1/document/<doc_id>', methods=['PUT'])
@jwt_required()
@jsonp
def put_document(doc_id):
    pass


# --------------------------------------------------------------------------
#  DELETE /DOCUMENT/<doc_id>
# --------------------------------------------------------------------------
# Given an specific id, if the documents exists, it deletes the document'
# from the database
@app.route('/api/v1/document/<doc_id>', methods=['DELETE'])
@jwt_required()
@jsonp
def delete_document(doc_id):
    pass

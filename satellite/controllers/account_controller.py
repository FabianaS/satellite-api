from satellite import app
from flask import request, jsonify
from satellite.models.account import User
from flask_jwt import jwt_required, current_identity
import uuid


# --------------------------------------------------------------------------
# POST: /account
# --------------------------------------------------------------------------
# Registers a new user in the system using Satellite Identity Sub-System
@app.route('/api/v1/account', methods=['POST'])
def post_account():
    user_data = request.get_json()
    if user_data:
        print(user_data)
        user = User(
            user_id=str(uuid.uuid4()),
            name=user_data['name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            username=user_data['username'],
            password=None
            )
        user.update_password(user_data['password'])
        user.save(validate=True)
        app.logger.info('User %s was created', user.user_id)
    return jsonify({"user_id": user.user_id}), 200


# --------------------------------------------------------------------------
# GET ACCOUNT
# --------------------------------------------------------------------------
# Gets the account information associated with current session in the system
@app.route('/api/v1/account', methods=['GET'])
@jwt_required()
def get_account():
    return current_identity.as_json(), 200

from satellite import app
from flask import request
from satellite.models.identity import User
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
            password=user_data['password']
            )
        user.save(validate=True)
    return 200

''

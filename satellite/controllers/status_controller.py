from satellite import app
from satellite.models.insights import SysStats
from flask_jwt import jwt_required


@app.route('/api/v1/info', methods=['GET'])
@jwt_required()
def get_status():
    return SysStats().as_json()

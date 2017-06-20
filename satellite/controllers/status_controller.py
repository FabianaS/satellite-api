from satellite import app
from satellite.models.insights import SysStats
from satellite.extensions.decorators import enable_jsonp
from flask_jwt import jwt_required


# ------------------------------------------------------------------------------
# FUNCTION GET_STATUS
# ------------------------------------------------------------------------------
@app.route('/api/v1/status', methods=['GET'])
@jwt_required()
@enable_jsonp
def get_status():
    """
        Gets some hardware performance indicators of the system where the API is
        running. 
    """
    return SysStats().as_json()

from satellite.models.identity import User
from mongoengine import *

# ------------------------------------------------------------------------------
# IDENTITY AND ACCESS MANAGEMENT SCRIPTS                                        
# ------------------------------------------------------------------------------
# This section provides scripts needed by 


# ------------------------------------------------------------------------------
# FUNCTION AUTHENTICATE                                       
# ------------------------------------------------------------------------------
# Checks given credential in order to authenticate or deny authentication to the 
# API. 
def authenticate(username, password):
    user = None
    try:
        user = User.objects.get(username = username)
        if user and user.authenticate(username, password):
            return user
        else:
            return None
    except DoesNotExist:
        app.logger.warning('A logging attempt of non-existing user: %d occured.', username)
        return None
    except MultipleObjectsReturned:
        app.logger.error('The username: %d has more than 1 match in database. Urgent revision required. Integrity failed', username)
        return None

# ------------------------------------------------------------------------------
# FUNCTION IDENTITY                                      
# ------------------------------------------------------------------------------
# Gets the User associated with a given identity
def identity(payload):
    user_id = payload['identity']
    user = None
    try:
        user = User.objects.get(username = user_id)
        return user
    except DoesNotExist:
        app.logger.warning('A retrieval attempt of non-existing user: %d occured.', username)
        return None
    except MultipleObjectsReturned:
        app.logger.error('The username: %d has more than 1 match in database. Urgent revision required. Integrity failed', username)
        return None
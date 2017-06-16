from satellite.models.identity import User
from mongoengine import *

# ------------------------------------------------------------------------------
# IDENTITY AND ACCESS MANAGEMENT SCRIPTS                                        
# ------------------------------------------------------------------------------


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
        return None
    except MultipleObjectsReturned:
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
        return None
    except MultipleObjectsReturned:
        return None
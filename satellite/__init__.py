from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt import JWT
# ------------------------------------------------------------------------------
# SETUP JWT AUTHENTICATION
# ------------------------------------------------------------------------------

__version__ = '1.0'
app = Flask('satellite')
app.config.from_object('config')
app.debug = True

# ------------------------------------------------------------------------------
# SETUP MONGO DB 
# ------------------------------------------------------------------------------

db = MongoEngine(app)

# ------------------------------------------------------------------------------
# SETUP JWT AUTHENTICATION
# ------------------------------------------------------------------------------

# Import all satellite controller files
from satellite.controllers import *
from satellite.security.idam import *

jwt = JWT(app, authenticate, identity)
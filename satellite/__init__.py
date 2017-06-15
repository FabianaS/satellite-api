from flask import Flask
from flask_mongoengine import MongoEngine

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

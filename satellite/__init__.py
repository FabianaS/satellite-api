import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt import JWT

# ------------------------------------------------------------------------------
# SETUP GENERAL APPLICATION
# ------------------------------------------------------------------------------

__version__ = '1.0'
app = Flask('satellite')
app.config.from_object('config')
app.debug = True

# ------------------------------------------------------------------------------
# SETUP LOGGING
# ------------------------------------------------------------------------------

handler = RotatingFileHandler('satellite-api.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# ------------------------------------------------------------------------------
# SETUP MONGO DB 
# ------------------------------------------------------------------------------

db = MongoEngine(app)

# ------------------------------------------------------------------------------
# SETUP JWT AUTHENTICATION
# ------------------------------------------------------------------------------

# Import all satellite controller files
from satellite.controllers import *
from satellite.security import idam

jwt = JWT(app, idam.authenticate, idam.identity)
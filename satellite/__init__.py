from flask import Flask

__version__ = '1.0'

app = Flask('satellite')
app.config.from_object('config')
app.debug = True

# Import all satellite controller files
from satellite.controllers import *

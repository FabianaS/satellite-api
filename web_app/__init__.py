from flask import Flask

__version__ = '1.0'

app = Flask('web_app')
app.config.from_object('config')
app.debug = True

# Import all web_app controller files
from web_app.controllers import *

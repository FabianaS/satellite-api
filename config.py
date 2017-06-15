# Turns on debugging features in Flask
DEBUG = True
#
# For use in web_app emails
MAIL_FROM_EMAIL = "info@boilerplateapp.com"
#
# This is a secret key that is used by Flask to sign cookies.
# Its also used by extensions like Flask-Bcrypt. You should
# define this in your instance folder to keep it out of version
# control.
SECRET_KEY = '!(q5W&V9zQ?jF<'
#
# Configuration for the Flask-Bcrypt extension
BCRYPT_LEVEL = 12
#
# ----------------------------------------------------------------
# SERVER CONFIGURATION
# ----------------------------------------------------------------
PORT = 8087
#
# ----------------------------------------------------------------
# SATELLITE DATABASE CONFIGURATION
# ----------------------------------------------------------------
# See https://flask-pymongo.readthedocs.io/en/latest/ for more
# MongoDB configuration parameters
MONGO_DBNAME = 'satellite'

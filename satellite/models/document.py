from mongoengine import *
from flask import jsonify
import datetime


class SatelliteDocument(Document):

    doc_id = StringField(max_length=40, required=True)

#!/usr/bin/python
# -*- coding: utf-8 -*-
from mongoengine import *
from werkzeug.security import safe_str_cmp
from satellite.security.entropy import gen_salt, compute_hash
import datetime


# ------------------------------------------------------------------------------
# CLASS USER
# ------------------------------------------------------------------------------
# Represents a User within the Satellite Identity sub-system. 
class User(Document):
    
    # --------------------------------------------------------------------------
    # USER PROPERTIES
    # --------------------------------------------------------------------------

    user_id = StringField(max_length=40, required=True)

    name = StringField(max_length=120, required=True)
    
    last_name = StringField(max_length=120, required=True)
    
    email = StringField(max_length=120, required=True, unique=True)
    
    username = StringField(max_length=120, required=True, unique=True)
    
    password = StringField(max_length=256, required=True)
    
    salt = StringField(max_length=17, required=True, default=gen_salt(17))
    
    date_modified = DateTimeField(default=datetime.datetime.now)
    
    meta = {
        'indexes': [
            'user_id',
            'username',
            'email'
        ]
    }

    # --------------------------------------------------------------------------
    # METHOD STR
    # --------------------------------------------------------------------------
    # Creates a string representation of a user
    def __str__(self):
        return "User(username='%s')" % self.username
        
    # --------------------------------------------------------------------------
    # METHOD IS_AUTHORIZED_TO
    # --------------------------------------------------------------------------
    def is_authorized_to(self, action):
        return action in self.claims
        
    # --------------------------------------------------------------------------
    # METHOD ADD_CLAIM
    # --------------------------------------------------------------------------
    def add_claim(self, claim):
        if claim not in self.claims:
            self.claims.append(claim)
        return
    
    # --------------------------------------------------------------------------
    # METHOD UPDATE PASSWORD
    # --------------------------------------------------------------------------
    def update_password(self, password):
        self.password = compute_hash(password, self.salt)
        
    # --------------------------------------------------------------------------
    # METHOD AUTHENTICATE
    # --------------------------------------------------------------------------
    def authenticate(self, password):
        challenge = compute_hash(password, self.salt)
        return safe_str_cmp(self.password.encode('utf-8'), challenge.encode('utf-8'))

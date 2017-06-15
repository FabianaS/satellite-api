from mongoengine import *
import datetime
import hashlib


# ------------------------------------------------------------------------------
# CLASS USER
# ------------------------------------------------------------------------------
# Represents a User within the Satellite Identity sub-system. 
class User(Document):
    
    # --------------------------------------------------------------------------
    # USER PROPERTIES
    # --------------------------------------------------------------------------
    
    name = StringField(max_length = 120, required = True)
    
    lastname = StringField(max_length = 120, required = True)
    
    email = StringField(max_length = 120, required = True)
    
    username = StringField(max_length = 120, required = True)
    
    password = StringField(max_length = 256, required = True)
    
    date_modified = DateTimeField(default=datetime.datetime.now)
    
    claims = []
    
    # --------------------------------------------------------------------------
    # CLASS CONSTRUCTOR 
    # --------------------------------------------------------------------------
    # Creats instances of User. 
    def __init__(self, id, name, lastname, email, username, password):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = hashlib.sha256(password).hexdigest()

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
        if claim not in self.claims
            self.claims.append(claim)
        return
    
    # --------------------------------------------------------------------------
    # METHOD UPDATE PASSWORD
    # --------------------------------------------------------------------------
    def update_password(self, password):
        self.password = hashlib.sha256(password).hexdigest()
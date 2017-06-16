from mongoengine import *
from werkzeug.security import safe_str_cmp
from satellite.security import entropy
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
    
    email = StringField(max_length = 120, required = True, unique=True)
    
    username = StringField(max_length = 120, required = True, unique=True)
    
    password = StringField(max_length = 256, required = True)
    
    salt = StringField(max_length = 17, required = True)
    
    date_modified = DateTimeField(default=datetime.datetime.now)
    
    meta = {
        'indexes': [
            'username',
            'email'
        ]
    }
    
    claims = []
    
   
    # --------------------------------------------------------------------------
    # METHOD __SALT_PASSWORD
    # --------------------------------------------------------------------------  
    # Appends a randomly generated value at the end of the password to protect
    # against dictionary attacks
    def __salt_password(self, password):
        return ''.join([password, self.salt])
        
    # --------------------------------------------------------------------------
    # METHOD __COMPUTE_HASH
    # -------------------------------------------------------------------------- 
    # Computes the SHA256 hash of the given password and encodes the result into
    # a hexadecimal string.
    def __compute_hash(self, password):
        return hashlib.sha256(__salt_password(password)).hexdigest()
    
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
        self.salt = gen_salt(length = 17)
        self.password = __compute_hash(password)

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
        self.password = hashlib.sha256(password).hexdigest()
        
    # --------------------------------------------------------------------------
    # METHOD AUTHENTICATE
    # --------------------------------------------------------------------------
    def authenticate(self, password):
        challenge = __compute_hash(password)
        return safe_str_cmp(self.password.encode('utf-8'), challenge.encode('utf-8'))
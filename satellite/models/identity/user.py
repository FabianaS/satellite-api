
# ------------------------------------------------------------------------------
# CLASS USER
# ------------------------------------------------------------------------------
# Represents a user in Satellite System. 

class User(object):
    
    # --------------------------------------------------------------------------
    # CLASS CONSTRUCTOR 
    # --------------------------------------------------------------------------
    # Creats instances of User. 
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    # --------------------------------------------------------------------------
    # METHOD STR
    # --------------------------------------------------------------------------
    # Creates a string representation of a user
    def __str__(self):
        return "User(id='%s')" % self.id

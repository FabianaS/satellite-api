import random
import string

# ------------------------------------------------------------------------------
# FUNCTION GEN_SALT
# ------------------------------------------------------------------------------
# Generates a random
def gen_salt(length):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))

import base64
import hashlib
import urllib

__auther__ = "Ameen"


def generate_random_password(length=15):
    import random
    import string
    '''generate randome string of fix length'''
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def encrypt_password(plain_password, salt):
    first_stage = hashlib.md5(plain_password.encode('utf-8')).hexdigest() + salt
    h = hashlib.md5()
    h.update(first_stage.encode('utf-8'))
    res = h.hexdigest()
    return res


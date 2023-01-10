import random
import string

def gen_password(password_len: int = 10):
    value = string.ascii_letters + string.punctuation + string.digits
    password = ""
    for i in range(password_len):
        password = password + random.choice(value)
    return password
import string
import random

def pass_gen ():

    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    password = []

    password.append(random.choice(uppercase_letters))
    password.append(random.choice(digits))
    password.append(random.choice(special_characters))

    for i in range(7):
        password.append(random.choice(uppercase_letters + digits + special_characters + lowercase_letters))

    random.shuffle(password)

    return ''.join(password)        
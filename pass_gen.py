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

    

# import random
# import string

# def generate_password():
#     # define the character sets for the password
#     uppercase_letters = string.ascii_uppercase
#     lowercase_letters = string.ascii_lowercase
#     digits = string.digits
#     special_characters = string.punctuation
    
#     # create a list to hold the password characters
#     password = []
    
#     # add one uppercase letter to the password
#     password.append(random.choice(uppercase_letters))
    
#     # add one digit to the password
#     password.append(random.choice(digits))
    
#     # add one special character to the password
#     password.append(random.choice(special_characters))
    
#     # fill the rest of the password with random characters
#     for i in range(7):
#         password.append(random.choice(uppercase_letters + lowercase_letters + digits + special_characters))
    
#     # shuffle the password characters
#     random.shuffle(password)
    
#     # convert the password list to a string and return it
#     return ''.join(password)
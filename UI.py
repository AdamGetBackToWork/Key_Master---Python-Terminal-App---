#from hash_maker import password
import string
import random
#from database import store_passwords, find_users, find_password 


def menu():
    print('-'*48)
    print(('-'*19) + 'Key master'+ ('-' *19))
    print('-'*48)
#    print(('-'*10) + 'Account'+ ('-' *10))
    print('1. Create new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('4. Generate a new safe password')
    print('Q. Exit')
    print('-'*48)
    return input(': ').upper()

def new_pass():
    print('To create a new password do as follows: ')
    URl = input('Please provide the URL of the website/app: \n')
    e_mail = input('Please provide the email associated with the account: \n')
    username = input('Please provide the username for the account: \n')



def pass_gen():

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

def create():
   print('Please proivide the name of the site or app you want to generate a password for')
   app_name = input()
   print('Please provide a simple password for this site: ')
   plaintext = input()
   passw = password(plaintext, app_name, 12)
   subprocess.run('xclip', universal_newlines=True, input=passw)
   print('-'*30)
   print('')
   print('Your password has now been created and copied to your clipboard')
   print('')
   print('-' *30)
   user_email = input('Please provide a user email for this app or site')
   username = input('Please provide a username for this app or site (if applicable)')
   if username == None:
       username = ''
   url = input('Please paste the url to the site that you are creating the password for')
   store_passwords(passw, user_email, username, url, app_name)


# def find():
#    print('Please proivide the name of the site or app you want to find the password to')
#    app_name = input()
#    find_password(app_name)

# def find_accounts():
#    print('Please proivide the email that you want to find accounts for')
#    user_email = input() 
#    find_users(user_email)

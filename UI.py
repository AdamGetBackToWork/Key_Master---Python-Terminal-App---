#from hash_maker import password



def menu():
    print('-'*36)
    print(('-'*10) + 'Password Manager'+ ('-' *10))
#    print(('-'*10) + 'Account'+ ('-' *10))
    print('1. Create new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('Q. Exit')
    print('-'*36)
    return input(': ')

def new_pass():
    print('To create a new password do as follows: ')
    URl = input('Please provide the URL of the website/app: \n')
    e_mail = input('Please provide the email associated with the account: \n')
    username = input('Please provide the username for the account: \n')





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
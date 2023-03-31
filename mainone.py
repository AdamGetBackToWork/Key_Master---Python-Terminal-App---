from UI import menu, new_pass

account = input("Hi! You're accesing your Password Manager, to proceed choose your account: \n 1 \n 2 \n 3 \n Account: ")

if account == "1":
    pass1 = input('To enter to your account, provide your password: ' )
    if pass1 == 'Pass1':
       print('You\'re in!')
    else: 
        quit

elif account == "2":
    pass1 = input('To enter to your account, provide your password: ' )
    if pass1 == 'Pass1':
       print('You\'re in!')
    else: 
        quit

elif account == "3":
    pass1 = input('To access your account, provide your password: ' )
    if pass1 == 'Pass1':
       print('You\'re in!')
    else: 
        quit

else:
    quit



choice = menu()
while choice != 'Q':
    if choice == '1':
        new_pass()
    if choice == '2':
        find_accounts()
    if choice == '3':
        find()
    else:
        print('Invalid input')
        choice = menu()
exit()
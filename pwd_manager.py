from cryptography.fernet import Fernet
m_pwd = input("What is the master password? ")
 
def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, " Password: ", passw)

def add():
    name = input("Account name: ")
    a_pwd = input("Password: ")
    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + a_pwd + "\n")


while True:
    mode = input("Do you want to add a new password or access existing ones? You can also press q and to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue


if m_pwd != "12345678":
    print("Wrong password! ")
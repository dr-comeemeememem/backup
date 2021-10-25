# Date created: Thu Oct 21 15:34:26 2021
# Last date modified: Sat Jul 24 17:17:04 2021
names = []
passwords = []  
def create_Account():
    name = input("What username do you want to have? ")
    names.append(name)
    password = input(f"What password do you want to have for {name}? ")
    passwords.append(password)

def login_Account():
    name = input("What is your username? ")
    password = input(f"What is your password for {name}? ")
    try:
        if(name not in names[names.index(name)] or password not in passwords[passwords.index(password)]):
            return "The username or password is incorrect"
    except:
        return "The username or password is incorrect"
    
    if(name in names[names.index(name)] and password in passwords[passwords.index(password)]):
        return "You are now logged in!"
    
def display():
    while True:
        print("Choose an option: ")
        print("1. Create a new account")
        print("2. Log in")
        print("3. Quit")
        choice = int(input("Enter: "))

        if(choice == 1):
            create_Account()
            print(login_Account())
            continue
        elif(choice == 2):
            print(login_Account())
            continue
        else:
            return False
if __name__ == '__main__':  
    display()

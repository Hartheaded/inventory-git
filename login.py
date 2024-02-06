import bcrypt
import os

class Account():


    def __init__(self):
        self.username = ""
        self.password = ""
        self.path = "./accounts"
        self.dir = os.listdir(self.path)

    def __new__(cls):
        return self.username

    # Creates a new user in a folder called accounts
    def newUser(self):
        username = input("New Username:")

        while True:
            password1 = input("New Password: ")
            password2 = input("Please repeat password: ")
            if password1 == password2:
                save_path = "./accounts"
                compName = os.path.join(save_path,username)
                newusr = open(compName,"w+")
                password = str(Account.passenCrypt((),password1))
                newusr.write(password[2:-1])
                newusr.close()
                break
            else:
                print("Please Try Again!")

    # Encrypts password and returns it
    def passenCrypt(self,pw):
        bytes = pw.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(bytes,salt)

    # Takes given password and checks it against the encrypted password
    def unlock(self,uname):
        uname = open(f"./accounts/{uname}","r+")
        password = uname.read()
        password = bytes(password, encoding="utf-8")
        attempt = input("Password: ").encode('utf-8')
        result = bcrypt.checkpw(attempt,password)
        return result

    #Creates a list of currently existing accounts and returns it for further use
    def listaccounts(self):
        acctpath = "./accounts"
        dir = os.listdir(acctpath)
        check = False

        while check == False:

            if len(dir) == 0:
                self.newUser()
                quit()
            else:
                accountlist = []
                while True:
                    count = 0
                    for i in dir:
                        count += 1
                        print(f"{count}. {i}")
                        accountlist.append(i)
                    return accountlist

# Function to log user in. Requires listaccounts and unlock to function
    def login(self):
        accountlist = Account.listaccounts(())
        choice = input("Username: ")
        if choice.isnumeric():
            if Account.unlock((), accountlist[int(choice)-1]) == True:
                check = accountlist[int(choice)-1]
                print("Login successful!")
                return check
            else:
                print("Login credentials invalid. Please try again.")
        elif choice.isalpha():
            if Account.unlock((), choice) == True:
                check = choice
                print("Login successful!")
                return check
        else:
            print("Invalid username. Please try again.")




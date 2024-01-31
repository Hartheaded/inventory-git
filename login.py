import bcrypt
import os
import glob
class Account():


    def __init__(self):
        self.username = ""
        self.password = ""
        self.path = "./accounts"
        self.dir = os.listdir(self.path)

    def newUser(self):
        self.username = input("Username:")
        while True:
            password1 = input("Password: ")
            password2 = input("Please repeat password: ")
            if password1 == password2:
                self.password = password1
                save_path = "./accounts"
                compName = os.path.join(save_path,self.username)
                newusr = open(compName,"w+")
                newusr.write(str(self.passenCrypt(self.password)))
                newusr.flush()
                os.fsync(newusr)
                newusr.close()
                break
            else:
                print("Please Try Again!")


    def passenCrypt(self,pw):
        bytes = pw.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(bytes,salt)

    def unlock(self,uname):
        uname = open(f"./accounts/{uname}","r+")
        password = uname.read()
        attempt = input("Password: ")
        attemptbytes = attempt.encode("utf-8")
        print(f"{password}\n{attemptbytes}")
        result = bcrypt.checkpw(attemptbytes,bytes(password))
        return result

    def login(self):
        check = False
        while check == False:
            account = input("Username: ")
            if os.path.isfile(f"./accounts/{account}"):
                self.unlock(account)
                break
            else:
                input("Password: ")
                print("Login Credentials Invalid.")

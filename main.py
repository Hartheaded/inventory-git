from login import Account
from logs import LogFunctions
import os

test = LogFunctions()
print(test.modEntry("HDMI","6",1,"tom"))


'''
while True:
    dir = os.listdir('accounts')
    if len(dir) == 0:
        Account.newUser(())
    else:
        decision = input("Please input numeric selection\n1. login\n2. create account\nresponse: ")
        if decision not in ['1','2']:
            print("Invalid input.")
        elif decision == '2':
            Account.newUser(())
        else:
            break



while True:
    loginattempt = Account.login(())
    print(loginattempt)
    break
'''
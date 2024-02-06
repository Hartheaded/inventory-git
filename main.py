from login import Account
from logs import LogFunctions
import os

def options(numlist):
    numlist.split(',')
    while True
        selection = input("Please input selection. 1-9")
        if not selection.isnumeric():
            print("Please ")


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
    user = Account.login(())
    print(user)
    result = options("1,2,3")


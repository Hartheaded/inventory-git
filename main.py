from login import Account
import os

while True:
    decision = input("Please input numeric selection\n1. login\n2. create account\nresponse: ")
    if decision not in ['1','2']:
        print("Invalid input.")
    elif decision == '2':
        Account.newUser(())
    else:
        break



while True:
    loginattempt = Account.login(())
    if loginattempt.isnumeric():
        print("Numeric")
        break
    elif loginattempt.isalpha():
        print("Alphanumeric")
        break


In-progress python inventory system with login credentials
Current plan is to get it functioning on the terminal before any GUI

This is a personal project used to learn programming, ssh, git and github.
Pull whatever you like and use it for your project, please credit me properly and let me know so I can check it out!

Plan below: In progress like everything else.

'''
Login:
    Option to create or delete a profile
    Option to select profile
    Optional password; MUST BE STORED LOCALLY AND ENCRYPTED
        Typical PW rules apply. Must have at least 1 symbol, 1 numeric and 1 uppercase 8 Char minimum

Homepage:
    Has the ability to create or delete listings.
    Has a list of currently existing cables in storage as well as how many in stock; List should be numbered.
    Each cable should show dongle stock; See bottom of Entry for more detail.
    An option for recent inventory changes with pages of text that you can flip through.
    Option to log out

Entry:
    Must have a list of cable lengths and current stock.
    Should have a modify button to add or subtract cables.
    Should split stock amount between cable lengths: Ex. 3' 6' 10' Etc.
    Should have an inventory log that shows WHO took it out, WHEN it was taken out, and WHY it was needed.
    List of dongles with that cable's output. Ex. If there is an HDMI to DP cable with the DP being the output,
        that should be listed in there too.
'''

'''
PSEUDO CODE

LOGIN:
    User is presented numbered list of accounts that comes from a folder of useraccounts and encrypted passwords
        Filename is account, text inside is their password encrypted by their password. If both strings match, user can login
        On fail, user is reprompted for password.
    - Numbered list of accounts
        - Accounts stored in seperate text document
            - Passwords are encrypted by themselves.

HOMEPAGE:
'''
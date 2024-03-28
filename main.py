menu = '''
~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to Big Money Bank's main banking menu!

1. Check Balance
2. Make a Deposit
3. Widthdrawl Cash
~~~~~~~~~~~~~~~~~~~~~~~~~
'''
new_user = input("Are you a new Big Money Bank user:")
if new_user == 'no':
    account_num = input("Enter your account number:")
    account_pin = input("Enter your account PIN:")
    menu_choice = input(menu)
else:
    new_name = input("What is your name:")
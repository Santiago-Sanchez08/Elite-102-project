import random

import mysql.connector

connection = mysql.connector.connect(user='root',database='elite102project',password='Ka0001970!_08')

cursor = connection.cursor()

menu = '''
~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to Big Money Bank's main banking menu!

1. Check Balance
2. Make a Deposit
3. Widthdrawl Cash
4. Modify Account Information
5.Delete account
~~~~~~~~~~~~~~~~~~~~~~~~~
'''
new_user = input("Are you a new Big Money Bank user:")
while new_user == 'yes':
    new_fname = input("Enter your first name:")
    new_lname = input('Enter your last name:')
    new_pin = input("Enter a PIN:")
    new_amount = input("Enter amount to deposit:")
    new_accountnum = random.randint(1, 1000000)
    newmember = ("INSERT INTO bank" 
                 "(pin, accountnum, totalfunds, firstname, lastname)" 
                 "VALUES (%s, %s, %s, %s, %s)")
    new_memdata =(new_pin, new_accountnum, new_amount, new_fname, new_lname)
    cursor.execute(newmember, new_memdata)
    connection.commit()
    print("Your all set to use Big Money Bank!")
    print("Returning to home menu...")
    new_user = input("Are you a new Big Money Bank user:")


account_pin = input("Enter your account PIN: ")
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
menu_choice = input(menu)

while menu_choice != 1 or menu_choice != 2 or menu_choice != 3 or menu_choice != 4 or menu_choice != 5:
    if menu_choice ==1:
        print('placeholder')

    elif menu_choice == 2:
        pass

    elif menu_choice == 3:
        pass

    elif menu_choice == 4:
        pass

    elif menu_choice == 5:
        pass
    else:
        print('Not a valid option')
        menu_choice = input(menu)
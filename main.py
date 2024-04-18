#from tkinter import *
#from tkinter import ttk

import random

import mysql.connector

connection = mysql.connector.connect(user='sql',database='elite102project',password='Ka0001970!_08')

cursor = connection.cursor()

"""
root = Tk()
root.title = ('Big Bank Banking App')
frame = ttk.Frame(root)
frame['padding'] = 5
frame['borderwidth'] = 2
frame['relief'] = 'sunken'
button = ttk.Button(frame, text='enter', command='buttonpressed')
button.grid()
test=button['text']
print(test)
"""

# Main menu
menu = '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to Big Money Bank's Main Banking Menu!

1. Check Balance
2. Make a Deposit
3. Widthdrawl Cash
4. Modify Account Information
5. Delete account
6. Log Out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# Account settings menu
accountmenu = '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to the Big Money Bank Account Menu!

1. Change PIN
2. Change First Name
3. Change Last Name
4. Show Account Number
5. Exit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# creates new users and puts them in the database
def createuser():
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
    cursor.close()
    print("Your all set to use Big Money Bank!")
    print("Returning to home menu...")
    
# allows to views funds
def viewfunds():
    cursor = connection.cursor()
    checkbalance = ("SELECT totalfunds FROM bank WHERE pin = %s AND firstname = %s AND lastname = %s")
    cursor.execute(checkbalance, (account_pin, first_name, last_name))
    for totalfunds in cursor:
        print("Your total balance is: " + str(totalfunds[0]))
    cursor.close()

# allows deposits and adds the number to the data base
def deposit():
    cursor = connection.cursor()
    deposit = int(input("How much would you like to deposit: "))
    gettotalfunds = ("SELECT totalfunds FROM bank WHERE pin = %s AND firstname = %s AND lastname = %s")
    cursor.execute(gettotalfunds, (account_pin, first_name, last_name))
    for fund in cursor:
        intfund= int(str(fund[0]))
    totalfunds = deposit + intfund
    updatefunds = ("UPDATE bank SET totalfunds = %s WHERE pin = %s AND firstname = %s AND lastname = %s")
    cursor.execute(updatefunds, (totalfunds, account_pin, first_name, last_name))
    connection.commit()
    print("Your total balance is: " + str(totalfunds))
    cursor.close()

# allows withdraws and subtracts the number to the data base
def withdraw():
    cursor = connection.cursor()
    withdraw = int(input("How much would you like to withdraw: "))
    gettotalfunds = ("SELECT totalfunds FROM bank WHERE pin = %s AND firstname = %s AND lastname = %s")
    cursor.execute(gettotalfunds, (account_pin, first_name, last_name))
    for fund in cursor:
        intfund= int(str(fund[0]))
    totalfunds = intfund - withdraw
    updatefunds = ("UPDATE bank SET totalfunds = %s WHERE pin = %s AND firstname = %s AND lastname = %s")
    cursor.execute(updatefunds, (totalfunds, account_pin, first_name, last_name))
    connection.commit()
    print("Your total balance is: " + str(totalfunds))
    cursor.close()

# allows user to change account settings
def accountsettings():
    accountmenuchoice = input(accountmenu)
    while accountmenuchoice != '5':
            # change pin
            if accountmenuchoice == '1':
                cursor = connection.cursor()
                new_pin = input("Enter Your New PIN: ")
                updatepin = ("UPDATE bank SET pin = %s WHERE pin = %s AND firstname = %s AND lastname = %s")
                cursor.execute(updatepin, (new_pin, account_pin, first_name, last_name))
                connection.commit()
                print("PIN Updated")
                cursor.close()
                print('Please log back in using your new pin!')
                exit()
            # Change first name
            elif accountmenuchoice == '2':
                cursor = connection.cursor()
                new_fname = input("Enter Your New First Name: ")
                updatefname = ("UPDATE bank SET firstname = %s WHERE pin = %s AND firstname = %s AND lastname = %s")
                cursor.execute(updatefname, (new_fname, account_pin, first_name, last_name))
                connection.commit()
                print("First name Updated")
                cursor.close()
                print('Please log back in using your new first name!')
                exit()
            # Change last name
            elif accountmenuchoice == '3':
                cursor = connection.cursor()
                new_lname = input("Enter Your New Last Name: ")
                updatelname = ("UPDATE bank SET lastname = %s WHERE pin = %s AND firstname = %s AND lastname = %s")
                cursor.execute(updatelname, (new_lname, account_pin, first_name, last_name))
                connection.commit()
                print("Last name Updated")
                cursor.close()
                print('Please log back in using your last name!')
                exit()
            #View account number
            elif accountmenuchoice == '4':
                cursor = connection.cursor()
                getaccnum = ("SELECT accountnum FROM bank WHERE pin = %s AND firstname = %s AND lastname = %s")
                cursor.execute(getaccnum, (account_pin, first_name, last_name))
                for num in cursor:
                    print("You account number is: " + str(num[0]))
                cursor.close()
                accountmenuchoice = input(accountmenu)
            else:
                print('Invalid option')

        

new_user = input('Are you a new Big Bank user(yes/no): ')
#def new_userdata(new_user):
while new_user == 'yes':
    createuser()
    new_user = input('Are you a new Big Bank user: ')   

#def accountdata():

# Collects user data
account_pin = input("Enter your account PIN: ")
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')


menu_choice = input(menu)
while menu_choice != '6':
#def choices(account_pin, first_name, last_name):
    if menu_choice == '1':
        viewfunds()
        menu_choice=input(menu)

    elif menu_choice == '2':
        deposit()
        menu_choice=input(menu)

    elif menu_choice == '3':
        withdraw()
        menu_choice = input(menu)
        
    elif menu_choice == '4':
        accountsettings()
        menu_choice = input(menu)

    elif menu_choice == '5':
        #allows for account deletion
        cursor = connection.cursor()
        confirmation = input("Are You sure that you would like to delete you account(yes/no): ")
        if confirmation == 'yes':
            deleteaccount = ("DELETE FROM bank WHERE pin = %s AND firstname = %s AND lastname = %s")
            cursor.execute(deleteaccount, (account_pin, first_name, last_name))
            connection.commit()
            print("Account deleted")
            print('Logging out...')
            exit()
        else:
            print('Thank you for staying with us!')
            menu_choice=input(menu)
print("Thank you for banking with Big Bank Banking!")

#new_user = input("Are you a new Big Money Bank user:")
#menu_choice = input(menu)
#choices(accountdata())


#greetingcontent =  StringVar()
#label['textvariable'] = greetingcontent
#label.grid()
#button = ttk.Button(root, text='Enter', command='newuser()')
#button.grid()

import random

import mysql.connector

connection = mysql.connector.connect(user='sql',database='elite102project',password='Ka0001970!_08')

cursor = connection.cursor()

menu = '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to Big Money Bank's Main Banking Menu!

1. Check Balance
2. Make a Deposit
3. Widthdrawl Cash
4. Modify Account Information
5. Delete account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

accountmenu = '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to the Big Money Bank Account Menu!

1. Change PIN
2. Change First Name
3. Change Last Name
4. Show Account Number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
    cursor.close()
    print("Your all set to use Big Money Bank!")
    print("Returning to home menu...")
    new_user = input("Are you a new Big Money Bank user:")


account_pin = input("Enter your account PIN: ")
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
menu_choice = input(menu)

if menu_choice == '1':
    cursor = connection.cursor()
    checkbalance = ("SELECT totalfunds FROM bank WHERE pin = %s AND firstname = %s AND lastname = %s")
    cursor.execute(checkbalance, (account_pin, first_name, last_name))
    for totalfunds in cursor:
        print("Your total balance is: " + str(totalfunds[0]))
    cursor.close()

elif menu_choice == '2':
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

elif menu_choice == '3':
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

elif menu_choice == '4':
    accountmenuchoice = input(accountmenu)
    if accountmenuchoice == '1':
        new_pin = input("Enter Your New PIN: ")
        updatepin = ("UPDATE bank SET pin = %s WHERE pin = %s AND firstname = %s AND lastname = %s")
        cursor.execute(updatepin, (new_pin, account_pin, first_name, last_name))
        connection.commit()
    elif accountmenuchoice == '2':
        new_fname = input("Enter Your New First Name: ")
        updatefname = ("UPDATE bank SET firstname = %s WHERE pin = %s AND firstname = %s AND lastname = %s")
        cursor.execute(updatefname, (new_fname, account_pin, first_name, last_name))
        connection.commit()
    elif accountmenuchoice == '3':
        new_lname = input("Enter Your New Last Name: ")
        updatelname = ("UPDATE bank SET lastname = %s WHERE pin = %s AND firstname = %s AND lastname = %s")
        cursor.execute(updatelname, (new_lname, account_pin, first_name, last_name))
        connection.commit()
    elif accountmenuchoice == '4':
        getaccnum = ("SELECT accountnum FROM bank WHERE lastname = %s WHERE pin = %s AND firstname = %s AND lastname = %s")
        cursor.execute(getaccnum, (account_pin, first_name, last_name))
        for num in cursor:
            print("You account number is: " + num)
    else:
        print('Invalid option')


elif menu_choice == '5':
    confirmation = input("Are You sure that you would like to delete you account: ")
    if confirmation == 'yes':
        deleteaccount = ("DELETE FROM bank WHERE pin = %s AND firstname = %s AND lastname = %s")
        cursor.execute(deleteaccount, (account_pin, first_name, last_name))
        connection.commit()
        print("Account deleted")
    else:
        menu_choice = input(menu)

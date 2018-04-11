import mysql.connector


import sys
import getpass # for password inputs

    

def new_user_detail():
    
    name = input("Enter your name ").strip()

    customer_ID = input("Enter a alpha-numeric customer ID")
    # check for it's uniqueness in the database
    
    number = input("Enter your number ").strip()
    address = input("Enter your Address").strip()
    email = input("Enter your Email").strip()
    type = input("Type of account you want? ")
    account_number = input("choose your account_number")


    while True:
        password = input("Enter a password").strip()
        re_pass = input("Re-Enter your password").strip()
        if password == re_pass:
            break:
        else:
            print("ERROR! password doesn't match")
    # you can have extra detail over here


    # Add these details to the database. The code for DB connection goes here
    # you can also add other validation checks over here


def existing_user():
    #ask for customer id and password for validation check

    c_id = input("Enter your customer ID - ")
    c_pass = input("Enter Your password")

    exist = False
    #check if the user exist and update the variable value

    if exist:
        
        #Fetch name and other prompt details
        while True:
            name = 'xyz'
            print("Hello,{}. Welcome to RUSS bank"):
            print("You have the following options")
            print("1. Change Address")
            print("2. Money Deposit")
            print("3. Money Withdrawl")
            print("4. Print statement")
            print("5. Transfer money")
            print("6. Account Closure")
            print('7.Logout')
            choice = int(input("Enter Your choice -- ").strip())
            
            if choice == 1:
                # code for address change of the same user

                pass
            elif choice ==2:
                # code to Deposit money of the same user
                pass
            elif choice ==3:
                # Code to Withdrawl money of the same user
                pass
            elif choice ==4:
                # print statement of the user from start time to end time
                start = input("enter the start date in dd-mm-yyyy format - ")
                end = input("enter the end date in dd-mm-yyyy format - ")

                #between clause
                pass
            elif choice ==5:
                # transfer money to another account
                account_holder_id = input("Enter the account number on which you have to tranfer the money")
                pass    
            elif choice ==6:
                
                # delete account
                c = input("Are you sure you wanna delete your account.Yes or no")
                pass

            elif choice ==7:
                print('Thank You for your time')
                return

    else:
        print("Invalid credentials")
        return

def admin_interface():
    admin_id = input("enter your admin ID")
    admin_password = input("enter your password")
    
    authentic_admin = False

    #check for admin authentication

    while authentic_admin:
        print("You have the following options")
        print("1. Print Closed accounts")
        print("2. logout")
        c = int(input("Enter your choice - "))

        if c == 1:
            pass
            # print closed account details
        elif c==2:
            print('logging out')
            return






while True:
    print("Welcome to the RUSS banking system")
    print("You have the following options")
    print("1. Sign Up - New Customer")
    print("2. Sign In - Existing Customer")
    print("3. Admin Sign In")
    print("4. Quit")

    choice = int(input("Enter you choice - "))

    if choice == 1:
        new_user_detail()
    elif choice == 2:
        existing_user()
    elif choice == 3:
        admin_interface()
    elif choice == 4:
        print("Thank you for your time")
        sys.exit(0)
    else:
        print("Wrong Choice. Do it again")

    print("\n---------------------------------\n")
        
        

import sys


    

def new_user_detail():
    
    name = input("Enter your name ").strip()

    customer_ID = input("Enter a alpha-numeric customer ID")
    # check for it's uniqueness in the database
    
    number = input("Enter your number ").strip()
    address = input("Enter your Address").strip()
    email = input("Enter your Email").strip()

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
        pass
    elif choice == 4:
        print("Thank you for your time")
        sys.exit(0)
    else:
        print("Wrong Choice. Do it again")

    print("\n---------------------------------\n")
        
        

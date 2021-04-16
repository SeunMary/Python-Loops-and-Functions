import random
import datetime
currentDateandTime = datetime.datetime.now()
print("Current Date and Time is: %s " % currentDateandTime)

database = {
    4718511073: ['Mary', 'Omange', 'omange.seun@gmail.com','OmangeM', 5000]
                 }
def init():
    print("Welcome to GTBank")

    have_account = int(input("Do you have account with us: 1. (Yes) 2. (No) \n"))
    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("Thank you for banking with us")
        init()


def login():
    print("********* Login ***********")

    accountNumberFromUser = int(input('What is your account number? \n'))
    password = input('What is your password:\n')

    for account_number,userDetails in database.items():
        if(account_number == accountNumberFromUser):
            if(userDetails[3] == password):
                bank_operation(userDetails)
    else:
        print('Thank you for banking with us')
        login()
       
        
def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    account_number = generation_account_number()

    database[account_number] = [first_name, last_name, email, password, 0]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()



def bank_operation(userDetails):
    print('Welcome %s %s' % ( userDetails[0],userDetails[1]) )
    
    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:
        
        deposit_operation()
    elif selected_option == 2:
        
        withdrawal_operation()
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("Thank you for Banking with us")
        bank_operation(userDetails)

def deposit_operation():
    oldBalance = 5000
    deposit = int(input("How much would you like to deposit? \n" ))
    currentBalance = deposit + oldBalance
    print("Current Balance is %s" % currentBalance)
    
def withdrawal_operation():
    initialBalance = 5000
    withdrawnMoney = int(input("How much would you like to withdraw? \n"))
    if initialBalance >= withdrawnMoney:
        withdrawBalance = initialBalance - withdrawnMoney
        print("Take your cash")
        print("Current Balance is %s" % withdrawBalance)

    else:
        print("Insufficient Balance")


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    login()


init()


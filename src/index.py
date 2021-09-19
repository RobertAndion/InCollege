import re

from src.database_access import database_access as Database


def get_credentials():
    # returns the credentials. Called either in login() or register()
    user = input('Enter username: ')
    password = input('Enter password: ')
    return (user, password)

# gets called when the user chooses to login


def login(db):
    while True:
        cred = get_credentials()
        # checks if the credentials exist in the users table
        find_user = ('SELECT * FROM users WHERE username = ? AND password = ?')
        res = db.execute(find_user, cred)
        if res:
            print('You have successfully logged in\n')
            return True
        else:
            print('Incorrect username / password, please try again\n')
            return False

# gets called when the user chooses to register


def register(db):
    # checking the number of accounts already registered
    num_accounts = len(db.execute('SELECT * FROM users'))
    if int(num_accounts) >= 5:
        print("All permitted accounts have been created, please come backlater\n")
    else:
        # if a new user is allowed to register, it prompts them to enter credentials
        cred = get_credentials()
        # the below function returns a boolean as to whether or not the password is secure
        satisfies = is_password_secure(cred[1])
        if satisfies:
            # posting data to the database
            db.execute("INSERT INTO users VALUES (?, ?)", cred)
            print("An account for " +
                  cred[0] + " was registered successfully... Redirecting\n")
            return True
        else:
            print('Weak Password')
            return False

# returns a boolean whether or not the password is secure. Helper function for the register function


def is_password_secure(pw):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%^()*#?&])[A-Za-z\d@$!#%^()*?&]{8,12}$"
    pattern = re.compile(reg)
    res = re.match(pattern, pw)
    return res != None


# executes when the user either successfully logged in or registered. Returns the next choice the user makes


def logged_in():
    option = int(input(
        "1- Search for a job\n2- Find people you may know\n3- learn a new skill\nEnter a choice: "))
    if option == 1 or option == 2 or option == 3:
        return option

# function gets called for the first two options


def construction():
    print("\nunder construction\n")

# gets called when user chooses to learn a new skill


def skills():
    skill = input(
        '\n1- JavaScript\n2- Python\n3- SQL Sever\n4- MongoDB\n5- Design Patterns\nEnter a choice: ')
    if skill:
        construction()
    back = input('Return to main menu? y/n: ').lower()
    if back == 'y':
        option = logged_in()
        # if the user chooses to learn a new skill again, they'll get the skills prompt again
        if option == 3:
            skills()


# ================ MAIN ==================
# you can think of it as the driver function. It's where everything starts
def main(db: Database):
    # Stores possible functions (actions for the user) to call in the home page
    home_options = {
        1: login,
        2: register
    }
    # Possible functions to call after the user logs in, construction is repeated because both option 1 and 2 will lead to 'under construction' message
    logged_in_options = {
        1: construction,
        2: construction,
        3: skills
    }

    # initial prompt (home page)
    first_action = int(
        input('Welcome to InCollege:\n1- Login\n2- Register\nEnter a choice: '))
    # calls the appropriate function based on the user choice
    if(first_action == 1 or first_action == 2):
        res = home_options[first_action](db)
        # if the user logs in or registers successfully
        if res:
            # run logged_in() and store the returned value (which represent the next action to take)
            option = logged_in()
            logged_in_options[option]()

    else:
        print("Invalid option")

if __name__ == "__main__":
    # Making a connection to the database. If it doesn't already exist, it creates it
    db = Database("InCollege.sqlite3")
    main(db)
    db.close()

#User list, not sure how to save it or do anything other then print it at the moment.

#Hi Nick! currently your username is set to NickCornell and password is 1234. do whatever you'd like to them.
#just use admin for testing though, it's much faster
UserList = {'0000': {'First Name': 'Admin', 'Last Name': 'Admin', 'Username': 'a', 'Password': 'a'},
            '0001': {'First Name': 'Nick', 'Last Name': 'Cornell','Username': 'NickCornell', 'Password': '1234'},
            '0002': {'First Name': 'Brett', 'Last Name': 'Hammerschmidt','Username': 'Bretthammer', 'Password': '1212'}}

#security check
loginSecure = False

#-----LOGGING IN--------------------------------------------------------------------------------------------------------------------------------
#Function for logging in
def login(Username):
    #input for password
    Password = input('Enter your Password: ')
    #searches through dictionary for matching username, then matching password
    for k in UserList.keys():
        if Username in UserList[k]['Username']:
            print()
            if Password in UserList[k]['Password']:
                print('Logging In...')
                print()
                #creating globals because I use them to print things in the menu
                global CurrentUser
                CurrentUser = Username
                #global security check
                global loginSecure
                loginSecure = True
            else:
                print('Invalid User Login!')

#------MAIN INPUT SCREEN-------------------------------------------------------------------------------------------------------------------------------

def Main(UserInput):
        #Create user
    if UserInput == 'create user' or UserInput == 'c':
        AnotherUser = 'yes' or 'y'
        while AnotherUser == 'yes' or AnotherUser == 'y':
            CreateUser()
            AnotherUser = input('Would you like to add another USER yes or no? ')
            if AnotherUser == 'no' or AnotherUser == 'n':
                break
    
    #Log Out
    elif UserInput == 'log out' or UserInput == 'l':
        print('Logged Out!')
        global loginSecure
        loginSecure = False

    #Print User
    elif UserInput == 'print user' or UserInput == 'p':
        PrintUserList()
        input('Enter Anything to Return to Menu: ')
    
    #Remove User
    elif UserInput == 'remove user' or UserInput == 'r':
        removeUser()

    #Enquire about a specific User
    elif UserInput == 'enquire user' or UserInput == 'e':
        enquireUser()

    #Modify User
    elif UserInput == 'modify user' or UserInput == 'm':
        modifyUser()

#------PRINTING USER-------------------------------------------------------------------------------------------------------------------------------

#function for printing the user list
def PrintUserList():
    #helps with security
    if loginSecure == True:
        print('--------------------------------------------USER-LIST----------------------------------------------')
        for p_id, p_info in UserList.items():
            print("\nUSER ID:", p_id)
    
            for key in p_info:
                print(key + ':', p_info[key])
        print()
        print('--------------------------------------------USER-LIST----------------------------------------------')

#------CREATING USER-------------------------------------------------------------------------------------------------------------------------------

#Function for creating user
def CreateUser():
    #helps with security
    if loginSecure == True:
        print('--CURRENT-USERS--')
        PrintUserList()
        print()
        print('--CREATING-USER--')
        print('USERID (FIRST NAME : LAST NAME : USERNAME : PASSWORD)')

        #getting input for USERID
        UserID = input('UserID: ')
        while UserID in UserList.keys():
            print('User ID Already Exists!')
            UserID = input('UserID: ')

        #getting input for first name
        First = input('First Name: ')

        #getting input for last name
        Last = input('Last Name: ')

        #getting input for username
        while True:
            username = input('Username: ')

            # Check if the username already exists
            username_exists = False
            for userID in UserList.values():
                if userID['Username'] == username:
                    username_exists = True
                    break

            if username_exists:
                print('Username Already Exists!')
            else:
                break
                
        #getting input for password
        Password = input('Password: ')
        #if statement checking if password is longer then 8 characters
        #else print password is weak
        while len(Password) > 8:
            break
        else:
            print('Password is Weak. Recommended Password is 8 characters long.')
            Password = input('Password: ')

        #creating user from inputs
        UserList[UserID] = {'First': First, 'Last': Last, 'Username': username, 'Password': Password}

        print('--CREATING-USER--')
        print()
        print('New User List')
        PrintUserList()

    else:
        print('Login Not Secure!')

#------REMOVING USER-------------------------------------------------------------------------------------------------------------------------------

def removeUser():
    print('Remove user')

#-----ENQUIRE USER--------------------------------------------------------------------------------------------------------------------------------

def enquireUser():
    print('Enquire User')

#-----MODIFY USER--------------------------------------------------------------------------------------------------------------------------------

def modifyUser():
    print('Modify User')

#-------------------------------------------------------------------------------------------------------------------------------------




#Main Code after Logging in
while True:

    #security Check
    while loginSecure == False:

        #Main Menu before logging in
        print('--------------------------------------------USER-SYSTEM--------------------------------------------')
        print('What Would you like to do?')
        print('')
        print('exit or \'x\'- Ends the program')
        print('login or \'l\'- Login with your Username and Password')
        print('')
        print('--------------------------------------------USER-SYSTEM--------------------------------------------')


        #Input for either end or login
        FirstUserInput = input('Input: ')
        print('--------------------------------------------USER-SYSTEM--------------------------------------------')

        #input for login
        if FirstUserInput == 'login' or FirstUserInput == 'l':
            #Getting userinput for username
            UsernameInput = input('Enter your Username: ')
            #incase you want to end the program
            #calling function Login
            login(UsernameInput)
            if loginSecure == False:
                print('Invalid Login Credentials!')

        #break if user input was end
        elif FirstUserInput == 'exit' or FirstUserInput == 'x':
            exit()

    #Printing main menu and the commands
    print('---------------------------------------------------------------------------------------------------')
    print('Securely logged into', CurrentUser)
    print('---------------------------------------------------------------------------------------------------')
    print()
    print('Commands:')
    print()
    print('--Every Command can be Shortened to it\'s First Letter--')
    print('create user - Create User Screen')
    print('remove user - Remove User Screen')
    print('enquire user - Enquire User Screen')
    print('modify user - Modify User Screen')
    print('print user - Prints User List')
    print('log out')
    print()
    print('---------------------------------------------------------------------------------------------------')
    
    #user input for what you'd like to do
    userInputMain = input('What would you like to do: ')
    Main(userInputMain)

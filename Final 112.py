#User list, not sure how to save it or do anything other then print it at the moment.

#Hi Nick! currently your username is set to NickCornell and password is 1234. do whatever you'd like to them.
#just use admin for testing though, it's much faster
UserList = {'0000': {'First': 'admin', 'Last': 'admin', 'Username': 'admin', 'Password': 'admin'},
            '0001': {'First': 'Nick', 'Last': 'Cornell','Username': 'NickCornell', 'Password': '1234'},
            '0002': {'First': 'Brett', 'Last': 'Hammerschmidt','Username': 'Bretthammer', 'Password': '1212'}}

#security check
loginSecure = False

#-------------------------------------------------------------------------------------------------------------------------------------
#Function for logging in
def login(Username):
    #input for password
    Password = input('Enter your Password: ')
    #searches through dictionary for matching username, then matching password
    for k in UserList.keys():
        if Username in UserList[k]['Username']:
            print()
            if Password in UserList[k]['Password']:
                print('Logging In')
                #creating globals because I use them to print things in the menu
                global CurrentUser
                CurrentUser = Username
                #global security check
                global loginSecure
                loginSecure = True
            else:
                print('Invalid User Login!')

#-------------------------------------------------------------------------------------------------------------------------------------

#function for printing the user list
def PrintUserList():
    #helps with security
    if loginSecure == True:
        print('------------------------------USER-LIST------------------------------')
        for k in UserList.keys():
            print('User ID:', iter(UserList))
            print('Name: ', UserList[k]['First'])
            print('Last Name:', UserList[k]['Last'])
            print('Username:', UserList[k]['Username'])
            print('Password:', UserList[k]['Password'])
            print()
        print('------------------------------USER-LIST------------------------------')

#-------------------------------------------------------------------------------------------------------------------------------------

#Function for creating user
def CreateUser():
    #helps with security
    if loginSecure == True:

        print('USERID (FIRST NAME : LAST NAME : USERNAME : PASSWORD)')

        #getting input for USERID
        UserID = input('UserID: ')
        if UserID in UserList:
            print('UserID Already Exists')
            while UserID in UserList:
                UserID = input('UserID: ')

        #getting input for first name
        First = input('First Name: ')

        #getting input for last name
        Last = input('Last Name: ')

        #getting input for username
        Username = input('Username: ')
        for k in UserList.keys():
            if Username in UserList[k]['Username']:
                print('Username Already Exists!')
                Username = input('Username: ')

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
        UserList[UserID] = {'First': First, 'Last': Last, 'Username': Username, 'Password': Password}
        PrintUserList()

    else:
        print('Login Not Secure!')

#-------------------------------------------------------------------------------------------------------------------------------------

def RemoveUser():
    print('Remove user')

def EnquireUser():
    print('Enquire User')

def ModifyUser():
    print('Modify User')

##############################################################################################################################

#Main Code after Logging in
while True:

    #security Check
    while loginSecure == False:

        #Main Menu before logging in
        print('--------------------------------------------USER-SYSTEM--------------------------------------------')
        print('What Would you like to do?')
        print('')
        print('end - Ends the program')
        print('login - Login with your Username and Password')
        print('')

        #Input for either end or login
        FirstUserInput = input('Input: ')
        print('--------------------------------------------USER-SYSTEM--------------------------------------------')

        #input for login
        if FirstUserInput == 'login':
            #Getting userinput for username
            UsernameInput = input('Enter your Username: ')
            #incase you want to end the program
            #calling function Login
            login(UsernameInput)
            if loginSecure == False:
                print('Invalid Login Credentials!')

        #break if user input was end
        elif FirstUserInput == 'end':
            break

    #breaking the loop again to prevent getting in after not logging in
    if FirstUserInput == 'end':
        break

    #Printing main menu and the commands
    print('---------------------------------------------------------------------------------------------------')
    print('Securely logged into', CurrentUser)
    print('---------------------------------------------------------------------------------------------------')
    print('Commands:')
    print()
    print('Create User')
    print('Remove User')
    print('Enquire User')
    print('Modify User')
    print('Print User')
    print('Log Out')
    print()
    
    #user input for what you'd like to do
    UserInput = input('What would you like to do? ')

    #Create user
    if UserInput == 'Create User':
        AnotherUser = 'yes'
        while AnotherUser == 'yes':
            CreateUser()
            AnotherUser = input('Would you like to add another USER yes or no? ')
            if AnotherUser == 'no':
                break
    
    #Log Out
    elif UserInput == 'Log Out':
        print('Logged Out!')
        loginSecure = False

    #Print User
    elif UserInput == 'Print User':
        PrintUserList()
        input('Enter Anything to Return to Menu: ')
    
    #Remove User
    elif UserInput == 'Remove User':
        RemoveUser()

    #Enquire about a specific User
    elif UserInput == 'Remove User':
        EnquireUser()

    #Modify User
    elif UserInput == 'Remove User':
        ModifyUser()


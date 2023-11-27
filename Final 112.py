#User list, not sure how to save it or do anything other then print it at the moment.

#Hi Nick! currently your username is set to NickCornell and password is 1234. do whatever you'd like to them.
#just use admin for testing though, it's much faster
UserList = {'0000': {'First Name': 'Admin', 'Last Name': 'Admin', 'Username': 'a', 'Password': 'a'},
            '0001': {'First Name': 'Nick', 'Last Name': 'Cornell','Username': 'NickCornell', 'Password': '1234'},
            '0002': {'First Name': 'Brett', 'Last Name': 'Hammerschmidt','Username': 'Bretthammer', 'Password': '1212'}}

#security check
loginSecure = False

#---CHECKING-PASSWORDS-----------------------------------------------------------------------------------------------------------------------------
#function for checking if passwords are strong
#information on how to do this, it took me forever to find anything on checking every character instead of the whole string.
#https://www.w3schools.com/python/ref_func_any.asp#:~:text=The%20any()%20function%20returns,()%20function%20will%20return%20False.
#https://www.geeksforgeeks.org/python-test-if-string-contains-any-uppercase-character/


def passwordCheck(password):
    passwordChecker = True

    #if passwords are less then 6 characters
    if len(password) < 6:
        print('Length of password should be atleast 6 Characters long.')
        passwordChecker = False

    #if passwords do not contain numbers
    if not any(character.isdigit() for character in password):
        print('Password should have at least one numeral')
        passwordChecker = False

    #if password doesn't contain a capital letter
    if not any(character.isupper() for character in password):
        print('Password should have at least one uppercase letter')
        passwordChecker = False

    #send back true or false
    return passwordChecker
    

#---TITLES------------------------------------------------------------------------------------------------------------------------------------------
#function for titles and length
def titleBuilder(name, length):
    name = name.center(length, '-')
    return print(name)

#-----LOGGING IN-------------------------------------------------------------------------------------------------------------------------------------
#Function for logging in
def login(Username):
    #input for password
    Password = input('Enter your Password: ')

    #searches through dictionary for matching username, then matching password of userID
    for userID, user_info in UserList.items():
        if Username == user_info['Username'] and Password == user_info['Password']:
            print('Logging In...')
            
            # creating globals because I use them to print things in the menu
            global CurrentUser
            CurrentUser = Username
            
            # global security check
            global loginSecure
            loginSecure = True

#------MAIN INPUT SCREEN-------------------------------------------------------------------------------------------------------------------------------

def Main(UserInput):

        #Create user
        if UserInput == 'create user' or UserInput == 'c' or UserInput == 'Create User' or UserInput == 'Create' or UserInput == 'create':
            CreateUser()

        #Log Out
        elif UserInput == 'log out' or UserInput == 'l' or UserInput == 'Log Out' or UserInput == 'logout' or UserInput == 'Logout':
            print('Logged Out!')
            global loginSecure
            loginSecure = False

        #Print User
        elif UserInput == 'print user' or UserInput == 'p' or UserInput == 'print' or UserInput == 'Print' or UserInput == 'Print User':
            PrintUserList()
            input('Enter Anything to Return to Menu: ')
            
        #Remove User
        elif UserInput == 'remove user' or UserInput == 'r' or UserInput == 'Remove User' or UserInput == 'remove' or UserInput == 'Remove':
            removeUser()

        #Enquire about a specific User
        elif UserInput == 'inquire user' or UserInput == 'i' or UserInput == 'Inquire' or UserInput == 'Inquire User' or UserInput == 'Inquire':
            inquireUser()

        #Modify User
        elif UserInput == 'modify user' or UserInput == 'm' or UserInput == 'Modify' or UserInput == 'modify' or UserInput == 'Modify User':
            modifyUser()

#------PRINTING USER--------------------------------------------------------------------------------------------------------------------------------

#function for printing the user list
def PrintUserList():
    #helps with security
    if loginSecure == True:

        titleBuilder('USER-LIST',100)
        
        #(user_id(user_info))
        for user_id, user_info in UserList.items():
            print("\nUSER ID:", user_id)
    
            for key in user_info:
                print(key + ':', user_info[key])

        print()
        titleBuilder('USER-LIST',100)

#------CREATING USER--------------------------------------------------------------------------------------------------------------------------------

#Function for creating user
def CreateUser():

    while True:

        #helps with security
        if loginSecure == True:
            titleBuilder('CREATE-USER',100)
            #getting input for USERID
            
            
            CreateUserMenu = input('''Create User Menu
-
Create User - 'c'
Print User - 'p'
Exit - 'x'
-
Input: ''')
            
            #checking what was entered
            #Exit
            if CreateUserMenu == 'x' or CreateUserMenu == 'Exit' or CreateUserMenu == 'exit':
                return
            
            #Print User
            elif CreateUserMenu == 'p' or CreateUserMenu == 'print' or CreateUserMenu == 'Print User' or CreateUserMenu == 'print user':
                PrintUserList()

            #Create User
            elif CreateUserMenu == 'c' or CreateUserMenu == 'create' or CreateUserMenu == 'Create User' or CreateUserMenu == 'create user':
                UserID = input('''USERID (FIRST NAME : LAST NAME : USERNAME : PASSWORD)
-                           
USERID: ''')
        
                
                while UserID in UserList.keys():
                    titleBuilder('-',100)
                    print('User ID Already Exists!')
                    titleBuilder('-',100)
                    UserID = input('''USERID (FIRST NAME : LAST NAME : USERNAME : PASSWORD)
-                           
USERID: ''')

                #getting input for first name
                First = input('First Name: ')

                #getting input for last name
                Last = input('Last Name: ')

                #getting input for username and checking if it exists, loop until it has one that doesn't exist
                while True:
                    username = input('Username: ')

                    # Check if the username already exists
                    username_exists = False

                    #checking if username already in userlist
                    for userID in UserList.values():
                        if userID['Username'] == username:
                            username_exists = True
                            break

                    if username_exists:
                        print('Username Already Exists!')
                    else:
                        break
                        
                #getting input for password
                titleBuilder('-',100)
                Password = input('''Password Must Contain:
-
Number.
Upper Case Character.
6 Characters.
-
Password: ''')
                
                #if statement checking if password is longer then 8 characters
                #else print password is weak
                while True:
                    if (passwordCheck(Password)):
                        #creating user from inputs
                        UserList[UserID] = {'First': First, 'Last': Last, 'Username': username, 'Password': Password}
                        titleBuilder('-',100)
                        print('User ID:',UserID,'Created!')
                        break

                    else:
                        Password = input('Password: ')

            #incase security check fails
        else:
            print('Login Not Secure!')

#------REMOVING USER-----------------------------------------------------------------------------------------------------------------------------

def removeUser():
    #security check
    if loginSecure == True:

        #not sure how else to double break out of a loop
        breaker = False
        #loops until you wanna stop removing users
        while breaker == False:

            #loop for making sure the USER ID exists
            while True:

                titleBuilder('REMOVE-USER',100)
                removeMenu = input('''What information do you have about the user you want to delete?
-
User ID - 'id'
Username - 'u'
Exit - 'x'
-
Input: ''')
                titleBuilder('-',100)

                #exiting remove menu
                if removeMenu == 'x' or removeMenu == 'Exit' or removeMenu == 'exit':
                    #for double loop
                    breaker = True
                    break
                
                #removing by user ID
                elif removeMenu == 'User ID' or removeMenu == 'id' or removeMenu == 'user id':
                    userID = input('''User ID is in the form '0000'
-
UserID: ''')
                    #if userID in userList
                    if userID in UserList:

                        #print user info
                        for key in UserList[userID]:
                            print(key, ':', UserList[userID][key])
                        titleBuilder('-',100)

                        #Check if they wanna delete
                        confirmation = input('''Is this the user you would like to remove?
-
Yes - 'y'
No - 'n'
-
Input: ''')
                        #confirm yes
                        if confirmation == 'y' or confirmation == 'yes' or confirmation == 'Yes':
                            del UserList[userID]
                            titleBuilder('-',100)
                            print('User ID:',userID, 'Removed!')

                        #confirm no
                        if confirmation == 'n' or confirmation == 'no' or confirmation == 'No':
                            titleBuilder('-',100)
                            print('User ID:',userID, 'not Removed!')
                            break

                    #if userID not in userList print
                    else:
                        print('User is not in the database!')

                #remove user with username
                elif removeMenu == 'u' or removeMenu == 'Username' or removeMenu == 'username':

                    #incase username does no exist i need a check
                    usernameExists = False
                    Username = input('Username: ')

                    #for (user_id(userinfo))
                    for user_id, user_info in UserList.items():

                        #if Username is found in UserList
                        if user_info['Username'] == Username:
                            titleBuilder('-', 100)

                            #print user ID
                            print('User ID: ', user_id)

                            #print user info by user id
                            for key, value in user_info.items():
                                print(key, ':', value)
                                usernameExists = True
                            titleBuilder('-', 100)

                    #if a username exists run this
                    if usernameExists == True:
                        #confirmation check
                        confirmation = input('''Is this the user you would like to remove?
-
Yes - 'y'
No - 'n'
-
Input: ''')
                        #remove user with username
                        if confirmation == 'y' or confirmation == 'yes' or confirmation == 'Yes':
                            del UserList[user_id]
                            titleBuilder('-',100)
                            print('Username:',Username, 'Removed!')

                        #don't remove user from username
                        if confirmation == 'n' or confirmation == 'no' or confirmation == 'No':
                            titleBuilder('-',100)
                            print('Username:',Username, 'not Removed!')
                            break
                    
                    #incase user does not exist
                    else:
                        print('Username is not in database!')
                
                            
#-----INQUIRE USER--------------------------------------------------------------------------------------------------------------------------------

def inquireUser():

    while True:
        titleBuilder('INQUIRE-USER',100)
        userInput = input('''What information do you have about the user?
                        
-
Username - 'u'
User ID - 'id'
Exit - 'x'
-                            
Input: ''')
        
        #Username Search
        if userInput == 'u' or userInput == 'Username' or userInput == 'username':
            Username = input('Username: ')
            
            #searching through list for username (UserID (User_info = FIRST NAME : LAST NAME : USERNAME : PASSWORD))
            for user_id, user_info in UserList.items():

                #if Username is found in UserList
                if user_info['Username'] == Username:
                    titleBuilder('-', 100)

                    #print user ID and info
                    print('User ID: ', user_id)

                    for key, value in user_info.items():
                        print(key, ':', value)

                if user_info['Username'] != Username:
                    Userfound = False

            if Userfound == False:
                print('User not found in Database!')

            titleBuilder('-',100)
            input('Enter Anything to Return to Menu: ')

        #User ID Seach
        elif userInput == 'id' or userInput == 'User ID' or userInput == 'user id':
            titleBuilder('-',100)
            UserID = input('''User ID is in the form '0000'
-
UserID: ''')

            #try and except incase user does not exist or user inputs a letter or something wrong
            try:
                for key in UserList[UserID]:
                    print(key, ':', UserList[UserID][key])
            except KeyError:
                print('User not found in Database!')

            titleBuilder('-',100)
            input('Enter Anything to Return to Menu: ')

        #Exit search
        elif userInput == 'x' or userInput == 'exit' or userInput == 'Exit':
            return
        
        else:
            titleBuilder('-',100)
            print('Invalid Command!')
    
    #enquire about a user from UserID or

#-----MODIFY USER---------------------------------------------------------------------------------------------------------------------------------

def modifyUser():
    print('Modify User')

#-------------------------------------------------------------------------------------------------------------------------------------------------


#Main Code after Logging in
while True:

    #security Check
    while loginSecure == False:

        #Main Menu before logging in
        titleBuilder('USER-SYSTEM',100)
        print('''What Would you like to do?
              
-
exit or 'x'- Ends the program
login or 'l'- Login with your Username and Password
-''')
        titleBuilder('USER-SYSTEM',100)


        #Input for either end or login
        FirstUserInput = input('Input: ')
        titleBuilder('USER-SYSTEM',100)

        #input for login
        if FirstUserInput == 'login' or FirstUserInput == 'l':
            #Getting userinput for username
            UsernameInput = input('''Login Credentials:
-
Enter your Username: ''')
            
            #calling function Login
            login(UsernameInput)
            if loginSecure == False:
                print('Invalid Login Credentials!')

        #break if user input was end
        elif FirstUserInput == 'exit' or FirstUserInput == 'x':
            exit()

    #Printing main menu and the commands
    titleBuilder('-',100)
    print('''Securely logged into''', CurrentUser)
    titleBuilder('-',100)
    print('''Commands:
                
-
Create User  - 'c'   Create User Screen.
Remove User  - 'r'   Remove User Screen.
Inquire User - 'i'   inquire User Screen.
Modify User  - 'm'   Modify User Screen.
Print User   - 'p'   Prints User List.
Log Out      - 'l'   Logs out.
-''')
    
    titleBuilder('-',100)
    #user input for what you'd like to do
    userInputMain = input('What would you like to do: ')
    Main(userInputMain)
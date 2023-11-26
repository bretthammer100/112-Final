#User list, not sure how to save it or do anything other then print it at the moment.

#Hi Nick! currently your username is set to NickCornell and password is 1234. do whatever you'd like to them.
#just use admin for testing though, it's much faster
UserList = {'0000': {'First Name': 'Admin', 'Last Name': 'Admin', 'Username': 'a', 'Password': 'a'},
            '0001': {'First Name': 'Nick', 'Last Name': 'Cornell','Username': 'NickCornell', 'Password': '1234'},
            '0002': {'First Name': 'Brett', 'Last Name': 'Hammerschmidt','Username': 'Bretthammer', 'Password': '1212'}}

#security check
loginSecure = False

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
    #searches through dictionary for matching username, then matching password
    for k in UserList.keys():
        if Username in UserList[k]['Username']:
            print()
            if Password in UserList[k]['Password']:
                print('Logging In...')
                #creating globals because I use them to print things in the menu
                global CurrentUser
                CurrentUser = Username
                #global security check
                global loginSecure
                loginSecure = True

#------MAIN INPUT SCREEN-------------------------------------------------------------------------------------------------------------------------------

def Main(UserInput):
        #Create user
    #using try so that in the event you input something wrong i can say so
    try:
        #this looks complacted to me but it's really just asking if you want to make another user after making your first
        if UserInput == 'create user' or UserInput == 'c':
            CreateUser()

        
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
        elif UserInput == 'inquire user' or UserInput == 'i':
            inquireUser()

        #Modify User
        elif UserInput == 'modify user' or UserInput == 'm':
            modifyUser()
    finally:
        print('Invalid Command!')

#------PRINTING USER--------------------------------------------------------------------------------------------------------------------------------

#function for printing the user list
def PrintUserList():
    #helps with security
    if loginSecure == True:
        titleBuilder('USER-LIST',100)
        for p_id, p_info in UserList.items():
            print("\nUSER ID:", p_id)
    
            for key in p_info:
                print(key + ':', p_info[key])
        print()
        titleBuilder('USER-LIST',100)

#------CREATING USER--------------------------------------------------------------------------------------------------------------------------------

#Function for creating user
def CreateUser():
    #helps with security
    if loginSecure == True:
        titleBuilder('CURRENT-USERS',20)
        PrintUserList()
        titleBuilder('CREATE-USER',100)

        #getting input for USERID
        UserID = input('''USERID (FIRST NAME : LAST NAME : USERNAME : PASSWORD)
-
'User ID to create' - format in '0000'
Exit - 'x'
-
Input: ''')
        if UserID == 'x' or UserID == 'Exit' or UserID == 'exit':
            return
        while UserID in UserList.keys():
            titleBuilder('-',100)
            print('User ID Already Exists!')
            titleBuilder('-',100)
            UserID = input('''USERID (FIRST NAME : LAST NAME : USERNAME : PASSWORD)
-
'User ID to create' - format in '0000'
Exit - 'x'
-
Input: ''')

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

        titleBuilder('CREATE-USER',100)

        while True:
            #another user input
            AnotherUser = input('''
Would you like to add another USER? 
-
Yes - 'y'
No - 'n'
-
Input: ''')
            if AnotherUser == 'yes' or AnotherUser == 'y' or AnotherUser == 'Yes':
                CreateUser()
            if AnotherUser == 'no' or AnotherUser == 'n' or AnotherUser == 'No':
                return
        #incase security check fails
    else:
        print('Login Not Secure!')


#------REMOVING USER-----------------------------------------------------------------------------------------------------------------------------

def removeUser():
    #security check
    if loginSecure == True:
        #loops until you wanna stop removing users
        while True:
            #loop for making sure the USER ID exists
            while True:
                PrintUserList()
                titleBuilder('REMOVE-USER',100)
                userID = input('''What is the User ID of the Profile you'd like to remove?
                               
-
'User ID to delete' - format is in '0000'
Exit - 'x'
-                            
Input: ''')
                try:
                    if userID == 'x' or userID == 'Exit' or userID == 'exit':
                        breaker = True
                        break
                    for key in UserList[userID]:
                        print(key, ':', UserList[userID][key])
                    break
                #checking if it exists
                except KeyError:
                    print('Invalid User ID!')
            titleBuilder('-',100)
            if breaker == True:
                break

            #loop for checking confirmation
            while True:
                #input for confirming delete
                userIDConfirmation = input('''
Is this for sure the user you want to Delete?
-
Yes - "y" Confirm delete.
No  - "n" Not Confirmed.
-
Input: ''')
        
                if userIDConfirmation == 'yes' or userIDConfirmation == 'Yes' or userIDConfirmation == 'y':
                    #remove user
                    del UserList[userID]
                    print('User removed!')
                    titleBuilder('REMOVE-USER',100)

                    #checking if you wanna remove another user
                    anotherInput = input('''
Would you like to Remove another user?
-
Yes - "y"
No  - "n"
-
Input: ''')
                    if anotherInput == 'yes' or anotherInput == 'Yes' or anotherInput == 'y':
                        removeUser()

                    elif anotherInput == 'no' or anotherInput == 'No' or anotherInput == 'n':
                        return False
                    
                #returning to start if confirmation returns no
                elif userIDConfirmation == 'no' or userIDConfirmation == 'No' or userIDConfirmation == 'n':
                    print('User not removed! Returning to start.')
                    break

                #incase you input something invalid
                else:
                    print('Improper input!')
    else:
        #incase security check fails
        print('Login Not Secure!')



#-----INQUIRE USER--------------------------------------------------------------------------------------------------------------------------------

def inquireUser():
    print('Inquire User')
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
            #incase you want to end the program
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
    print('''
Commands:
    
--Every Command can be Shortened to it\'s First Letter--
          
-
create user - Create User Screen
remove user - Remove User Screen
inquire user - inquire User Screen
modify user - Modify User Screen
print user - Prints User List
log out
-''')
    titleBuilder('-',100)
    #user input for what you'd like to do
    userInputMain = input('What would you like to do: ')
    Main(userInputMain)

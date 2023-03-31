import getpass
import re


def account():
    user_status = ''
    users_data = []
    sign = True
    while user_status not in ['login', 'signup']:
        user_status = input("for log in enter 'login', otherwise 'signup': " )
    

    
    if user_status == 'login':
        usr_name = input("enter your user name: ")
        psscode = getpass.getpass("enter the password(the letters has to be > 3, < 10): ")
        
        sign = False
        user_data = "("+usr_name+': '+psscode+")"
            
        pattern = r'\W\w{3,10}\W\s\w{3,10}\W' 
        
        f = open("accnt_info.txt", 'r')
        info = f.read()
        khan = re.findall(pattern, info)
        
        availability = user_data in khan
        if availability == True:
            print("login succesful!!!")
            
        while availability == False:
            print("account is not availible!!")
            usrSecondOption = input("wanna sign up!?, insert '1'; and '0' for try again!")
            if usrSecondOption == '1':
                user_status = 'signup'
                break
            if usrSecondOption == '0':
                user_status = 'login'
                pass
            
            usr_name = input("enter your user name: ")
            psscode = getpass.getpass("enter the password(the letters has to > 3, < 10): ")

            sign = False
            user_data = "("+usr_name+': '+psscode+")"

            pattern = r'\W\w{3,10}\W\s\w{3,10}\W' 

            f = open("accnt_info.txt", 'r')
            info = f.read()
            khan = re.findall(pattern, info)

            availability = user_data in khan
            if availability == True:
                print("login succesful!!!")
            else:
                print("sorry we don't have account on these info!")

            
                        
            
    if user_status == 'signup':

        name = input("enter your username for signup purpose: ")
        password = getpass.getpass("set your password: ")
        f = open("accnt_info.txt", 'a')
        f.write('\n(' + name + ': ')
        f.write(password + ')\n')
        print("thank you!!")
        sign = False

        
account()


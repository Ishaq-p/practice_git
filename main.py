import numpy as np
import re
import pandas as pd
from getpass import getpass
from Database import DataBase as DB
# import mysql.connector

# data_base = mysql.connector.connect(host="localhost", user="root", password="", database="User_info")
# cursor = data_base.cursor()

import SignUp as SU
import login as LI


# getting and then searching for the user data existance
def get_and_check_usr_data():
    username = input("please enter your username: ").strip()
    password = getpass("please enter your password: ")
    user = LI.Login(username,password)
    return user.search_for_existence()

# getting user's overall data to confirm for giving him/her the permission to choose a new password
def get_and_check_usr_data_for_password_change():
    username = input("please enter your username: ").strip()
    password = getpass("please enter your password: ")
    user = LI.Login(username,password)
    return user.forgot_password()
     

# initial point of the program
user = input("do you have an account? (y/n): ").strip()

# if user has an account LOG IN
if user == "y":
    bol, msg = get_and_check_usr_data()

    # if the username is not found or the password is incorrect
    if (bol, msg) in [(False,"the username is not found"), (False, "the password is incorrect")]:
        tries = 3
        print("username and password don't match\n")
        while True:
            after_wrong_input = input("('0' for try again)\n('1' for forget password)\n('2' for exit)\n")
            if after_wrong_input in ["0","1","2"]:
                break
            print("invalid input, try again!\n")

        # while user want to try again
        while after_wrong_input=='0' and tries>0:
            tries-=1
            bol, msg = get_and_check_usr_data()
            if (bol, msg) in [(False,"the username is not found"), (False, "the password is incorrect")]:
                print("username and password don't match\n")
            elif (bol, msg) == (True, "the password is correct"):
                print("you are logged in")
                break
            if tries==0:
                print("you have no more tries")
                break
            after_wrong_input = input("('0' for try again)\n('1' for forget password)\n('2' for exit)\n")
            
        # UNDER CONSTRUCTION...
        while after_wrong_input=='1':
            bol, msg = get_and_check_usr_data_for_password_change()
            print(bol, msg)
            if bol:
                break

        while after_wrong_input=='2':
            print("have a nice day!")
            break


    elif (bol, msg) == (True, "the password is correct"):
        print("you are logged in")



        

#     elif not bol:
#         print(msg)
#         ask_ = input("would you like to change your password? (y/n): ").strip()

#         if ask_ == "y":
#             bol1, msg1 = user.user_verification_for_password_change()

#             if bol1:
#                 new_password = getpass("please enter your new password(1): ")
#                 bol2, msg2 = user.password_context_validity(new_password)

#                 while bol2==False:
#                     print(msg2)
#                     new_password = getpass("please enter your new password(2): ")
#                     bol2, msg2 = user.password_context_validity(new_password)

#                 while new_password != input("please re-enter your new password(3): "):
#                     print("the passwords do not match")
#                     new_password = getpass("please enter your new password(5): ")
#                     while not user.password_context_validity(new_password)[0]:
#                         new_password = getpass("please enter your new password(6): ")
                    
#                 user.password = new_password
#                 user.database()
#                 print(user)

#             else:
#                 print(msg)

#         else:
#             print("good bye")

#     else:
#         print("\n",msg,"\n")
#         print(user)





# if user == "n":
#     Full_Name = input("please enter your Full Name: ").strip()
#     email = input("please enter your email: ").strip()
#     username = input("please enter your username: ").strip()
#     password = getpass("please enter your password: ")
#     getting_updates = input("would you like get notified with updates via email (0,1): ").strip()
    
#     user = SU.SignUp(Full_Name,email,username,password,getting_updates)
#     user.database()
#     print(user)
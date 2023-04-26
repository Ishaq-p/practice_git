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

user = input("do you have an account? (y/n): ").strip()

if user == "y":
    username = input("please enter your username: ").strip()
    password = getpass("please enter your password: ")

    user = LI.Login(username,password)
    bol, msg = user.search_for_existence()

    if (bol, msg) == (False,"the username is not found"):
        print("username is not found")
        

    elif not bol:
        print(msg)
        ask_ = input("would you like to change your password? (y/n): ").strip()

        if ask_ == "y":
            bol1, msg1 = user.user_verification_for_password_change()

            if bol1:
                new_password = getpass("please enter your new password(1): ")
                bol2, msg2 = user.password_context_validity(new_password)

                while bol2==False:
                    print(msg2)
                    new_password = getpass("please enter your new password(2): ")
                    bol2, msg2 = user.password_context_validity(new_password)

                while new_password != input("please re-enter your new password(3): "):
                    print("the passwords do not match")
                    new_password = getpass("please enter your new password(5): ")
                    while not user.password_context_validity(new_password)[0]:
                        new_password = getpass("please enter your new password(6): ")
                    
                user.password = new_password
                user.database()
                print(user)

            else:
                print(msg)

        else:
            print("good bye")

    else:
        print("\n",msg,"\n")
        print(user)





elif user == "n":
        Full_Name = input("please enter your Full Name: ").strip()
        email = input("please enter your email: ").strip()
        username = input("please enter your username: ").strip()
        password = getpass("please enter your password: ")
        getting_updates = input("would you like get notified with updates via email (0,1): ").strip()


        user = SU.SignUp(Full_Name,email,username,password,getting_updates)
        user.database()
        print(user)
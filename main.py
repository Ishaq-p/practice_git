import numpy as np
import re
import pandas as pd
from getpass import getpass
# import mysql.connector

# data_base = mysql.connector.connect(host="localhost", user="root", password="", database="User_info")
# cursor = data_base.cursor()

import SignUp as SU
import login as LI

user = input("do you have an account? (y/n): ").strip()
if user == "y":
    user = LI.Login("","")
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
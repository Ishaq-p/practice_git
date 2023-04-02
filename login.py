import numpy as np
import re
import pandas as pd
from getpass import getpass
import mysql.connector
# import SignUp as SU

data_base = mysql.connector.connect(host="localhost", user="root", password="Khanzaman #1231", database="User_info")
cursor = data_base.cursor()

class Login:

    def __init__(self,username,password):
        self.username = username
        self.password = password

        # self.username = input("please enter your username: ").strip() # strip for removing spaces
        # self.password = getpass("please enter your password: ")


    def search_for_existence(self):
        cursor.execute(f"SELECT * FROM User_info.User_infSQ WHERE user_name = '{self.username}';")
        lis = cursor.fetchall()
        if lis == []:
            return False, "the username is not found"
        else:
            lis = lis[0]
            self.Full_Name = lis[1]
            self.email = lis[2]
            self.getting_updates = lis[4]
            self.created_at = lis[5]

            if self.password == lis[3]:
                return True, "the password is correct"
            else:
                return False, "the password is incorrect"
    
    
    def user_verification_for_password_change(self):
        pass
    
    def forgot_password(self):
        pass


    def decryption(self):
        pass

    def __str__(self):
        return f"username: {self.username}, \npassword: {self.password}, \nFull Name: {self.Full_Name}, \nemail: {self.email}, \nupdate_status: {self.getting_updates}, \naccount created at: {self.created_at}"



# TEST

data = [['ishaqpaktin' , 'Khanman-_22'],
        ['yunuskhan'   , 'yunusdF_33' ],
        ['yousufpaktin', 'yousufdF.33'],
        ['aimalamiri'  , 'aimalDF_33' ],
        ['johnwhick'   , 'jhonDF--33' ]]

for i in data:
    user = Login(*i)
    print(user.search_for_existence())
    print(user,"\n")
    del(user)
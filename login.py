import numpy as np
import re
import pandas as pd
from getpass import getpass
import mysql.connector
import SignUp as SU
import Database as DB

# data_base = mysql.connector.connect(host="localhost", user="root", password="Khanzaman #1231", database="User_info")
# cursor = data_base.cursor()

class Login(SU.SignUp, DB.DataBase):

    def __init__(self,username,password):
        DB.DataBase.__init__(self, username,password)
        self.username = username
        self.password = password

        self.lis = DB.DataBase.select(self)
        if self.lis == []:
            return False, "the username is not found"
        else:
            self.lis = self.lis[0]
            self.Full_Name = self.lis[1]
            self.email = self.lis[2]
            self.getting_updates = self.lis[4]
            self.created_at = self.lis[5]

            SU.SignUp.__init__(self, self.username,self.Full_Name,self.email,self.password, getting_updates="0")

        # self.username = input("please enter your username: ").strip() # strip for removing spaces
        # self.password = getpass("please enter your password: ")


    def search_for_existence(self):
        # lis = DB.DataBase.select(self)
        if self.lis == []:
            return False, "the username is not found"
        else:
            if self.password == self.lis[3]:
                return True, "the password is correct"
            else:
                return False, "the password is incorrect"
    
    
    def user_verification_for_password_change(self, state='forgot_password'):
        full_name = input("please enter your Full Name: ").strip()
        email = input("please enter your email: ").strip()

        if state=='forgot_password':
            if full_name == self.Full_Name and email == self.email:
                return True, "the Full Name and email are correct"
            else:
                return False, "the Full Name and email are incorrect"
            
        elif state=='delete_account':
            password = getpass("please enter your password: ")
            if full_name == self.Full_Name and email == self.email and password == self.password:
                return True, "the Full Name and email and password are correct"
            else:
                return False, "the Full Name and email and password are incorrect"
    

    def forgot_password(self):
        if self.user_verification_for_password_change('forgot_password')[0]:
            state, message = SU.SignUp.password_context_validity(self, status=False)
            while not state:
                print(message)
                state, message = SU.SignUp.password_context_validity(self, status=False)
                if state:
                    return state, message
            return state, message
        else:
            return False, "the Full Name and email are incorrect"
        

    def delete_account(self):
        if self.user_verification_for_password_change('delete_account')[0]:
            DB.DataBase.delete(self)
            return True, "the account has been deleted"
        else:
            return False, "the Full Name and email are incorrect"


    # def decryption(self):
    #     pass

    def __str__(self):
        return f"username: {self.username}, \npassword: {self.password}, \nFull Name: {self.Full_Name}, \nemail: {self.email}, \nupdate_status: {self.getting_updates}, \naccount created at: {self.created_at}"



# TEST

# data = [['ishaqpaktin' , 'Khanman-_22'],
#         ['yunuskhan'   , 'yunusdF_33' ],
#         ['yousufpaktin', 'yousufdF.33'],
#         ['aimalamiri'  , 'aimalDF_33' ],
#         ['johnwhick'   , 'jhonDF--33' ]]

# # for i in data:
# user = Login(*data[0])
# print(user.forgot_password())
# print(user,"\n")
# del(user)
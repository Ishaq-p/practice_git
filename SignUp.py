import numpy as np
import re
import pandas as pd
from getpass import getpass
import mysql.connector
import string
import Database as DB

# data_base = mysql.connector.connect(host="localhost", user="root", password="", database="User_info")
# cursor = data_base.cursor()



class SignUp(DB.DataBase):

    def __init__(self,username,Full_Name,email,password, getting_updates="0"):
        super().__init__(username,password)

        self.username = username
        self.password = password
        self.Full_Name = Full_Name
        self.email = email
        self.getting_updates = getting_updates

        # self.Full_Name = input("please enter your Full Name: ").strip()
        # self.email = input("please enter your email: ").strip()
        # self.username = input("please enter your username: ").strip()
        # self.password = getpass("please enter your password: ")

        # while self.getting_updates != "0" and self.getting_updates != "1":
        #     self.getting_updates = input("would you like get notified with updates via email (0,1): ").strip()


    def database(self):
        DB.DataBase.insert(self, self.Full_Name, self.email, self.getting_updates)
        return True, "the user is added to the database"


    def __str__(self):
        return f"{self.username}, {self.password}, {self.Full_Name}, {self.email}, {self.getting_updates}"


    def username_context_validity(self):
        if " " in self.username:
            return False, "it's containing space(s)"
        
        name_peices = [*self.username]
        for i in name_peices:
            if i not in string.ascii_letters:
                return False, f"the username contains somthing else other than ENG alphabets: {i}"
                
        return True, "the user name is made of plain Alphabets"
    

    def email_context_validity(self):
        valid_chars = string.ascii_letters+"-_."+string.digits       
        if "@" not in self.email:
            return False, "'@' is missing"
        
        usrnam, domain = self.email.split("@")
        for i in usrnam:
            if i not in valid_chars:
                return False, f"your email must not contain '{i}'"
            
        if "." not in domain:
            return False, "the domain is not in valid format"
    
        provider = domain.split(".")[0]
        return (True, provider, usrnam, domain)
    

    def password_context_validity(self, status=True):
        valid_chars = string.ascii_letters+"-_."+string.digits 

        if status:
            if len(self.password) < 8:
                return False, "the passcode must be at least 8 characters long."
            elif len(self.password) >= 16:
                return False, "the passcode must not be more than 16 characters long."
            
            if ' ' in self.password:
                return False, "the passcode must not contain spaces."
            
            for i in self.password:
                if i not in valid_chars:
                    return False, f"the passcode must only contain alphabets, digits, and (- _ .), {i}"
                
            return True, "valid passcode."
        
        else:
            passcode0 = getpass("please enter your new password: ")
            if passcode0 == self.password:
                return False, "the new password is same as the old one."
            
            if len(passcode0) < 8:
                return False, "the passcode must be at least 8 characters long."
            elif len(passcode0) >= 16:
                return False, "the passcode must not be more than 16 characters long."
            
            if ' ' in passcode0:
                return False, "the passcode must not contain spaces."
            
            for i in passcode0:
                if i not in valid_chars:
                    return False, f"the passcode must only contain alphabets, digits, and (- _ .), {i}"

            passcode1 = getpass("please re-enter your new password: ")
            if passcode0 == passcode1:
                self.password = passcode0
                DB.DataBase.update(self, self.password)
                return True, "the password has been changed"
            else:
                return False, "the passwords do not match" 


    def email_uniqueness(self):
        lis = DB.DataBase.select(self)
        
        try:
            if len(lis):
                return False, f"the email exists, and it's with {lis[0][1]}"
        except Exception as e:
            return False, f"{e}"
        
        return True, f"your {self.email} email is unique."
    

    def username_uniqueness(self):
        lis = DB.DataBase.select(self)
        
        try:
            if len(lis)!=0:
                return False, f"the username exists, and it's with {lis[0][1]}"
        except Exception as e:
            return False, f"{e}"
        
        return True, f"the {self.username} username is unique."
    

    def password_encryption(self):
        pass
  

    # def __del__(self):
    #     cursor.close()
    #     data_base.close()
    #     print("database connection closed.")



#  TESTS

# signup = SignUp('peter'   , 'Peter'      , 'peter@icloud.com'      , 'PeTer-33'    , '1')
# print(signup.email_uniqueness())
# print(signup.username_uniqueness())
# if signup.email_uniqueness()[0] and signup.username_uniqueness()[0]:
#     print(signup.database())
#     print(signup.close())



# data = [['ishaqpaktin' , 'ishaq paktin yar', 'shaqiniar@gmail.com', 'Khanman-_22'   , '1'],
#         ['yunuskhan'   , 'yunus khan'      , 'yunus@xyz.com'      , 'yunusdF_33'    , '0'],
#         ['yousufpaktin', 'yousuf paktin'   , 'yousuf@icloud.com'  , 'yousufdF.33'   , '1'],
#         ['aimalamiri'  , 'aimal amiri'     , 'aimal@outlook.com'  , 'aimalDF_33'    , '0'],
#         ['johnwhick'   , 'john whick'      , 'jhon@khan.com'      , 'jhonDF--33'    , '1']]
# for i in data:
#     signup = SignUp(*i)
#     print(signup.username_context_validity())
#     print(signup.email_context_validity())
#     print(signup.password_context_validity())
#     print(signup.email_uniqueness())
#     print(signup.username_uniqueness())
#     if signup.username_context_validity()[0] and signup.email_context_validity()[0] and signup.password_context_validity()[0] and signup.email_uniqueness()[0] and signup.username_uniqueness()[0]:
#         signup.database()
#         print("saved to database, done!! \n")
#     else:
#         print("something went wrong, please correct the mistake showing above.")
#     del(signup)
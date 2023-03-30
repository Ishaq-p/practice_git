import numpy as np
import re
import pandas as pd
from getpass import getpass
import mysql.connector

data_base = mysql.connector.connect(host="localhost", user="root", password="Khanzaman #1231", database="User_info")
cursor = data_base.cursor()

class SignUp:

    def __init__(self,Full_Name,email,username,password, getting_updates="0"):
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

    def __str__(self):
        return f"{self.username}, {self.password}, {self.Full_Name}, {self.email}, {self.getting_updates}"

    def username_context_validity(self):
        pass
    def email_context_validity(self):
        pass
    def password_context_validity(self):
        pass
    def email_uniqueness(self):
        pass

    def database(self):

        INSERTION_query = ("INSERT INTO User_info.User_infSQ (user_name, password, Full_Name, email, getting_updates) VALUES (%s, %s, %s, %s, %s)")
        Values = (self.username, self.password, self.Full_Name, self.email, self.getting_updates)
        
        cursor.execute(INSERTION_query, Values)
        data_base.commit()


    def data_encryption(self):
        pass


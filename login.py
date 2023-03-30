import numpy as np
import re
import pandas as pd
from getpass import getpass
import mysql.connector

data_base = mysql.connector.connect(host="localhost", user="root", password="Khanzaman #1231", database="User_info")
cursor = data_base.cursor()

class Login:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.username = input("please enter your username: ").strip() # strip for removing spaces
        self.password = getpass("please enter your password: ")

    def __str__(self):
        return self.username
    
    def search_for_existence(self):
        pass

    def password_validity(self):
        pass

    def database(self):
        pass

    def decryption(self):
        pass


import numpy as np
import re
import pandas as pd
from getpass import getpass

class Login:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.username = input("please enter your username: ").strip() # strip for removing spaces
        self.password = getpass("please enter your password: ")

    def __str__(self):
        return self.username
    
    def search_for_exists(self):
        pass

    def password_valid(self):
        pass

    def database(self):
        pass

    def encryption(self):
        pass

    def decryption(self):
        pass

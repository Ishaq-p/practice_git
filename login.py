import numpy as np
import re
import pandas as pd

class Login:

    def __init__(self,username,password):
        self.username = username
        self.password = password

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
    
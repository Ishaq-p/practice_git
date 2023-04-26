import mysql.connector

data_base = mysql.connector.connect(host="localhost", user="root", password="Khanzaman #1231", database="User_info")
cursor = data_base.cursor()


class DataBase:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def insert(self, Full_Name, email, getting_updates):
        INSERTION_query = ("INSERT INTO User_info.User_infSQ (user_name, password_, Full_Name, email, getting_updates) VALUES (%s, %s, %s, %s, %s);")
        Values = (self.username, self.password, Full_Name, email, getting_updates)
        
        cursor.execute(INSERTION_query, Values)
        data_base.commit()

    def update(self, new_password):
        UPDATE_query = ("UPDATE User_info.User_infSQ SET password_ = %s WHERE user_name = %s")
        Values = (new_password, self.username)
        
        cursor.execute(UPDATE_query, Values)
        data_base.commit()
    
    def delete(self):
        DELETE_query = ("DELETE FROM User_info.User_infSQ WHERE user_name = %s")
        Values = (self.username,)
        
        cursor.execute(DELETE_query, Values)
        data_base.commit()
    
    def select(self):
        SELECT_query = ("SELECT * FROM User_info.User_infSQ WHERE user_name = %s")
        Values = (self.username,)
        
        cursor.execute(SELECT_query, Values)
        # data_base.commit()
        return cursor.fetchall()
    
    def close(self):
        cursor.close()
        data_base.close()
        return True, "the connection is closed"
    
    
    

    #  TESTS
# print(DataBase("johnwhick", "jhonDF--33").select())
# print(DataBase("johnwhick", "jhonDF--33").update("janoo__f3"))
# print(DataBase("johnwhick", "janoo__f3").delete())
# print(DataBase("johnwhick", "jhonDF--33").insert("john whick", "john@yahoo.com", "1"))

# cursor.close()
# data_base.close()
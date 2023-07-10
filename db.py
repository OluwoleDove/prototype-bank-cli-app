import mysql.connector
from db_details import db

############################# DATABASE CODE #######################
def create_db():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = db["user"],
        password = db["password"],
        database="bank_cli_db" #returns an error if DB does not exist
    )
    
    return mydb
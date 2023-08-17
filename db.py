import mysql.connector
from db_params import db_params

############################# DATABASE CODE #######################
def create_db():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = db_params["user"],
        password = db_params["password"],
        database="bank_cli_db" #returns an error if DB does not exist
    )
    
    return mydb
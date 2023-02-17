import mysql.connector

    ############################# DATABASE CODE #######################
def create_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="",
        password="",
        database="bank_cli_db" #returns an error if DB does not exist
    )
    
    return mydb
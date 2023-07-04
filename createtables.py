from db import create_db 

new_db = create_db.cursor()

    #CREATE TABLE
    #Table user
    #Table account
    #Table transactions
new_db.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL, occupation VARCHAR(50) NOT NULL, gender VARCHAR (10), city VARCHAR(50), joindate DATETIME PRIMARY KEY (id))")
new_db.execute("CREATE TABLE account (user_id INT(11) NOT NULL AUTO_INCREMENT, balance, city, accountType, transaction_type, transactionDate VARCHAR(50) PRIMARY KEY (user_id))")

create_db.commit()

new_db.execute("SHOW TABLES")
######################################################################
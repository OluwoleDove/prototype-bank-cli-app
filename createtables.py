from db import create_db 

new_db = create_db.cursor()

#CREATE TABLES users  |  accounts  |  Table transactions
new_db.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL, occupation VARCHAR(50) NOT NULL, gender VARCHAR (10), city VARCHAR(50), join_date DATETIME PRIMARY KEY (id))")
new_db.execute("CREATE TABLE accounts (id INT(11) NOT NULL AUTO_INCREMENT, user_id INT(11) NOT NULL, accountType ENUM('Savings', 'Current'), balance FLOAT(20), pin INT(4), last_edited DATETIME PRIMARY KEY (user_id))")
new_db.execute("CREATE TABLE transactions (id INT(11) NOT NULL AUTO_INCREMENT, user_id INT(11) NOT NULL, transaction_type ENUM('Deposit', 'Withdrawal', 'Transfer', 'Pin_Change'), transaction_amount FLOAT(20), transaction_date DATETIME PRIMARY KEY (user_id))")
create_db.commit()

new_db.execute("SHOW TABLES")
######################################################################
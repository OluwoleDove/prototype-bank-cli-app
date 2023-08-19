from db import create_db 

new_db = create_db.cursor()

#CREATE TABLES users  |  accounts  |  Table transactions
new_db.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT, firstname VARCHAR(50) NOT NULL, lastname VARCHAR(50) NOT NULL, email VARCHAR(50), phone VARCHAR(20), gender VARCHAR (10), dob DATETIME, occupation VARCHAR(50), city VARCHAR(50), join_date DATETIME PRIMARY KEY (id))")
new_db.execute("CREATE TABLE accounts (id INT(11) NOT NULL AUTO_INCREMENT, user_id INT(11) NOT NULL, account_type ENUM('Savings', 'Current', 'Fixed') DEFAULT 'Savings', balance FLOAT(10,2), charges FLOAT(10,2), interests FLOAT(10,2), pin INT(4), last_edited DATETIME PRIMARY KEY (user_id))")
new_db.execute("CREATE TABLE transactions (id INT(11) NOT NULL AUTO_INCREMENT, user_id INT(11) NOT NULL, transaction_type ENUM('Create_Account', 'Deposit', 'Withdrawal', 'Transfer', 'Pin_Change', 'Close_Account') DEFAULT 'Create_Account', transaction_amount FLOAT(10,2), transaction_date DATETIME PRIMARY KEY (user_id))")
create_db.commit()

new_db.execute("SHOW TABLES")
######################################################################
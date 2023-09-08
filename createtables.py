from db import mydb, new_db

#Create the 'users' table
new_db.execute("CREATE TABLE users ("
               "id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY",
               "firstname VARCHAR(50) NOT NULL",
               "lastname VARCHAR(50) NOT NULL",
               "email VARCHAR(50) NOT NULL",
               "phone VARCHAR(20) NOT NULL",
               "gender ENUM('Male', 'Female', 'Prefer not to say') DEFAULT 'Prefer not to say'",
               "dob DATETIME",
               "occupation VARCHAR(50)",
               "city VARCHAR(50)",
               "join_date DATETIME"
               "deactivatevalidity DATETIME",
               ")")

#Create the 'accounts' table
new_db.execute("CREATE TABLE accounts ("
               "id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY",
               "user_id INT(11) NOT NULL",
               "account_type ENUM('Savings', 'Current', 'Fixed') DEFAULT 'Savings'",
               "balance FLOAT(10,2)",
               "charge FLOAT(10,2)",
               "interest FLOAT(10,2)",
               "pin INT(4)",
               "last_edited DATETIME"
               ")")

#Create the 'transactions' table
new_db.execute("CREATE TABLE transactions ("
               "id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY",
               "user_id INT(11) NOT NULL",
               "transaction_type ENUM('Create_Account', 'Deposit', 'Withdrawal', 'Transfer', 'Pin_Change', 'Close_Account') DEFAULT 'Create_Account'",
               "transaction_amount FLOAT(10,2)",
               "transaction_date DATETIME"
               ")")

mydb.commit()

print(f"{new_db} Tables created successfully.")
######################################################################
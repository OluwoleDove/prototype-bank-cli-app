# prototype-bank-cli-app

This python applications mimics our regular everyday bank transactions
It contains a main Account class other other class types that inherits the Account class
It saves the application's data in a MySql database
Some activities that are possible includes
 - Account creation
 - Withdrawal
 - Deposit
 - PIN creation and change
 - Funds Transfer

The database tables are 'user', 'account', and 'transactions' table.

pip install the following modules python modules
- mysql.connector
Remember to install MySql database and its python connector if you haven'at already done that.

Find this block of code in the program file and fill them with your MySQL database parameters

mydb = mysql.connector.connect(
  host="localhost",
  user="{Your Database username}",
  password="{Your Database Password}",
  database="{Your Model's Name}" #returns an error if DB does not exist
)
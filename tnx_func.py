from bankclass import Account, Savings, Current
from db import create_db
import datetime


this_db = create_db().cursor()

def check_db(my_model):
    email = str(input("Type your email: "))
    sql = "SELECT * FROM accounts where user_id = %s"
    val = ([email])
    my_model.execute(sql, val)
    this_query = my_model.fetchone()

    return this_query

def process_transactions(arg_dict, account_type, tnx_type):
    if account_type == "Savings":
        this_client = Savings()
    elif account_type == "Current":
        this_client = Current()
        
    db_instance = create_db.cursor()

    if tnx_type == 'create_account':
        sql = "INSERT INTO users (firstname, lastname occupation, gender, joindate) VALUES (%s, %s, %s, %s, %s)"
        val = (arg_dict['firstname'], arg_dict['lastname'], arg_dict['occupation'], arg_dict['gender'], datetime.now())
        db_instance.execute(sql, val)
        return f"{db_instance.rowcount}, records inserted."

    elif tnx_type == 'change_pin':
        pass

    elif tnx_type == 'check_balance':
        pass

    elif tnx_type == 'deposit':
        sql = "SELECT id, email FROM users"
        db_instance.execute(sql)
        my_query = db_instance.fetchone()
        print(my_query)
        this_customer = Savings()
        depositamount = str(input("Enter the deposit amount: "))
        my_deposit = this_customer.deposit(float(depositamount))
        print(my_deposit)
        sql = "UPDATE transactions SET balance = %s WHERE email = %s"
        val = (my_deposit, email)
        db_instance.execute(sql, val)
        create_db.commit()
        print(db_instance.rowcount, "records affected.")

    elif tnx_type == 'withdrawal':
        
        my_query = check_db(this_db)
        balance = my_query[-1]
        email = my_query[7]
        print(f"This client's record is - {my_query}\nThe balance is {balance}")

        this_client = Savings(my_query[1], my_query[3], my_query[5], "Doctor", my_query[4], my_query[2], my_query[7], my_query[6])
        depositamount = input("Enter the deposit amount: ")

        amount = input("Enter the withdrawal amount: ")
        try:
            amount = float(input("Enter the withdrawal amount: "))
            if amount > balance:
                 # raise the ValueError
                raise ValueError("Insufficient Funds")
            else:
                this_withdrawal = this_client.withdraw(balance, amount)
                print(this_withdrawal)
                sql = "UPDATE Bank_Account SET balance = %s WHERE email = %s"
                val = (this_withdrawal, email)
                this_db.execute(sql, val)
                db_instance.commit()
                print(this_db.rowcount, "records affected.")
            # if false then raise the value error
        except ValueError as e:
            print(e)
            print("Please supply a floating value for the amount")

    elif tnx_type == 'funds_transfer':
        pass

    elif tnx_type == 'close_account':
        pass

    else:
        return "Invalid Transaction"
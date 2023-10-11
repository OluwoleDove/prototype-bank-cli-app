from bankclass import Account, Savings, Current
from db import mydb
import datetime
import random

def find_client(my_model):
    pin = input("Your pin number please: ")
    sql = "SELECT * FROM accounts where pin = %s"
    val = ([pin])
    my_model.execute(sql, val)
    this_query = my_model.fetchone()

    return this_query

def gen_account(this_len):
    acc_num = ''
    chars = '0123456789'
    for _ in range(this_len):
        acc_num += random.choice(chars)
   
    return acc_num


def process_transactions(arg_dict, account_type, tnx_type): 
    db_instance = mydb.cursor()

    if tnx_type == 'create_account':
        pin = 1000
        acc_type = input("\nSelect your account type: \n1. Savings Account\n2. Current Account\n\n")
        if acc_type == "1":
            this_client = Savings(arg_dict['firstname'], arg_dict['lastname'], arg_dict['email'], arg_dict['phone'],  arg_dict['gender'], arg_dict['dob'], arg_dict['occupation'], arg_dict['city'])
        elif acc_type == "2":
            this_client = Current(arg_dict['firstname'], arg_dict['lastname'], arg_dict['email'], arg_dict['phone'],  arg_dict['gender'], arg_dict['dob'], arg_dict['occupation'], arg_dict['city'])

        new_account = gen_account(10)
        #Create Client's Bio
        sql = "INSERT INTO users (firstname, lastname, email, phone, gender, dob, occupation, city, join_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (arg_dict['firstname'], arg_dict['lastname'], arg_dict['email'], arg_dict['phone'], arg_dict['gender'], arg_dict['dob'], arg_dict['occupation'], arg_dict['city'], datetime.now())
        db_instance.execute(sql, val)

        #Get client's id from user records
        sql = "SELECT id FROM users where email = %s"
        val = (arg_dict['email'])
        db_instance.execute(sql, val)
        userID = db_instance.fetchone()
        #Create Client's Account
        sql = "INSERT INTO accounts (user_id, account_type, balance, charge, interest, pin, last_edited) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (userID, account_type, arg_dict['balance'], 0, 0, datetime.now())
        db_instance.execute(sql, val)
        mydb.commit()
        return f"{db_instance.rowcount}, client created."

    elif tnx_type == 'change_pin':
        try:
            prev_pin = int(input("Enter your previous pin "))
            if isinstance(prev_pin, int) == False:
                 # raise the ValueError
                raise ValueError("Only Numbers Please")
            else:
                sql = "SELECT * FROM accounts where pin = %s"
                val = (arg_dict['email'])
                db_instance.execute(sql, val)
                mydb.commit()
                print(db_instance.rowcount, "records affected.")
            # if false then raise the value error
        except ValueError as e:
            print(e)
            print("Please supply a four digit integer")

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
        mydb.commit()
        print(db_instance.rowcount, "records affected.")

    elif tnx_type == 'withdrawal':
        
        my_query = find_client(db_instance)
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
                db_instance.execute(sql, val)
                mydb.commit()
                print(db_instance.rowcount, "records affected.")
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
import sys
from bankclass import Account, Savings, Current
from db import create_db
import datetime

def process_transactions(arg_dict, tnx_type):
    db_instance = create_db.cursor()

    if tnx_type == 'create_account':
        sql = "INSERT INTO users (firstname, lastname occupation, gender, joindate) VALUES (%s, %s, %s, %s)"
        val = (arg_dict['firstname'], arg_dict['lastname'], arg_dict['occupation'], arg_dict['gender'], datetime.now())
        db_instance.execute(sql, val)
        return f"{db_instance.rowcount}, records inserted."

    elif tnx_type == 'change_pin':
        pass

    elif tnx_type == 'withdraw':
        pass

    elif tnx_type == 'deposit':
        sql = "SELECT id, email FROM users"
        db_instance.execute(sql)
        my_query = db_instance.fetchone()
        print(my_query)
        depositamount = str(input("Enter the deposit amount: "))
        my_deposit = new_client.deposit(float(depositamount))
        print(my_deposit)
        sql = "UPDATE transactions SET balance = %s WHERE email = %s"
        val = (my_deposit, email)
        db_instance.execute(sql, val)
        create_db.commit()
        print(db_instance.rowcount, "records affected.")

    elif tnx_type == 'funds_transfer':
        pass

    else:
        return "Invalid Transaction"

def get_input():
    for user_input in sys.stdin:
        if 'q' == user_input.rstrip():
            break
        return user_input
        #print(f'Input : {line}')

def input_prompt():
    user_dict = {"firstname":"", "lastname":"", "occupation":"", "gender":"", "city":""}
    print("Getting user input ... Please carefully supply the following")
    for key in user_dict:
        print(f"{key}: ")
        user_dict.update({ key : get_input() })

    print(user_dict)
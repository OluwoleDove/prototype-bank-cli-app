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
        this_customer = Savings()
        depositamount = str(input("Enter the deposit amount: "))
        my_deposit = this_customer.deposit(float(depositamount))
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


def check_db(model):
    email = str(input("Email: "))
    sql = "SELECT * FROM Bank_Account where email = %s"
    val = ([email])
    model.execute(sql, val)
    new_query = model.fetchone()

    return new_query

    my_query = check_db(new_db)
    bal = my_query[-1]
    email = my_query[7]
    print(f"This client's record is - {my_query}\nThe balance is {bal}")

    my_client = Savings_account(my_query[1], my_query[3], my_query[5], "Doctor", my_query[4], my_query[2], my_query[7], my_query[6])
    depositamount = input("Enter the deposit amount: ")
    my_deposit = my_client.deposit(bal, depositamount)
    print(my_deposit)
    sql = "UPDATE Bank_Account SET balance = %s WHERE email = %s"
    val = (my_deposit, email)
    new_db.execute(sql, val)
    mydb.commit()
    print(new_db.rowcount, "records affected.")

    my_query = check_db(new_db)
    bal = my_query[-1]
    email = my_query[7]
    print(f"This client's record is - {my_query}\nThe balance is {bal}")
    
    withdrawamount = input("Enter the withdrawal amount: ")
    my_withdrawal = my_client.withdrawal(bal, withdrawamount)
    print(my_withdrawal)
    sql = "UPDATE Bank_Account SET balance = %s WHERE email = %s"
    val = (my_withdrawal, email)
    new_db.execute(sql, val)
    mydb.commit()
    print(new_db.rowcount, "records affected.")
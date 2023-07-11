import sys
from db import create_db
import datetime


def process_transactions(arg_dict, tnx_type):
    if tnx_type == 'create_account':
        sql = "INSERT INTO users (name, occupation, gender, joindate) VALUES (%s, %s, %s, %s)"
        val = (firstname, lastname, occupation, gender, datetime.now())
        new_db.execute(sql, val)

        return f"{new_db.rowcount}, records inserted."

    elif tnx_type == 'change_pin':
        pass

    elif tnx_type == 'withdraw':
        pass

    elif tnx_type == 'deposit':
        pass

    elif tnx_type == 'funds_transfer':
        pass

    else:
        return "Invalid Transaction"

def receive_input():
    for user_input in sys.stdin:
        if 'q' == user_input.rstrip():
            break
        return user_input
        #print(f'Input : {line}')


user_dict = {"firstname":"", "lastname":"", "occupation":"", "gender":"", "city":""}
print("Getting user input ... Please carefully supply the following")
for key in user_dict:
    print(f"{key}: ")
    user_dict.update({ key : receive_input() })

print(user_dict)

'''
process_transactions(user_dict, 'create_account')

print(create_db)
new_db = create_db.cursor()
'''
import sys
from db import create_db
import datetime

def receive_input():
    for user_input in sys.stdin:
        if 'q' == user_input.rstrip():
            break
        return user_input
        #print(f'Input : {line}')

firstname = receive_input()
lastname = receive_input()
occupation = receive_input()
gender = receive_input()
city = receive_input()

user_dict = {"firstname":"", "lastname":"", "occupation":"", "gender":"", "city":""}
print("Getting user input ... Please carefully suppy the following")
for i in range(len(user_dict)):
    new_input = (user_dict.keys())[i]
    print(f"{new_input}: ", new_input)
    user_dict.update({ (user_dict.keys())[i]: new_input.strip('\"') })

print(create_db)
new_db = create_db.cursor()

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

def funds_transfer():
    pass
import sys
from db import create_db
import datetime

def receive_input():
    for user_input in sys.stdin:
        if 'q' == user_input.rstrip():
            break
        return user_input
        #print(f'Input : {line}')

name = receive_input()
occupation = receive_input()
gender = receive_input()

#WRITE TO MYSQL DATABASE

print(create_db)
new_db = create_db.cursor()

sql = "INSERT INTO users (name, occupation, gender, joindate) VALUES (%s, %s, %s, %s)"
val = (name, occupation, gender, datetime.now())

new_db.execute(sql, val)

print(new_db.rowcount, "records inserted.")

def create_account():
    pass

def change_pin():
    pass

def withdraw():
    pass

def deposit():
    pass

def funds_transfer():
    pass
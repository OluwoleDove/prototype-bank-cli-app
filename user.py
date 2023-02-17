import sys
from db import create_db 

def receive_input():
    for user_input in sys.stdin:
        if 'q' == user_input.rstrip():
            break
        return user_input
        #print(f'Input : {line}')

name = receive_input()
account_type = receive_input()
tnx_type = receive_input()

#WRITE TO MYSQL DATABASE

print(create_db)
new_db = create_db.cursor()

    #CREATE TABLE
    #Table user
    #Table account
    #Table transactions
new_db.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT, name, gender, joindate VARCHAR(50), PRIMARY KEY (id))")

sql = "INSERT INTO users (name, gender, joindate) VALUES (%s, %s, %s)"
val = (name, account_type, tnx_type)

new_db.execute(sql, val)

create_db.commit()

print(new_db.rowcount, "records inserted.")
new_db.execute("SHOW TABLES")
######################################################################
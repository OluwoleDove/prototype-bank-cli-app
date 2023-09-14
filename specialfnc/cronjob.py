import csv
from datetime import datetime, timedelta
from db import mydb

# Define the CSV filename
csv_filename = "user_data.csv"

new_db = mydb.cursor()
# Get the current datetime
current_datetime = datetime.now()

# Calculate the datetime threshold (2 weeks ago)
threshold_datetime = current_datetime - timedelta(weeks=2)

# Query to retrieve and delete user data
query = """
    SELECT `id`, `firstname`, `lastname`, `email`, `phone`, `gender`, `dob`, `occupation`, `city`, `join_date`, `deactivatevalidity`,
           `accounts`.`id` AS `account_id`, `account_type`, `balance`, `charge`, `interest`, `pin`, `last_edited`,
           `transactions`.`id` AS `transaction_id`, `transaction_type`, `transaction_amount`, `transaction_date`
    FROM `users`
    LEFT JOIN `accounts` ON `users`.`id` = `accounts`.`user_id`
    LEFT JOIN `transactions` ON `users`.`id` = `transactions`.`user_id`
    WHERE `deactivatevalidity` <= %s;
"""

# Execute the query with the threshold datetime
new_db.execute(query, (threshold_datetime,))
results = new_db.fetchall()

if results:
    # Write the data to a CSV file
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ["id", "firstname", "lastname", "email", "phone", "gender", "dob", "occupation", "city", "join_date", "deactivatevalidity",
                      "account_id", "account_type", "balance", "charge", "interest", "pin", "last_edited",
                      "transaction_id", "transaction_type", "transaction_amount", "transaction_date"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in results:
            # Convert DATETIME objects to strings for CSV
            row = [str(col) if isinstance(col, datetime) else col for col in row]
            writer.writerow(dict(zip(fieldnames, row)))

    # Commit changes and delete user data from tables
    new_db.commit()
    new_db.execute("DELETE FROM `users` WHERE `deactivatevalidity` <= %s;", (threshold_datetime,))
    mydb.commit()

    print("User data harvested and deleted successfully.")
else:
    print("No user data to harvest.")

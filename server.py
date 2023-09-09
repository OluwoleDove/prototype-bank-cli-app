import schedule
import time
import subprocess

def run_cronjob():
    print("Running cron job...")
    subprocess.run(["C:/Python311/Python", "cronjob.py"])
    print("Cron job completed.")

# Schedule the cron job to run daily at midnight
schedule.every().day.at("00:00").do(run_cronjob)

# Run the scheduler continuously
while True:
    schedule.run_pending()
    time.sleep(1)

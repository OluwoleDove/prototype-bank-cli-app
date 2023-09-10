import time
import subprocess

def run_cronjob():
    print("Running cron job...")
    subprocess.run(["C:/Python311/Python", "cronjob.py"])
    print("Cron job completed.")

# Run the scheduler continuously
while True:
    # Get the current time
    current_time = time.localtime()

    # Check if it's midnight (00:00)
    if current_time.tm_hour == 0 and current_time.tm_min == 0:
        run_cronjob()
    
    # Sleep for a while to avoid continuous checking
    time.sleep(60)  # Sleep for 60 seconds (adjust as needed)

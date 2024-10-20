#After using this code one have to set it to show notification every two Hours using task Scheduler in windows
import time
import os
from plyer import notification

# File to store the username
username_file = r"C:\Users\ssanj\Github\GitHub\learning-python\python Practice question\username.txt"

# Check if the username file exists
if os.path.exists(username_file):
    # Read the username from the file
    with open(username_file, "r") as file:
        User = file.read().strip()
else:
    # Ask for the username and save it to the file
    User = input("What shall I call you? ")
    with open(username_file, "w") as file:
        file.write(User)

# Creating the message template
message_template = f"Don't you think you should drink some water, {User}?"

while True:  # Infinite loop for periodic notifications
    # Sending the notification
    notification.notify(
        title="Water Drink Reminder",
        message=message_template,
        timeout=2  # Notification timeout in seconds
    )

    # Waiting time (set to 2 hours)
    time.sleep(2*3600)  # Sleep for 2 hours

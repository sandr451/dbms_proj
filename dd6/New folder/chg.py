import os
import datetime

# Specify the path of the file whose modification time you want to change
file_path = "C:\\Users\\Sarthak\\Desktop\\New folder\\front.py"

# Define the desired modification time as a datetime object
new_time = datetime.datetime(2023, 3, 29, 23, 24, 51)

# Convert the datetime object to a Unix timestamp
timestamp = new_time.timestamp()

# Set the new modification time for the file
os.utime(file_path, (timestamp, timestamp))

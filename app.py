import os
import shutil
from datetime import datetime

# Set the root directory and the target date
root_folder = 'QuestSystem'  # Change this to your local root folder name
new_creation_date = datetime(2024, 5, 4)  # New creation date: 4th May 2024

# Convert the datetime object to a timestamp (seconds since the epoch)
new_creation_timestamp = new_creation_date.timestamp()

# Walk through all files and folders in the root folder and its subfolders
for dirpath, dirnames, filenames in os.walk(root_folder):
    # Change the creation time for the current directory
    os.utime(dirpath, (new_creation_timestamp, new_creation_timestamp))
    
    for filename in filenames:
        # Get the full path of the file
        file_path = os.path.join(dirpath, filename)

        # Change the creation, modification, and access times for the file
        os.utime(file_path, (new_creation_timestamp, new_creation_timestamp))

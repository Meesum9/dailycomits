import os
import datetime

# Define file path (could be any file in the repo)
file_path = "daily_commit.txt"

# Get the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write the current date to the file
with open(file_path, "a") as file:
    file.write(f"Commit made on: {current_date}\n")

# Stage the changes
os.system("git add .")

# Commit the changes
os.system(f'git commit -m "Daily commit: {current_date}"')

# Push the changes to GitHub
os.system("git push origin main")

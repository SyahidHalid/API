# pip install openpyxl --trusted-host pypi.org --trusted-host files.pythonhosted.org

import pandas as pd
import random
import string
from datetime import datetime
import openpyxl
import numpy as np

# ==========================================================================================
# Create excel
# ==========================================================================================


# current_time = pd.Timestamp.now()

# # function to generate random alphanumeric ID
# def generate_id(length=8):
#     chars = string.ascii_letters + string.digits
#     return ''.join(random.choice(chars) for _ in range(length))

# # number of rows
# n = 5

# # create base dataframe with timestamp
# df = pd.DataFrame({
#     "id": [generate_id() for _ in range(n)],
#     "timestamp": [datetime.now() for _ in range(n)]
# })

# # ✅ split into separate columns
# df["date"] = pd.to_datetime(df["timestamp"]).dt.date
# df["time"] = pd.to_datetime(df["timestamp"]).dt.time

# # optional: drop original timestamp column
# df = df.drop(columns=["timestamp"])

# df.to_excel("task_schedular.xlsx", index=False)


# ==========================================================================================
# Append excel
# ==========================================================================================

# # Example existing data
# data = [
#     [0, "wZklyQI9", "2026-07-01", "14:38:26.047863"],
#     [1, "Pmcbj8Ls", "2026-07-01", "14:38:26.047868"],
#     [2, "TfukvA7m", "2026-07-01", "14:38:26.047869"],
#     [3, "Tbp1JLJN", "2026-07-01", "14:38:26.047870"],
#     [4, "prtCCO6I", "2026-07-01", "14:38:26.047871"],
# ]

# df = pd.DataFrame(data, columns=["id", "code", "date", "time"])

# # ----- Generate new row -----
# new_id = df["id"].max() + 1

df = pd.read_excel("task_schedular.xlsx")

# random 8-char string (same style as your IDs)
new_code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

now = datetime.now()
new_date = now.strftime("%Y-%m-%d")
new_time = now.strftime("%H:%M:%S.%f")

new_row = {
    "id": new_code,
    "date": new_date,
    "time": new_time
}

# ----- Append -----
df1 = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

df1['date'] = pd.to_datetime(df1['date']).dt.date

df1['time'] = pd.to_datetime(df1['time']).dt.time


df1.to_excel("task_schedular.xlsx", index=False)

# print("Job run at:", datetime.now())


# ==========================================================================================
# Run Task Scheduler
# ==========================================================================================


# 1. Create the task

# Open Task Scheduler
# Click Create Task… (not “Basic Task”)


# 2. Configure Action (run Python)

# Go to Actions → New
# Program/script:
# C:\Path\to\python.exe

# Add arguments:
# C:\Path\to\your_script.py


#C:\Users\syahidhalid\Syahid_PC\Python 3.13.14\python.exe
#D:\00. Git Repository\API\task_schedular.py


# 3. Configure Trigger (this is the key ⚡)
# Go to Triggers → New:

# Begin the task: On a schedule
# Settings: Daily
# Start time: e.g. 9:00 AM (your starting point)

# Then click Advanced settings:

# ✅ Tick Repeat task every: → 30 minutes
# ✅ Set For a duration of:
# → calculate duration until 6 PM

# Example:

# Start: 9:00 AM
# End: 6:00 PM
# Duration = 9 hours

# So set:
# Repeat task every: 30 minutes
# For a duration of: 9 hours


# ==========================================================================================
# different Methods 
# ==========================================================================================


# ✅ Method 2: Command line (optional)
# You can do the same using schtasks:
# Shell
# schtasks /create ^ 
# /tn "RunPythonEvery30Min" ^ 
# /tr "C:\Python39\python.exe C:\scripts\your_script.py" ^ 
# /sc daily ^ 
# /st 09:00 ^ 
# /ri 30 ^ 
# /et 18:00S

# /ri 30 → every 30 minutes
# /et 18:00 → stop at 6 PM
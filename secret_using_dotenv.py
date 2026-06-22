#==================================================================
# Secret
#==================================================================


# location PPS GPM
# \\10.30.12.14\documents\knowledge center\e-PPG

# pip install python-dotenv --trusted-host pypi.org --trusted-host files.pythonhosted.org
# create .env file
# add to .gitignore

from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()
api_key = os.getenv("api_key")

print(f"{api_key}")

#all values
print(dotenv_values('.env'))

#==================================================================
# gitignore
#==================================================================

# 1. create
# cmd: touch .gitignore

# 2. put .env

# 3. cmd: git status 
# to check


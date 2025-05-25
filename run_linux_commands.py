import os
import subprocess

# # Getting files from current working directory
# present_wd = os.getcwd()
# file_list = os.listdir(present_wd)
# print(f"present working dir is: {present_wd}\n list of file are: {file_list}")




file_listt = subprocess.run(['uptime'], capture_output=True, text=True, check=True)
print(file_listt.stdout)
# print(file_list)
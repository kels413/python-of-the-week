import os

path = input("Please enter directory Path (absolute or relative) to view the output: ")

try:
    expand_path = os.path.expanduser(path)
    content = os.listdir(expand_path)
except FileNotFoundError:
    print("No such File or Directory")
    


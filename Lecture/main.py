import os
import sys

print(os.name)


#testing for os.getcwd
# cwd = os.getcwd()
# print(cwd)


# #testing for os.chdir()

# def check_directory():
#     print("path before changing the directory")
#     cwd = os.getcwd()


# check_directory()
# os.chdir('../')
# print(os.getcwd())

# path = "/Users/mistarkelly/ubunteu_shared/My-Projects/python-of-the-week/Lecture"

# try:
#     content = os.listdir(path)
#     print(content)
# except  FileNotFoundError:
#    print("No such file")
#     # pass
   

path = input("Enter directory to sort: ")

expand_path = os.path.expanduser(path)

print(os.listdir(expand_path))


"""
A Python script for efficient file management on my system. The script should be able to perform tasks such as organizing files, renaming, moving, and possibly categorizing them.
"""
import os
import shutil

class Organize:

    """
        A class that Manages the files in the specified Directory.
    """
    # __directories = ["Documents", "Downloads", "Pictures", "Videos", "Work", "Others"]

    def recieve_userInput(self):
        user_input = input("Please Enter The Directory you wish to arrange: ")
        self.expanded_path = os.path.expanduser(user_input)

        # check if file exists
        if not os.path.exists(self.expanded_path):
            raise FileNotFoundError("File or directory does not exist")

        # if valid directory and not a file:
            # change cwd to user_input.
    def change_directory(self):
        if os.path.isdir(self.expanded_path):
            # change current working to the path provided by the user
            os.chdir(self.expanded_path)
        else:
            print("provided path is not a directory")
       
    def create_directories(self):
        """ create Directories
            a method responsible for creating directories
        """
        content = os.listdir(self.expanded_path)
        print("changed directory",os.getcwd())

       
            
try:      
    organize1 = Organize()
    organize1.recieve_userInput()
    organize1.change_directory()
    organize1.create_directories()
except FileNotFoundError as fe:
    print(f"Error:", fe)
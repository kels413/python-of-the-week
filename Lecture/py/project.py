"""
A Python script for efficient file management on my system. The script should be able to perform tasks such as organizing files, renaming, moving, and possibly categorizing them.
"""
import os
import shutil
import magic

class Organize:

    """
        A class that Manages the files in the specified Directory.
    """
    # __directories = ["Documents", "Downloads", "Pictures", "Videos", "Work", "Others"]

    def recieve_userInput(self):
        user_input = input("Please Enter The Directory you wish to arrange: ")

        expanded_path = os.path.expanduser(user_input)

        # check if file exists
        if not os.path.exists(expanded_path):
            raise FileNotFoundError("Error: File or directory does not exist")
        
        # check if its a valid directory and not a file
        if os.path.isdir(expanded_path):
            content = os.listdir(expanded_path)
            # change current working the the path provided by the user
            os.chdir(expanded_path)
            print(content)
        else:
            print("Error: provided path is not a directory")

    def create_directories(self):
        """ create Directories
            a method responsible for creating directories
        """
        try:
            pass
        except FileExistsError:
            print("File aready created", self.__directories)

    def move_files(self):
        """Move files
            A Method responsible for moving files into directories
        """
        pass

            
try:      
    organize1 = Organize()
    organize1.recieve_userInput()
    organize1.create_directories()
except FileNotFoundError as fe:
    print(f"Erro:", fe)
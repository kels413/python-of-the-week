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

    def recieve_userInput(self) -> None:
        user_input = input("Please Enter The Directory you wish to arrange: ")
        self.expanded_path = os.path.expanduser(user_input)
        print(self.expanded_path)

        # check if file exists
        if not os.path.exists(self.expanded_path):
            raise FileNotFoundError("File or directory does not exist")

        # if valid directory and not a file:
        #     change cwd to user_input.
        
    def change_directory(self):
        print(os.getcwd())
        if os.path.isdir(self.expanded_path):
            # change current working to the path provided by the user
            os.chdir(self.expanded_path)
            print(os.getcwd())
            print("this is the path",self.expanded_path)

        else:
            print("provided path is not a directory")
       
    def create_directories(self):
        """ create Direct ories
            a method responsible for creating directories
        """
        content = os.listdir(self.expanded_path)
        print(content)
       
        print("changed directory",os.getcwd())
        print("this is where i am")

        try:
          for file in content:
             #expand the file_name
              print(file)
              print("Kelly")
              name, ext = os.path.splitext(file)
              print(name)
              print(os.getcwd())
    #           #remove dot(.) from the ext using slicing.
              excluded_dot = ext[1:]
              # if the tuple created from splitext is not empty:
                # eg name, ext = (file, txt) and not name, ext = (file, "") 
              if excluded_dot != "" and not os.path.isdir(excluded_dot) and not os.path.exists(excluded_dot):
                os.mkdir(excluded_dot)
                print("this is the excluded dot", excluded_dot)
                print("Name of the file", name)
                print("extension", ext)
        except FileExistsError:
            print("File aready created")


    # def move_files(self):
    #     """Move files
    #         A Method responsible for moving files into directories
    #     """
    #     pass

try:      
    organize1 = Organize()
    organize1.recieve_userInput()
    organize1.change_directory()
    organize1.create_directories()
    # organize1.move_files()
except FileNotFoundError as fe:
    print(f"Error:", fe)
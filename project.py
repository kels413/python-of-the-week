"""
A Python script for efficient file management on my system. The script should be able to perform tasks such as organizing files, renaming, moving, and possibly categorizing them. using OOP.
"""
import os
import shutil

class Organize:

    """
        A class that Manages the files in the specified Directory.
    """
    # __directories = ["Documents", "Downloads", "Pictures", "Videos", "Work", "Others"]

    def recieve_userInput(self) -> str:
        user_input = input("Please Enter The Directory you wish to arrange: ")
        cleaned_input = user_input.strip()

        expanded_path = os.path.expanduser(cleaned_input)
        print(os.getcwd())

        # check if file exists
        if not os.path.exists(expanded_path):
            raise FileNotFoundError("directory does not exist")
        # check wether path exists buh not a directory
        if os.path.exists(expanded_path) and not os.path.isdir(expanded_path):
            raise FileNotFoundError("Sorry path provided is a file not a directory")

        if user_input.startswith("~") or user_input.startswith("/"):
            os.chdir(expanded_path)
            return expanded_path

        os.chdir(expanded_path)
        return os.getcwd()

    def manage_dir(self, path):
        """ create Direct ories
            a method responsible for creating directories
        """
        content = os.listdir(path)
        print(content)
       
        print("changed directory",os.getcwd())
        print("this is where i am")

        try:
          for file in content:
             #expand the file_name
              name, ext = os.path.splitext(file)
    #           #remove dot(.) from the ext using slicing.
              excluded_dot = ext[1:]
            #   print(name)
              print(file)
    #           # if the tuple created from splitext is not empty:
    #             # eg name, ext = (file, txt) and not name, ext = (file, "")
              if not excluded_dot:
                 continue
              
              if os.path.isdir(excluded_dot):
                  if excluded_dot in file:
                    shutil.move(file, excluded_dot)
                
    #           if excluded_dot and not os.path.isdir(excluded_dot) and not os.path.exists(excluded_dot):
    #             os.mkdir(excluded_dot)
    #             print("this is the excluded dot", excluded_dot)
    #             print("Name of the file", name)
    #             print("extension", ext)
    #           shutil.move(file,excluded_dot)
        except FileExistsError:
            print("File aready created")


#     def move_files(self):
#         """Move files
#             A Method responsible for moving files into directories
#         """
#         pass


try:
    organize1 = Organize()
    path = organize1.recieve_userInput()
except FileNotFoundError as fe:
    print("Error!",fe)
# content = os.listdir(path)
# print(content)
# print(path)
# organize1.manage_dir(path)


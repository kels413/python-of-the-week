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
        try:
            user_input = input("Please Enter The Directory you wish to arrange: ")
        
        
            cleaned_input = user_input.strip()

            expanded_path = os.path.expanduser(cleaned_input)

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
        except (EOFError, KeyboardInterrupt):
            print("\nGood bye!")
            exit(0)
    

    def manage_dir(self, path):
        """ create Direct ories
            a method responsible for creating directories
        """
        filename = "others"
        content = os.listdir(path)
        print(content)
       
        try:
          for file in content:
             #expand the file_name
              name, ext = os.path.splitext(file)
    #           #remove dot(.) from the ext using slicing.
              excluded_dot = ext[1:]
            #   print(name)
              print(file)
              if ext == ".DS_Store":
                  pass
    #           # if the tuple created from splitext is not empty:
    #             # eg name, ext = (file, txt) and not name, ext = (file, "")
              if os.path.isfile(file) and excluded_dot == "":
                  pass

                # check if the others dir already exists and just move files into it
              if os.path.exists(filename) and os.path.isdir(filename):
                    shutil.move(file, filename)
              else:
                os.mkdir(filename)
                shutil.move(file, filename)
                    # check if excluded path exists and has the file has an same extension
              if os.path.isdir(excluded_dot) and excluded_dot in file:
                    shutil.move(file, excluded_dot)

              if excluded_dot in file:
                    os.mkdir(excluded_dot)
                    shutil.move(file, excluded_dot)
        except (FileExistsError, shutil.Error):
            print(f"File Already exists ({file})")

try:
    organizer = Organize()
    path = organizer.recieve_userInput()
    organizer.manage_dir(path)
except FileNotFoundError as fe:
    print("Error!",fe)

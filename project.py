"""
A Python script for efficient file management on my system. The script should be able to perform tasks such as organizing files, moving, and possibly categorizing them. using OOP.
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
            
            os.chdir(expanded_path)
            return os.getcwd()
        except (EOFError, KeyboardInterrupt):
            print("\nGood bye!")
            exit(0)

    
    def create_dir(self, filename):
        if not os.path.isdir(filename):
            os.mkdir(filename)


    
    def move_files(self, filename, path):
        try:
            shutil.move(filename, path)
        except (FileExistsError, shutil.Error):
            print("File already exists")


    def manage_dir(self, path):
        """ create Direct ories
            a method responsible for creating directories
        """
        print(os.getcwd())
        dirname = "others"
        content = os.listdir(path)
        print(content)
        for file in content:
            name, ext = os.path.splitext(file)
            file_ext = ext[1:]        

            # file is directory and move files into it
            if name == ".DS_Store":
                continue
            if os.path.isdir(file_ext):
                self.move_files(file, file_ext)
            else:
                pass
            if file_ext: # file has an extension
                self.create_dir(file)
                self.move_files(file, file_ext)
        
            # others directory already exists
            if os.path.isdir(dirname):
                # move folders that has no extention and are files
                if not file_ext and os.path.isfile(file):
                    self.move_files(file, dirname)
            else:
                os.mkdir(dirname)
                if not file_ext and os.path.isfile(file):
                    self.move_files(file, dirname)

try:      
    organizer = Organize()
    path = organizer.recieve_userInput()
    organizer.manage_dir(path)
except FileNotFoundError as fe:
    print("Error!",fe)

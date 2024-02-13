import os
import shutil

class Organize:
    def receive_user_input(self) -> str:
        try:
            user_input = input("Please enter the directory you wish to arrange: ")
            cleaned_input = user_input.strip()

            expanded_path = os.path.expanduser(cleaned_input)

            # Check if the directory exists
            if not os.path.exists(expanded_path):
                raise FileNotFoundError("Directory does not exist")
            
            # Check whether the path exists but is not a directory
            if os.path.exists(expanded_path) and not os.path.isdir(expanded_path):
                raise FileNotFoundError("Provided path is a file, not a directory")

            os.chdir(expanded_path)
            return os.getcwd()
        
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            exit(0)

    def create_directory(self, directory_name):
        try:
            os.mkdir(directory_name)
        except FileExistsError:
            print(f"Directory already exists: {directory_name}")

    def move_files(self, filename, path):
        try:
            shutil.move(filename, path)
        except (FileExistsError, shutil.Error):
            print(f"File already exists in {path}")

    def manage_directory(self, path):
        print(os.getcwd())
        main_directory_name = "others"
        content = os.listdir(path)
        print(content)

        for file in content:
            name, ext = os.path.splitext(file)
            file_directory = ext[1:]        

            if name == ".DS_Store":
                continue

            if os.path.isdir(file_directory):
                self.move_files(file, file_directory)
            else:
                if file_directory:
                    self.create_directory(file_directory)
                    self.move_files(file, file_directory)

            if os.path.isdir(main_directory_name):
                if not file_directory and os.path.isfile(file):
                    self.move_files(file, main_directory_name)
            else:
                self.create_directory(main_directory_name)


try:      
    organizer = Organize()
    path = organizer.receive_user_input()
    organizer.manage_directory(path)
except FileNotFoundError as fe:
    print("Error:", fe)

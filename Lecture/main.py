import magic

def get_file_type(file_path):
    mime = magic.Magic()
    file_type = mime.from_file(file_path)
    return file_type

# Example usage:
file_path = 'movie'
file_type = get_file_type(file_path)

print(file_type)

import os
import os

def get_file_extension(file_path):
    """
    Get the file extension from a given file path.
    """
    return os.path.splitext(file_path)[1]

def create_output_directory(directory_path):
    """
    Create the output directory if it doesn't exist.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def check_file_extension(file_path):
    valid_extensions = ['.pdf', '.docx', '.txt']
    _, extension = os.path.splitext(file_path)
    if extension not in valid_extensions:
        raise ValueError(f'Invalid file extension: {extension}. Only {valid_extensions} are supported.')
    return extension
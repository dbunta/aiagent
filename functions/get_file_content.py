import os
import sys

def get_file_content(working_directory, file_path):
    if file_path.startswith("..") or file_path.startswith("/"):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    working_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_path, file_path))

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000
    with open(abs_file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) == 10000:
            file_content_string += f"[...File ""{file_path}"" truncated at 10000 characters]"
        return file_content_string


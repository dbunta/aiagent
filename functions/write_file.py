import os
import sys 

def write_file(working_directory, file_path, content):
    if file_path.startswith("..") or file_path.startswith("/"):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    working_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_path, file_path))

    # if not os.path.exists(abs_file_path):
    #     return f'Error: file path does not exist'

    try:
        with open(abs_file_path, 'w') as f:
            f.write(content)
    except Exception as e:
        return f'Error: {e}'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

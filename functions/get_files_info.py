import os
import sys

def get_files_info(working_directory, directory=None):
    try:
        if directory is not None and (directory.startswith("..") or directory.startswith("/")):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        working_path = os.path.abspath(working_directory)
        dir_path = ""
        if directory is None:
            dir_path = working_path
        else:
            dir_path = os.path.abspath(os.path.join(working_path, directory))


        if not os.path.isdir(dir_path):
            return f'Error: "{directory}" is not a directory'
        
        dir_contents = os.listdir(dir_path)

        #- README.md: file_size=1032 bytes, is_dir=False
        file_infos = []
        for item in dir_contents:
            item_path = os.path.join(dir_path, item)
            file_infos.append(f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}")

        return "\n".join(file_infos)
    except Exception as e:
        return f"Error: {e}"


        
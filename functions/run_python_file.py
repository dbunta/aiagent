import os
import subprocess
import sys

def run_python_file(working_directory, file_path):
    if file_path.startswith("..") or file_path.startswith("/"):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    working_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_path, file_path))

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    extension = os.path.splitext(abs_file_path)[-1]
    if file_path[-3:] != ".py" or extension != ".py":
        return f'Error: "{file_path}" is not a Python file.'

    try:
        command = [sys.executable, abs_file_path]
        result = subprocess.run(command, timeout=30, capture_output=True)
        if result.stderr:
            print(f'STDOUT: {result.stderr}')
        if result.stdout:
            print(f'STDERR: {result.stderr}')
        else:
            print("No output produced")
    except subprocess.CalledProcessError as e:
        print(f'Process exited with code {e.returncode}')


    


    return "so far so good"
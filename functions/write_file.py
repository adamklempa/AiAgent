import os

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(abs_working_directory, file_path))
    parent = os.path.dirname(target_file)
    if not target_file.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(parent):
        os.makedirs(parent, exist_ok=True)
    try:
        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{target_file}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: "{target_file}": {e}'

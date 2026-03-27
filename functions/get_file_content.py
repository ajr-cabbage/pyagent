import os

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        # get abs path and make full target path
        working_dir_abs = os.path.abspath(working_directory)
        target_filepath = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # check for valid path/file
        if os.path.commonpath([working_dir_abs, target_filepath]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_filepath):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # open and read file
        with open(target_filepath, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
            return content
    except Exception as e:
        return f"Error: {e}"

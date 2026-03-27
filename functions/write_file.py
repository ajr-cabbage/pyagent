import os


def write_file(working_directory, file_path, content):
    try:
        # get abs path and make full target path
        working_dir_abs = os.path.abspath(working_directory)
        target_filepath = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # check for valid path & make target dir
        if os.path.commonpath([working_dir_abs, target_filepath]) != working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_filepath):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(target_filepath), exist_ok=True)

        # open and write to file
        with open(target_filepath, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

# get_files_info
import os


def get_files_info(working_directory, directory="."):
    try:
        # get abs path and make full target path
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        # check for valid directory
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        dir_contents = os.listdir(target_dir)
        contents_str = ""
        for item in dir_contents:
            item_path = os.path.join(target_dir, item)
            item_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            contents_str += f"- {item}: file_size={item_size} bytes, is_dir={is_dir}\n"
        return contents_str[:-1]
    except Exception as e:
        return f"Error: {e}"

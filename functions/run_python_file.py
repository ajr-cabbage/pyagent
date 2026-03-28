import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        # get abs path and make full target path
        working_dir_abs = os.path.abspath(working_directory)
        target_filepath = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # check for valid path/isfile
        if os.path.commonpath([working_dir_abs, target_filepath]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_filepath):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # build the command
        command = ["python", target_filepath]
        if args:
            command.extend(args)

        # run the command and capture output
        output_str = ""
        comp_proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        if comp_proc.returncode != 0:
            output_str += f"Process exited with code {comp_proc.returncode}\n"
        if len(comp_proc.stderr) == 0 and len(comp_proc.stdout) == 0:
            output_str += "No output produced\n"
        else:
            output_str += f"STDOUT: {comp_proc.stdout}\nSTDERR: {comp_proc.stderr}\n"
        return output_str[:-1]

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python file at the specified file path, relative to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to the pythopn file that is to be run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Arguments passed to the python file. The default is no arguments.",
            ),
        },
        required=["file_path"],
    ),
)

import os

def get_file_info(working_directory, directory=None):
    if not directory.isdir(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
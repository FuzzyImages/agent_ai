import os

def get_files_info(working_directory, directory=None):
    working_directory_path = os.path.abspath(working_directory)
    directory_arg = os.path.abspath(os.path.join(working_directory_path, directory))
    print(f"TESTING directories paths:\nWorking Directory Path = {working_directory_path}\nDirectory Path = {directory_arg}")
    if not directory_arg.startswith(working_directory_path):
        return f'Error: Cannot list "{directory_arg}" as it is outside the permitted working directory'
    elif os.path.isdir(directory_arg) == False:
        return f'Error: "{directory_arg}" is not a directory'
 

    contents = ''

    for item in os.listdir(directory_arg):
        item_path = os.path.join(directory_arg, item)
        contents += f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}\n" 

    return contents
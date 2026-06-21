import os

def get_files_info(working_directory: str, directory: str = "."):
    
    # get absolute path of working directory
    working_dir = os.path.abspath(working_directory)
    # construct absolute path of target directory
    target_dir = os.path.join(working_dir, directory)
    target_dir = os.path.normpath(target_dir) # normalize
    
    if not os.path.isdir(target_dir):
        raise ValueError(f"Error, {directory} is not a directory.")
    
    # validate if target_dir is in working dir
    valid_target_dir = os.path.commonpath(target_dir, working_dir) == working_dir
    
    if not valid_target_dir:
        raise ValueError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    return f"Success, {directory} is within the working directory."
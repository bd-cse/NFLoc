import os

# Methods for folder and file processing

def _print_files_in_folder(folder_path : str):
    file_paths = [os.path.join(dirpath, filename) for dirpath, _, filenames in os.walk(folder_path) for filename in filenames]

    for file_path in file_paths:
        print(file_path)

def _make_file_paths_array(folder_path : str) -> list:
    file_paths = [os.path.join(dirpath, filename) for dirpath, _, filenames in os.walk(folder_path) for filename in filenames]
    path_array = []

    for file_path in file_paths:
        path_array.append(file_path)
    
    return path_array
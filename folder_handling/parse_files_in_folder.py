import os
import glob

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

def _print_folders_within_folder(folder_path : str):
    folders = [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]

    print(f"List of folders in {folder_path}:")
    for folder in folders:
        print(folder)

def _make_folder_paths_array(folder_path : str) -> list:
    return [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]

def _get_folder_paths_within_folder(folder_path : str) -> list:
    subfolders = []
    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            subfolders.append(item_path)
    
    return subfolders

def _get_all_images_given_folder(folder_path : str) -> list:
    return glob.glob(folder_path + '/**/*.tif', recursive=True)
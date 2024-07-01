from EXIF_handling.get_gps_data import _get_coordinates_as_point
from geojson_handling.get_geojson_info import _make_dict_with_coordinates_list
from folder_handling.parse_files_in_folder import _get_all_images_given_folder
import os
import sys

# def process_all_folders(folder_path : str):
#    folders = _get_folder_paths_within_folder(folder_path)
#
#    for folder in folders:
#        print(_make_dict_with_locations_count("Fields.geojson", folder))

def process_all_images(folder_path : str):
    images = _get_all_images_given_folder(folder_path)
    coords = []

    for image in images:
        coords.append(_get_coordinates_as_point(image))

    print(_make_dict_with_coordinates_list("Fields.geojson", coords))

if __name__ == '__main__':

    if (len(sys.argv) != 2):
        print("Usage: python NFLoc.py [folder_path]")
        exit(-1)
    
    if not(os.path.exists(sys.argv[1])):
        print("Couldn't find path. Is it surrounded by quotes?")
        exit(-1)

    process_all_images(sys.argv[1])
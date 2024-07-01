from EXIF_handling.get_gps_data import _get_coordinates_as_point
from geojson_handling.get_geojson_info import _print_location_of_coordinate, _print_all_shapes_in_geojson, _make_dict_with_locations_count
from folder_handling.parse_files_in_folder import _make_file_paths_array, _make_folder_paths_array, _get_folder_paths_within_folder
import sys

def process_all_folders(folder_path : str):
    folders = _get_folder_paths_within_folder(folder_path)

    for folder in folders:
        print(_make_dict_with_locations_count("Fields.geojson", folder))

if __name__ == '__main__':
    process_all_folders(sys.argv[1])
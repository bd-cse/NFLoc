from EXIF_parsing.get_gps_data import _print_latitude_and_longitude, _get_coordinates_as_list, _get_coordinates_as_point
from geojson_parsing.get_geojson_info import _print_all_shapes_in_geojson, _print_first_shape_in_geojson, _print_location_of_coordinate
from folder_parsing.parse_files_in_folder import _make_file_paths_array

if __name__ == '__main__':
    tif_path = input("Enter tif folder path: ")
    tif_path.replace('\\', '\\\\')

    geojson_path = input("Enter geojson path: ")
    geojson_path.replace('\\', '\\\\')

    paths =_make_file_paths_array(tif_path)
    for path in paths:
        coords = _get_coordinates_as_point(path)
        _print_location_of_coordinate(geojson_path, coords)
    
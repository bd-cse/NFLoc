from EXIF_handling.get_gps_data import _get_coordinates_as_point
from geojson_handling.get_geojson_info import _print_location_of_coordinate, _print_all_shapes_in_geojson
from folder_handling.parse_files_in_folder import _make_file_paths_array
import sys

# if __name__ == '__main__':
#    tif_path = input("Enter tif folder path: ")
#    tif_path.replace('\\', '\\\\')
#
#    geojson_path = input("Enter geojson path: ")
#    geojson_path.replace('\\', '\\\\')
#
#    paths =_make_file_paths_array(tif_path)
#    for path in paths:
#        coords = _get_coordinates_as_point(path)
#        _print_location_of_coordinate(geojson_path, coords)

if __name__ == '__main__':
    print(sys.argv[0])

    if (len(sys.argv) != 3):
        print("Usage: python main.py -geojsonpath -tiffolderpath")
        exit(-1)

    print(sys.argv[1])
    print(sys.argv[2])

    arr = _make_file_paths_array(sys.argv[2])
    print(arr)

    _print_all_shapes_in_geojson(sys.argv[1])
    
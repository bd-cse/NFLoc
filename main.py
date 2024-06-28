from EXIF_processing.get_gps_data import _print_latitude_and_longitude, _get_coordinates_as_list, _get_coordinates_as_point
from geojson_processing.get_geojson_info import _print_all_shapes_in_geojson, _print_first_shape_in_geojson, _print_location_of_coordinate

if __name__ == '__main__':
    _print_latitude_and_longitude('IMG_0000_1.tif')
    
    coordinates = _get_coordinates_as_point('IMG_0000_1.tif')
    _print_location_of_coordinate('Fields.geojson', coordinates)
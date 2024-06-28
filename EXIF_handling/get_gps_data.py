import exifread
import exifread.utils
from shapely.geometry import Point


# Functions for processing GPS data from tiff files

def _print_latitude_and_longitude(tif_path : str):
    tags = {}
    with open(tif_path, 'rb') as f:
        tags = exifread.process_file(f, details=False)
    
    if "GPS GPSLatitude" in tags.keys():
        lat = tags["GPS GPSLatitude"]
        print("Latitude: " + str(lat))
    else:
        print("Did not find 'GPS GPSLatitude'")

    if "GPS GPSLongitude" in tags.keys():
        lon = tags["GPS GPSLongitude"]
        print("Longitude: " + str(lon))
    else:
        print("Did not find 'GPS GPSLongitude'")

# Puts decimal coordinates from an image into list of form [lon, lat]
def _get_coordinates_as_list(tif_path : str) -> list:
    tags = {}
    with open(tif_path, 'rb') as f:
        tags = exifread.process_file(f, details=False)

    coords = exifread.utils.get_gps_coords(tags)
    return [coords[1], coords[0]]

def _get_coordinates_as_point(tif_path : str) -> Point:
    return Point(_get_coordinates_as_list(tif_path))
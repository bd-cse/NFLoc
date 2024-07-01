import geojson
from shapely.geometry import shape, Point
from folder_handling.parse_files_in_folder import _make_file_paths_array
from EXIF_handling.get_gps_data import _make_list_of_coordinates_from_tiffs

# Functions for getting information about coordinates and geographical data
# from a geojson file

def _print_first_shape_in_geojson(geojson_path : str):
    with open(geojson_path, "r") as f:
      gj = geojson.load(f)

      shapely_polygon = shape(gj["features"][0]["geometry"])
      print(shapely_polygon)

def _print_all_shapes_in_geojson(geojson_path : str):
   with open(geojson_path, "r") as f:
    gj = geojson.load(f)

    i = 0
    for polygon in gj["features"]:
        print(gj["features"][i]["properties"])
        print(str(gj["features"][i]["geometry"]) + '\n')

        i += 1

def _print_location_of_coordinate(geojson_path : str, coordinate: Point):
    with open(geojson_path, "r") as f:
      gj = geojson.load(f)

      i = 0
      for polygon in gj["features"]:
        shapely_poly = shape(gj["features"][i]["geometry"])
        
        if coordinate.within(shapely_poly):
           print(gj["features"][i]["properties"]["Name"])
           return

        i += 1
      
      print("No location found")

def _make_dict_with_locations_count(geojson_path : str, folder_path : str) -> dict:
   with open(geojson_path, "r") as f:
      gj = geojson.load(f)
      coords_list = _make_list_of_coordinates_from_tiffs(folder_path)
      locations_dict = {}

      for coordinate in coords_list:

        i = 0
        for polygon in gj["features"]:
          shapely_poly = shape(gj["features"][i]["geometry"])

          if coordinate.within(shapely_poly):
             
             key = gj["features"][i]["properties"]["Name"]
             if key not in locations_dict:
                locations_dict[key] = 0
             
             locations_dict[key] += 1
          i += 1

   return locations_dict
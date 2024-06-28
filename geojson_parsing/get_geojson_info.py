import geojson
from shapely.geometry import shape, Point

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
        print(gj["features"][i]["geometry"] + '\n')

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
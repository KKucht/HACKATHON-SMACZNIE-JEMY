import geopy.distance

def minutes_from_coordinates(coords1, coords2, v):
    s = geopy.distance.geodesic((coords1[1], coords1[0]), (coords2[1], coords2[0])).km
    min_in_h = 60
    return s/v*min_in_h
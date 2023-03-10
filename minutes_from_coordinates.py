import geopy.distance

avg_speeds = {
    'walk' : 1.4,
    'bike' : 57.6
}

def get_distance_from_coordinates(coords1, coords2):
    return geopy.distance.geodesic((coords1[1], coords1[0]), (coords2[1], coords2[0])).km

def minutes_from_coordinates(coords1, coords2, mode):
    speed = avg_speeds[mode] * 3.6
    s = get_distance_from_coordinates(coords1, coords2)
    min_in_h = 60
    return s/speed*min_in_h
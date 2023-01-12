from minutes_from_coordinates import minutes_from_coordinates
from time_between_points import time_between_points


def create_list_with_bools(dic_locations,point, graph_for_walking, graph_for_biking):
    new_dict = {}
    for key in dic_locations.keys():
        locations = dic_locations[key]
        new_dict[key] = False
        for location in locations:
            if minutes_from_coordinates(point, location, 'bike') <= 15.0:
                print("1\n")
                if time_between_points(graph_for_biking,point, location, 'bike') <= 15.0:
                    new_dict[key] = True
                    break
                print("2\n")
                if minutes_from_coordinates(point, location, 'walk') <= 15.0:
                    print("3\n")
                    if time_between_points(graph_for_walking,point, location, 'walk') <= 15.0:
                        new_dict[key] = True
                        break
                    print("4\n")
    return new_dict
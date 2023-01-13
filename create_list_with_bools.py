import networkx

from minutes_from_coordinates import minutes_from_coordinates
from time_between_points import time_between_points


def create_list_with_bools(dic_locations,point, graph_for_walking, graph_for_biking):
    new_dict = {}
    for key in dic_locations.keys():
        locations = dic_locations[key]
        closest = [False, (0, 0, 'xd'), 'empty']
        closest_time = 10000
        for long_location in locations:
            location = (long_location[0], long_location[1])
            if minutes_from_coordinates(point, location, 'bike') <= 15.0:
                    if minutes_from_coordinates(point, location, 'walk') <= 15.0:
                        time = time_between_points(graph_for_walking,point, location, 'walk')
                        if time <= 15.0:
                            if closest[2] == 'bike' or time < closest_time:
                                closest_time = time
                                closest = [True, long_location, 'walk']
                                break
                    if closest[2] != 'walk':
                        try:
                            bike_time = time_between_points(graph_for_biking,point, location, 'bike')
                        except networkx.exception.NetworkXNoPath:
                            continue
                        if bike_time <= 15.0 and bike_time < closest_time:
                            closest_time = bike_time
                            closest = [True, long_location, 'bike']
                            break

        new_dict[key] = closest
    return new_dict
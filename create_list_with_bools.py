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
            if minutes_from_coordinates(point, location, 'walk') <= 15.0:
                try:
                    time = time_between_points(graph_for_walking,point, location, 'walk')
                    if time <= 15.0:
                        if time < closest_time:
                            closest_time = time
                            closest = [True, long_location, 'walk']
                            break
                except networkx.exception.NetworkXNoPath:
                    continue
        if closest[2] != 'walk':
            for long_location in locations:
                location = (long_location[0], long_location[1])
                if minutes_from_coordinates(point, location, 'bike') <= 15.0:
                    try:
                        time = time_between_points(graph_for_walking, point, location, 'bike')
                        if time <= 15.0:
                            if time < closest_time:
                                closest_time = time
                                closest = [True, long_location, 'bike']
                                break
                    except networkx.exception.NetworkXNoPath:
                        continue
        new_dict[key] = closest
    return new_dict
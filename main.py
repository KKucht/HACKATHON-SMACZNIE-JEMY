from map_graph import get_map_graph
from create_points_list import create_points_list
from data_extraction import get_places_dictionary
from create_list_with_bools import create_list_with_bools
from calculate_value import calculate_value
from display_heatmap import display_heatmap

def main():
    print("start get_map_graph")
    graph_biking = get_map_graph('bike')
    print("start get_map_graph")
    graph_walking = get_map_graph('walk')
    print("start create_points_list")
    points = create_points_list()
    print(len(points))
    print("start get_places_dictionary")
    dict_locations = get_places_dictionary()
    values = []
    for point in points:
        print("start create_list_with_bools")
        dict_loc = create_list_with_bools(dict_locations,point,graph_walking,graph_biking)
        values.append(calculate_value(dict_loc))
    print("start display_heatmap")
    display_heatmap(points,values)




if __name__ == '__main__':
    main()
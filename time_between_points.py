import osmnx as ox
import networkx as nx
avg_speeds = {
    'walk' : 1.4,
    'bike' : 57.6
}
def time_between_points(graph, point1, point2, mode):
    speed = avg_speeds[mode]
    orig_node = ox.nearest_nodes(graph, point1[0], point1[1])
    dest_node = ox.nearest_nodes(graph, point2[0], point2[1])
    shortest_path_length = nx.shortest_path_length(graph,
                                      orig_node,
                                      dest_node,
                                      weight='length')
    return (shortest_path_length/speed)/60

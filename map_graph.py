import osmnx as ox
import networkx as nx
import folium

def get_map_graph(mode):
    # mode: 'walk' or 'bike'

    place = 'Gdańsk, Poland'
    return ox.graph_from_place(place, network_type=mode)
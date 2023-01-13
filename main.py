import folium as fl
from streamlit_folium import st_folium
import streamlit as st
from map_graph import get_map_graph
from data_extraction import get_places_dictionary
from create_list_with_bools import create_list_with_bools
from minutes_from_coordinates import get_distance_from_coordinates

def get_pos(lat,lng):
    return lat,lng

if 'location' not in st.session_state:
    st.session_state['location'] = [54.3520, 18.6466]

if 'zoom_start' not in st.session_state:
    st.session_state['zoom_start'] = 13

m = fl.Map(location=st.session_state['location'], zoom_start=st.session_state['zoom_start'])

m.add_child(fl.LatLngPopup())

if 'markers' not in st.session_state:
    print("create markers")
    st.session_state['markers'] = []

if 'graph_walk' not in st.session_state:
    print("create graph_walk")
    st.session_state['graph_walk'] = get_map_graph('walk')

if 'graph_bike' not in st.session_state:
    print("create graph_bike")
    st.session_state['graph_bike'] = get_map_graph('bike')

if 'locations' not in st.session_state:
    print("create locations")
    st.session_state['locations'] = get_places_dictionary()

if len(st.session_state["markers"]) != 0:
    for marker in st.session_state["markers"]:
        m.add_child(marker)

map = st_folium(m, height=700, width=700)


if map['last_clicked'] is not None:
    data = get_pos(map['last_clicked']['lat'], map['last_clicked']['lng'])
    if data is not None:
        print("click!")
        point = (data[1], data[0])
        reference_point = 18.6265931, 54.3721152
        if get_distance_from_coordinates(point, reference_point) < 20:
            print("create list")
            locations = create_list_with_bools(st.session_state['locations'],point, st.session_state['graph_walk'], st.session_state['graph_bike'])
            st.session_state['markers'] = []
            st.session_state['markers'].append(fl.Marker(
                [data[0], data[1]], popup="<b>Here</b>"
            ))
            for key in locations.keys():
                location = locations[key]
                if location[0]:
                    st.session_state['markers'].append(fl.Marker(
                        [location[1][1], location[1][0]], popup="<i>"+location[1][2]+"</i>", tooltip=key , icon=fl.Icon(color="red"),
                    ))
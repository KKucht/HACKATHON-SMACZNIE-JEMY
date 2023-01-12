import folium
from folium.plugins import HeatMap
import itertools

def display_heatmap(points, values):
    gdansk_map = folium.Map(location=[54.35, 18.64], zoom_start=12)

    # konwersja punktów na format dla HeatMap
    heat_points = [[point[1], point[0], value] for point, value in itertools.product(points, values)]

    # dodanie heatmapy do mapy
    HeatMap(heat_points).add_to(gdansk_map)

    # wyświetlenie mapy
    gdansk_map.save("heatmap.html")
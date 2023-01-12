import folium
from folium.plugins import HeatMap

def display(points):
    gdańsk_map = folium.Map(location=[54.35, 18.64], zoom_start=12)

    # konwersja punktów na format dla HeatMap
    heat_points = [[point[1], point[0], point[2]] for point in points]

    # dodanie heatmapy do mapy
    HeatMap(heat_points).add_to(gdańsk_map)

    # wyświetlenie mapy
    gdańsk_map.save("heatmap.html")
import pandas as pd
import os
from minutes_from_coordinates import get_distance_from_coordinates

def get_places_dictionary():
    reference_point = 18.6265931, 54.3721152
    places_dictionary = dict()
    csv_files = os.listdir('data')
    for file in csv_files:
        place_type_list = list()
        df = pd.read_csv(f'data/{file}')
        place_type = df['type'].values[0]
        for i in range(len(df.index)):
            place = df.iloc[i]
            if get_distance_from_coordinates((place.loc['loc'], place.loc['lat']), reference_point) < 20:
                place_type_list.append((place.loc['lon'], place.loc['lat'], place.loc['title']))
        places_dictionary[place_type] = place_type_list
    return places_dictionary




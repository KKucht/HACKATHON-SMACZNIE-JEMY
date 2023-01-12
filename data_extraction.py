import pandas as pd
import os

def get_places_dictionary():
    places_dictionary = dict()
    csv_files = os.listdir('data')
    for file in csv_files:
        place_type_list = list()
        df = pd.read_csv(f'data/{file}')
        place_type = df['type'].values[0]
        for i in range(len(df.index)):
            place = df.iloc[i]
            place_type_list.append((place.loc['lon'], place.loc['lat']))
        places_dictionary[place_type] = place_type_list
    return places_dictionary




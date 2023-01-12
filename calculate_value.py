
def calculate_value(presence_of_location):
    # value of point
    number_of_present_locations = 0
    for presence in presence_of_location:
        if presence:
            number_of_present_locations += 1
    return number_of_present_locations

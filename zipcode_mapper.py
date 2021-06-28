import json
from const import l_cities 

# ------------------------------ Purpose ------------------------------
# The purpose of this file is to create a hashmap of where the cities are keys and the value is a list of zipcodes for that city 
# ---------------------------------------------------------------------
# Variables 
# ------------------------------------------------------------------------------------------------------------------------------------------

# File name to be passed into main function
filename = "House-feb-28-2021.json"

# create a variable to hold zipcodes that could not be mapped to a specific city 
unclaimed = 'unclaimed'

# Create a hash map where l_cities are the keys and the values are a list of zipcodes
city_zipcode = {city: list() for city in l_cities}

# ------------------------------------------------------------------------------------------------------------------------------------------
# Helper methods
# ------------------------------------------------------------------------------------------------------------------------------------------

# Append the unclaimed variable to l_cities
# Returns the appended list
def append_to_lCities(unclaimed):
    l_cities.append(unclaimed)
    return l_cities

# Appending 
city_zipcode = append_to_lCities(unclaimed)

# This method receives a dictionary and parses the address to see what city list it should belong too  
# TODO add regex 
def mapper(location_dict):
    # New York
    if 'New York' in location_dict['address']:
        city_zipcode['newyork - ny'].append(location_dict['zip_code'])

    elif 'IL' in location_dict['address']:
        city_zipcode['chicago-il'].append(location_dict['zip_code'])

    elif 'FL' in location_dict['address']:
        city_zipcode['miami-fl'].append(location_dict['zip_code'])

    elif 'Denver' in location_dict['address']:
        city_zipcode['denver-co'].append(location_dict['zip_code']) 

    elif 'Austin' in location_dict['address']:
        city_zipcode['austin-tx'].append(location_dict['zip_code']) 

    elif 'Dallas' in location_dict['address']:
        city_zipcode['dallas-tx'].append(location_dict['zip_code']) 

    elif 'San Francisco' in location_dict['address']:
        city_zipcode['san-francisco-ca'].append(location_dict['zip_code']) 

    elif 'Los Angeles' in location_dict['address']:
        city_zipcode['los-angeles-ca'].append(location_dict['zip_code']) 
        
    elif 'Boulder' in location_dict['address']:
        city_zipcode['boulder-co'].append(location_dict['zip_code']) 

    elif 'Washington' in location_dict['address'] or 'Virgina' in location_dict['address'] or 'Maryland' in location_dict['address']:
        city_zipcode['washington-dc'].append(location_dict['zip_code']) 

    else:
        city_zipcode['unclaimed'].append(location_dict['zip_code'])
    # if the line has an address line which the regex maps to one of the 10 categories add that zip code to the set of city zip codes

# ------------------------------------------------------------------------------------------------------------------------------------------
# Appending - runs before entry point 
# -----------------------------------------------------------------------------------------------------------------------------------------
city_zipcode = append_to_lCities(unclaimed)
# ------------------------------------------------------------------------------------------------------------------------------------------
# Entry Point for zipcode mapper module
# ------------------------------------------------------------------------------------------------------------------------------------------
def entry_point(filename, additional=None):
    
    with open(filename) as f:
        data = json.load(f)
        for record in data:
            mapper(record)


    with open('mappedzips.json', 'w+') as f:
        json.dump(city_zipcode, f)
# ------------------------------------------------------------------------------------------------------------------------------------------

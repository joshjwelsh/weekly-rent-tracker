import json
from const import l_cities as LC

# ------------------------------ Purpose ------------------------------
# The purpose of this file is to create a hashmap of where the cities are keys and the value is a list of zipcodes for that city 
# ---------------------------------------------------------------------


class Mappr:
    def __init__(self):
        try:
            self.unclaimed = 'unclaimed' 
            self.l_cities = LC + [self.unclaimed]
            self.city_zipcode = {city: list() for city in self.l_cities}
        except Exception as e:
            print("Error in init - ", e)
# This method receives a dictionary and parses the address to see what city list it should belong too  
# TODO add regex 
    def mapper(self, location_dict):
        try:
            # New York
            if 'New York' in location_dict['address']:
                self.city_zipcode['newyork - ny'].append(location_dict['zip_code'])

            elif 'IL' in location_dict['address']:
                self.city_zipcode['chicago-il'].append(location_dict['zip_code'])

            elif 'FL' in location_dict['address']:
                self.city_zipcode['miami-fl'].append(location_dict['zip_code'])

            elif 'Denver' in location_dict['address']:
                self.city_zipcode['denver-co'].append(location_dict['zip_code']) 

            elif 'Austin' in location_dict['address']:
                self.city_zipcode['austin-tx'].append(location_dict['zip_code']) 

            elif 'Dallas' in location_dict['address']:
                self.city_zipcode['dallas-tx'].append(location_dict['zip_code']) 

            elif 'San Francisco' in location_dict['address']:
                self.city_zipcode['san-francisco-ca'].append(location_dict['zip_code']) 

            elif 'Los Angeles' in location_dict['address']:
                self.city_zipcode['los-angeles-ca'].append(location_dict['zip_code']) 
                
            elif 'Boulder' in location_dict['address']:
                self.city_zipcode['boulder-co'].append(location_dict['zip_code']) 

            elif 'Washington' in location_dict['address'] or 'Virgina' in location_dict['address'] or 'Maryland' in location_dict['address']:
                self.city_zipcode['washington-dc'].append(location_dict['zip_code']) 

            else:
                self.city_zipcode['unclaimed'].append(location_dict['zip_code'])
            # if the line has an address line which the regex maps to one of the 10 categories add that zip code to the set of city zip codes
        except Exception as e:
            print("Error when mapping zip codes in mapper method - ", e)


    # ------------------------------------------------------------------------------------------------------------------------------------------
    # Entry Point for zipcode mapper module
    # ------------------------------------------------------------------------------------------------------------------------------------------
    def entry_point(self, filename, additional=None):
        try:
            with open(filename) as f:
                data = json.load(f)
                for record in data:
                    self.mapper(record)


            with open('mappedzips.json', 'w+') as f:
                json.dump(self.city_zipcode, f)
        except Exception as e:
            print("Error at entry point - ", e)

    # ------------------------------------------------------------------------------------------------------------------------------------------

import json
import re

l_cities = [
    'newyork - ny',
    'los-angeles-ca',
    'san-francisco-ca',
    'denver-co',
    'washington-dc',
    'miami-fl',
    'chicago-il',
    'dallas-tx',
    'austin-tx',
    'boulder-co',
    'unclaimed'
]

def mapper(line):
    # New York
    if 'New York' in line['address']:
        record['newyork - ny'].append(line['zip_code'])

    elif 'IL' in line['address']:
        record['chicago-il'].append(line['zip_code'])

    elif 'FL' in line['address']:
        record['miami-fl'].append(line['zip_code'])

    elif 'Denver' in line['address']:
        record['denver-co'].append(line['zip_code']) 

    elif 'Austin' in line['address']:
        record['austin-tx'].append(line['zip_code']) 

    elif 'Dallas' in line['address']:
        record['dallas-tx'].append(line['zip_code']) 

    elif 'San Francisco' in line['address']:
        record['san-francisco-ca'].append(line['zip_code']) 

    elif 'Los Angeles' in line['address']:
        record['los-angeles-ca'].append(line['zip_code']) 
        
    elif 'Boulder' in line['address']:
        record['boulder-co'].append(line['zip_code']) 

    elif 'Washington' in line['address'] or 'Virgina' in line['address'] or 'Maryland' in line['address']:
        record['washington-dc'].append(line['zip_code']) 

    else:
        record['unclaimed'].append(line['zip_code'])
    # if the line has an address line which the regex maps to one of the 10 categories add that zip code to the set of city zip codes





record = {city:list() for city in l_cities}
print(record)

with open('House-oct-25-2020.json') as f:
    data = json.load(f)
    for line in data:
        mapper(line) 

with open('mappedzips.json','w+') as f:
    json.dump(record,f)


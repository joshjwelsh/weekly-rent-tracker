import json
import logging
from const import MAX_L_FILENAMES_DATA_FORMATER as MAX

# Init a logger for file errors
logger = logging.getLogger(__name__)

# Entry point to data formatter 
# entry point accepts as filenames as an argument
def entry_point(l_filenames):
    
    # Init data structures
    record = dict()
    zipSet = set()

    try:
        # test to see l_filenames is correctly sized or not
        # raise error if it is not correctly sized
        if len(l_filenames) > MAX or len(l_filenames) < MAX:
            raise ValueError('This function must pass in a list with 2 values. It failed to do so', f'Size of l_filenames: {len(l_filenames)}' )
        
        # Decompose filename list into zipset file, json file and records file
        jsonFile, zipcodeFile, recordsJsonFile = l_filenames
        
        
        with open(jsonFile) as json_:
            data = json.load(json_)
            print(data)
            for item in data:
                if item['zip_code'] in zipSet:
                    record[item['zip_code']].append(item['price'])
                else:
                    zipSet.add(item['zip_code'])
                    record[item['zip_code']] = list()
                    record[item['zip_code']].append(item['price'])

        zresults = {'zipcodes':zipSet}
        with open(zipcodeFile, 'w+') as f:
            for z in zipSet:
                f.write("%s\n" % z)

        with open(recordsJsonFile, 'w+') as f:
            json.dump(record, f)
    
    except ValueError as error:
        logger.error(error)
        

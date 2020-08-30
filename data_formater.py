import json

record = dict()
zipSet = set()

with open('House_data_v3_aug_28_2020.json') as json_:
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
with open('zip_set.txt', 'w+') as f:
    for z in zipSet:
        f.write("%s\n" % z)

with open('records_v1.json','w+') as f:
    json.dump(record, f)
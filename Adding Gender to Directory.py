import json

with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\Scraped_Data.json', 'r') as f:
    datastore = json.load(f)

for data in datastore['friends']['data']:
    if 'name' in data:
        print(data['name'])
        try:
            with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\gender.json'.format(data['name']), 'w') as f:
                json.dump(data['gender'], f)
        except:
            continue

import json
import wikipedia
import csv

with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\Scraped_Data.json', 'r') as f:
    datastore = json.load(f)
for data in datastore['friends']['data']:
    try:
        print(data['name'])
        Name= data['name']
        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\favorite_teams.json'.format(data['name']), 'r') as f:
            data= json.load(f)
            with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\favorite_teams_desc.csv'.format(Name), 'w', newline='') as csvfile:
                writer= csv.writer(csvfile, delimiter='|')
                for iter in data:
                        print(iter['name'])
                        try:
                            desc = wikipedia.summary(iter['name'], sentences=1)
                            print(desc)
                            writer.writerow([iter['name'], desc])
                        except:
                            print("Exception Raised")
                            continue
    except:
        print("Exception Raised: No file found")
        continue
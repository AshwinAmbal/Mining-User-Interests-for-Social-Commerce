import json
import csv
import nltk

map = dict()
count = dict()
with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\Keywords.csv', 'r', newline='') as file:
            reader1= csv.reader(file, delimiter='|')
            for row1 in reader1:
                map[row1[0]] = row1[1]
                count[row1[1]] = 0

with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\Scraped_Data.json', 'r') as f:
    datastore = json.load(f)
for data in datastore['friends']['data']:
    for key in count:
        count[key] = 0 
    try:
        print(data['name'])
        Name = data['name']
        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\favorite_athletes_desc.csv'.format(Name), 'r', newline='') as csvfile:
                    reader= csv.reader(csvfile, delimiter='|')
                    for row in reader:
                        words = nltk.word_tokenize(row[1])
                        for word in words:
                            if word in map:
                                count[map[word]] += 1
        print(count)
    except Exception as e:
        print(e)
        continue
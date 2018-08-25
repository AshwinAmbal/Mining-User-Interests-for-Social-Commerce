import json
import csv
with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\Scraped_Data.json', 'r') as f:
    datastore = json.load(f)
likes_categories = ['Games/Toys', 'Athlete', 'Musician/Band', 'Board Game', 'Public Figure', 'Author',
                    'TV', 'Video Game', 'Musician', 'Movie', 'Artist', 'Sport', 'Sports', 'Product/Service',
                    'Society & Culture Website', 'Cause', 'Organization', 'Computer Company', 'Sports Team',
                    'Motor Vehicle Company','Motivational Speaker', 'Actor', 'Entrepreneur','Actress',
                    'Photographer', 'Article', 'Company', 'Journalist']
for data in datastore['friends']['data']:
    try:
        print(data['name'])
        Name = data['name'] 
        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\likes.json'.format(data['name']), 'r') as f:
                datas = json.load(f)
                with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\likes_desc.csv'.format(Name), 'w', newline='') as csvfile:
                    writer= csv.writer(csvfile, delimiter='|')
                    for iter in datas['data']:
                        if iter['category'] in likes_categories: 
                            print(iter['name'], "|", iter['category'])
                            writer.writerow([iter['name'], iter['category']])
    except:
        print()
        continue
    print()
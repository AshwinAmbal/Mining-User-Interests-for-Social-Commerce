import json
import os
with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\Scraped_Data.json', 'r') as f:
    datastore = json.load(f)
    
print(datastore['friends']['data'][0].keys())

for data in datastore['friends']['data']:
    if 'name' in data:
        print(data['name'])
        try:
            os.makedirs(data['name'])
        except OSError as e:
            if e:
                continue
        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\name.json'.format(data['name']), 'w') as f:
            json.dump(data['name'], f)
        if 'birthday' in data:
            with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\birthday.json'.format(data['name']), 'w') as f:
                json.dump(data['birthday'], f)
        if 'favorite_athletes' in data:
            with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\favorite_athletes.json'.format(data['name']), 'w') as f:
                json.dump(data['favorite_athletes'], f)
        if 'favorite_teams' in data:
            with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\favorite_teams.json'.format(data['name']), 'w') as f:
                json.dump(data['favorite_teams'], f)
        if 'likes' in data:
            with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\likes.json'.format(data['name']), 'w') as f:
                json.dump(data['likes'], f)
        if 'books' in data:
            with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\books.json'.format(data['name']), 'w') as f:
                json.dump(data['books'], f)
        if 'movies' in data:
            with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\movies.json'.format(data['name']), 'w') as f:
                json.dump(data['movies'], f)
        if 'music' in data:
            with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\music.json'.format(data['name']), 'w') as f:
                json.dump(data['music'], f)
        if 'posts' in data:
            with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\posts.json'.format(data['name']), 'w') as f:
                json.dump(data['posts'], f)
        if 'events' in data:
            with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\events.json'.format(data['name']), 'w') as f:    
                json.dump(data['events'], f)

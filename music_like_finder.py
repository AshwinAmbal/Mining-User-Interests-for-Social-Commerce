import json
import csv
from PyLyrics import PyLyrics

with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\Scraped_Data.json', 'r') as f:
    datastore = json.load(f)
for data in datastore['friends']['data']:
    try:
        print(data['name'])
        Name = data['name']
        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\music.json'.format(data['name']), 'r') as f:
            datas= json.load(f)
            with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\favorite_music_albums.csv'.format(Name), 'w', newline='') as csvfile:
                    writer= csv.writer(csvfile, delimiter='|')
                    for iter in datas['data']:
                        try:
                            print(iter['name'])
                            albums = PyLyrics.getAlbums(singer=iter['name'])
                            print(albums[0])
                            writer.writerow([albums[0], iter['name']])
                        except Exception as e:
                            print(e)
                            continue
                
    except:
        print("No.. Failed Here")
        continue
    print()
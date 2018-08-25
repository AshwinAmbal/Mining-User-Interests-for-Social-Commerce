import json
import csv
import tmdbsimple as tmdb

tmdb.API_KEY = 'c4e57d0edde7695d75b49df941f50b3d'
search = tmdb.Search()
with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\Scraped_Data.json', 'r') as f:
    datastore = json.load(f)
for data in datastore['friends']['data']:
    try:
        print(data['name'])
        Name = data['name']
        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\movies.json'.format(data['name']), 'r') as f:
            datas= json.load(f)
            with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\favorite_similar_movies.csv'.format(Name), 'w', newline='') as csvfile:
                    writer= csv.writer(csvfile, delimiter='|')
                    for iter in datas['data']:
                        try:
                            print(iter['name'])
                            response = search.movie(query=iter['name'])
                            movies = tmdb.Movies(search.results[0]['id'])
                            response = movies.similar_movies()
                            print(movies.results[0]['title'],movies.results[0]['id'])
                            writer.writerow([movies.results[0]['title'],movies.results[0]['id']])
                        except Exception as e:
                            print(e)
                            continue
                
    except:
        print("No.. Failed Here")
        continue
    print()
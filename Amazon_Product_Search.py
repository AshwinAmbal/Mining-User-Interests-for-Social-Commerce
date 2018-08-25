from amazon.api import AmazonAPI
import csv
import json
amazon = AmazonAPI('AKIAIEOGZE3ZYS64PKVQ',
                   'bOvagh6eyGG8sVvI8ZipAdrs4qOk5d93BVfKr39A',
                   'abcd12340eb-21',
                   MaxQPS=0.9,
                   Region='US')

with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\Scraped_Data.json', 'r') as f:
    datastore = json.load(f)
    
for data in datastore['friends']['data']:
    try:
        print(data['name'])
        Name = data['name'] 
        counter = 0
        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\favorite_books_desc.csv'.format(Name), 'r') as f:
                reader= csv.reader(f, delimiter='|')
                for row in reader:
                    try:
                        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\probable_gifts.csv'.format(Name), 'a', newline='') as csvfile:
                            writer= csv.writer(csvfile, delimiter='|')
                            products = amazon.search(Keywords=row[1], SearchIndex='Books')
                            for i, product in enumerate(products):
                                print(product) 
                                writer.writerow([product])
                                counter += 1
                                break
                            if counter == 3:
                                break
                    except Exception as e:
                        print(e)
                        continue
    except Exception as e:
        print(e)
        continue
    
for data in datastore['friends']['data']:
    try:
        print(data['name'])
        Name = data['name'] 
        counter = 0
        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\favorite_similar_movies.csv'.format(Name), 'r') as f:
                reader= csv.reader(f, delimiter='|')
                for row in reader:
                    try:
                        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\probable_gifts.csv'.format(Name), 'a', newline='') as csvfile:
                            writer= csv.writer(csvfile, delimiter='|')
                            products = amazon.search(Keywords=row[0], SearchIndex='Movies')
                            for i, product in enumerate(products):
                                print(product) 
                                writer.writerow([product])
                                counter += 1
                                break
                            if counter == 3:
                                break
                    except Exception as e:
                        print(e)
                        continue
    except Exception as e:
        print(e)
        continue
    
for data in datastore['friends']['data']:
    try:
        print(data['name'])
        Name = data['name'] 
        counter = 0
        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\favorite_music_albums.csv'.format(Name), 'r') as f:
                reader= csv.reader(f, delimiter='|')
                for row in reader:
                    try:
                        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\probable_gifts.csv'.format(Name), 'a', newline='') as csvfile:
                            writer= csv.writer(csvfile, delimiter='|')
                            products = amazon.search(Keywords=row[1], SearchIndex='Music')
                            for i, product in enumerate(products):
                                print(row[1], product) 
                                writer.writerow([product])
                                counter += 1
                                break
                            if counter == 3:
                                break
                    except Exception as e:
                        print(e)
                        continue
    except Exception as e:
        print(e)
        continue
    
for data in datastore['friends']['data']:
    try:
        print(data['name'])
        Name = data['name'] 
        counter = 0
        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\likes_desc.csv'.format(Name), 'r') as f:
                reader= csv.reader(f, delimiter='|')
                for row in reader:
                    try:
                        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\probable_gifts.csv'.format(Name), 'a', newline='') as csvfile:
                            writer= csv.writer(csvfile, delimiter='|')
                            products = amazon.search(Keywords=row[0], SearchIndex='All')
                            for i, product in enumerate(products):
                                print(row[1], product) 
                                writer.writerow([product])
                                break
                    except Exception as e:
                        print(e)
                        continue
    except Exception as e:
        print(e)
        continue
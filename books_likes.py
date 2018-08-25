import json
import csv
import requests
from time import sleep
with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\Scraped_Data.json', 'r') as f:
    datastore = json.load(f)
for data in datastore['friends']['data']:
    try:
        print(data['name'])
        Name = data['name']
        with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\books.json'.format(data['name']), 'r') as f:
            datas= json.load(f)
            with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\{0}\\favorite_books_desc.csv'.format(Name), 'w', newline='') as csvfile:
                    writer= csv.writer(csvfile, delimiter='|')
                    for iter in datas['data']:
                        try:
                            print(iter['name'])
                            json_response_data = requests.get('https://www.googleapis.com/books/v1/volumes?q={0}&key=AIzaSyDo0RdbSrTxgQZ7-k94w-cx8FvGuRJxSGk'.format(iter['name']))
                            print(json_response_data.json()['items'][0]['volumeInfo']['title'])
                            print(json_response_data.json()['items'][0]['volumeInfo']['authors'][0])
                            writer.writerow([json_response_data.json()['items'][0]['volumeInfo']['title'], json_response_data.json()['items'][0]['volumeInfo']['authors'][0]])
                            sleep(2)
                        except Exception as e:
                            print(e)
                
    except:
        print("No.. Failed Here")
        continue
    print()

import facebook
import json
token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
graph = facebook.GraphAPI(access_token=token, version = 2.7)
events = graph.request("/me?fields=id,friends{name,birthday,about,favorite_athletes,favorite_teams,likes{about,name,category,description},gender,books{name,about,genre},groups,movies{about,name,artists_we_like},music{name,id,artists_we_like},inspirational_people,posts{with_tags,message,is_popular},events{name,description,start_time},sports},gender")
with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\Scraped_Data.json', 'w') as f:
    json.dump(events, f)

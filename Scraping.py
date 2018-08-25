import facebook
import json
token = 'EAACEdEose0cBAIofFityZAtAb7CxTbtUORCsTAVCUvJYgwl3nNnOjdZB1mIUYZCO9LYYtZBvqBampqhV4vKf9yaXuXntefd8OqUrZB8Q8WeGVpNGrTIjCPQKCjyCaRx3T02IwAOhfMO3vqiKbFObqacIN59Ec0vsLpkzyFEMGLW5Ue9kG8YP1ZClAqHkZAZAeGcZD'
graph = facebook.GraphAPI(access_token=token, version = 2.7)
events = graph.request("/me?fields=id,friends{name,birthday,about,favorite_athletes,favorite_teams,likes{about,name,category,description},gender,books{name,about,genre},groups,movies{about,name,artists_we_like},music{name,id,artists_we_like},inspirational_people,posts{with_tags,message,is_popular},events{name,description,start_time},sports},gender")
with open('C:\\Users\\AshwinAmbal\\Desktop\\SDL Lab\\Scraped_Data.json', 'w') as f:
    json.dump(events, f)
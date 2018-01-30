import facebook
import requests
import csv

from secrets import secrets

access_token = secrets["access_token"]
user_id = secrets["user_id"]
pages = []

with open('pages.csv', 'r') as pagefile:
    pagereader = csv.reader(pagefile, delimiter=',')

    for row in pagereader:
        pages.append(row[0])

graph = facebook.GraphAPI(access_token)

for page in pages:
    posts = graph.get_connections(page, 'feed')

    print(posts)

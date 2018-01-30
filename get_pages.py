import facebook
import requests
import csv

from datetime import datetime
from secrets import secrets

access_token = secrets["access_token"]
user_id = secrets["user_id"]
pages = []

# previous_time = 0
next_time = 100

with open('pages.csv', 'r') as pagefile:
    pagereader = csv.reader(pagefile, delimiter=',')

    for row in pagereader:
        pages.append(row[0])

graph = facebook.GraphAPI(access_token)

for page in pages:
    posts = graph.get_connections(page, 'feed')
    posts = posts["data"]

    for post in posts:
        time_posted = datetime.strptime(post["created_time"], '%Y-%m-%dT%H:%M:%S%z')
        mili_time = time_posted.timestamp() * 1000

        print(mili_time)

#Step 1: import the data

import feedparser;
NewsFeed = feedparser.parse("https://www.lemonde.fr/climat/rss_full.xml");
print (NewsFeed);

#Step 2: make a summary of the data

import requests
r = requests.post(
    "https://api.deepai.org/api/summarization",
    data={
        'text':'https://www.lemonde.fr/climat/rss_full.xml',
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())
#Step 3: put the data into a word doc


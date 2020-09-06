#Step 1: import the data


#Step 2: make a summary of the data

import requests
r = requests.post(
    "https://api.deepai.org/api/summarization",
    data={
        'text':'https://www.lemonde.fr/climat/rss_full.xml',
    },
    headers={'api-key': 'fdc4c55f-4078-4730-a681-534cda607471'}
)

print(r.json());

text = str(r.json());

#Step 3: put the data into a txt file

fh = open ('ccscraping.txt','w');
fh.write(text);
fh.close();

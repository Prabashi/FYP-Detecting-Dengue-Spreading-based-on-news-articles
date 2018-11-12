import feedparser

# RSS feed url
url = 'http://www.dailynews.lk/rss.xml'
feed = feedparser.parse(url)

entries = feed['entries']
no_entries = len(entries)

entry_keys = entries[0].keys()
articles = []
for entry in entries:
    articles.append({
        'Title': entry['title'],
        'Date': entry['published'],
        'Article_content': entry['summary'],
    })

import re
TAG_RE=re.compile(r'<[^>]+>')



for article in articles:
    article_content = article['Article_content']
    pure_content=TAG_RE.sub('',article_content)
    article['Article_content']=pure_content

import csv
with open('Test_dataset.csv',mode='w') as csv_file:
    fieldnames=['Title','Date','Article_content']
    writer=csv.DictWriter(csv_file,fieldnames=fieldnames)

    writer.writeheader()
    for article in articles:
        writer.writerow({'Title':article['Title'],'Date':article['Date'],'Article_content':article['Article_content']})

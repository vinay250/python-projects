import json
with open('articles.json') as json_file:
    data = json.load(json_file)
for article in data['articles']:
    title = article['title']
    author = article['author']
    date = article['date']
    content = article['content']
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Date: {date}")
    print(f"Content: {content}")
    print()

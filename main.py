import requests
api_key = "78721f510cf549659a101e33ea091825"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-07-21&" \
"sortBy=publishedAt&apiKey=78721f510cf549659a101e33ea091825"

# Make a request
request = requests.get(url)

# Create a dictionary/list with JSON
content = request.json()

# Access the article titles and descriptions with a loop that goes through all the articles
for article in content["articles"]:
    print(article["title"])
    print(article["descriptions"])
import requests
from datetime import datetime, timedelta

# Put the date time of today
today = datetime.now()

# Convert the number of the day that we got to a string in the URL
#today.strftime("%Y-%m-%d") (just a test)

# Includes the last 7 days, putting today less the seven days with timedelta
seven_days_before = today - timedelta(days=7)

# Convert the number of the seven days that we got to a string in the URL
api_date = seven_days_before.strftime("%Y-%m-%d")

api_key = "78721f510cf549659a101e33ea091825"
url = f"https://newsapi.org/v2/everything?q=tesla&from={api_date}&" \
"sortBy=publishedAt&apiKey=78721f510cf549659a101e33ea091825"

# Make a request
request = requests.get(url)

# Create a dictionary/list with JSON
content = request.json()

email_body = ""

# Access the article titles, descriptions and url with a loop that 
# goes through all the articles, and enumerate them to organize
for i, article in enumerate(content["articles"], 1):
    title = article.get("title", "(no title)")
    description = article.get("description", "(no description)")
    url = article.get("url", "")

    email_body += f"{i}. {title}\n {description}\n {url}\n"
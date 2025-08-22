import requests
from datetime import datetime, timedelta
from email_sender import send_email

# Put the date time of today
today = datetime.now()

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
for i, article in enumerate(content["articles"][:10], 1):
    title = article.get("title", "(no title)")
    description = article.get("description", "(no description)")
    url = article.get("url", "")

    email_body += f"{i}. {title}\n{description}\n{url}\n\n"

# Add subject and the message (email_body) to put in the function
subject = "Tesla News of the Week"
message = f"Subject: {subject}\n\n{email_body}\n"

# Encode in UTF-8 to handle special characters correctly
message = message.encode("utf-8")

send_email(message)
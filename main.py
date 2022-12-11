import requests
from send_email import send_email

topic = "tesla"

api_key = "f05e41a0cdea4fc3a43b13f75fc53d92"
url = "https://newsapi.org/v2/everything?"\
    f"q={topic}&"\
    "from=2022-11-11&"\
    "sortBy=publishedAt&"\
    "apiKey=f05e41a0cdea4fc3a43b13f75fc53d92&"\
    "language=en"

# Make Request
request = requests.get(url)

# Get a Dictionary with Data
content = request.json()
print(content)
# Access the Article titles and description
body = ""
print(type(body))
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" \
               + article["description"] + "\n" + article["url"] + "\n\n"

body = body.encode("utf-8")
send_email(body)

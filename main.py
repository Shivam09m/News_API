import requests

api_key = "f05e41a0cdea4fc3a43b13f75fc53d92"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "from=2022-11-11&sortBy=publishedAt&apiKey=" \
    "f05e41a0cdea4fc3a43b13f75fc53d92"

# Make Request
request = requests.get(url)

# Get a Dictionary with Data
content = request.json()

# Access the Article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

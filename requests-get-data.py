import requests

username = "apify" # github username
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url)
print(user_data.json())
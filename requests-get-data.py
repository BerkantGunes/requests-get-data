import requests

username = "YOUR GITHUB USERNAME"
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url)
print(user_data.json())

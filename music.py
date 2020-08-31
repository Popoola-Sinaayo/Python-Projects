import requests
import json
res = requests.get("https://github.com/jesseward/discogs-oauth-example")

print(res.json())

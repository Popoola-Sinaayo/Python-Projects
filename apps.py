import requests
import json
res = requests.get("http://api.fungenerators.com/fact/fod/categories")

ans = res.json()

print(ans)

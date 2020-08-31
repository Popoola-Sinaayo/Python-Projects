import requests


res = requests.get("https://cat-facts.herokuapp.com/facts")

print(res.status_code)

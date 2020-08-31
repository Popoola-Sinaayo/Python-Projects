import requests

#res = requests.get("https://gateway.marvel.com")
#433/v1/public/characters?apikey=e14291a7ea40ad3a82bd126eba5b813fc068aa0")
#res0 = requests.get("https://www.google.com")
#ponse = res.json()


joke = requests.get("https://api.imgflip.com/get_memes")

jokes = joke.json()

koke = jokes["data"]["data.memes"]

print(jokes)

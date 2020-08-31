import requests

url = "https://andruxnet-random-famous-quotes.p.rapidapi.com/" 
querystring = {"cat":"famous","count":"10"}
headers = { 'x-rapidapi-host': "andruxnet-random-famous-quotes.p.rapidapi.com", 'x-rapidapi-key': "351aae87c6msh0f6ae2b86eb073bp177906jsnc8f99495783d" }
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)

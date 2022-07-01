import requests
import pandas
import pprint
import json

url = "https://wger.de/api/v2/meal/"
api_key = "de6e9a9ac86a5514d8fc9b7fd0b406382282d0fe"
# response = requests.get(url)

# data = response.json()

# pprint.pprint(data)

data = {"key": "value"}

headers = {"Authorization": f"Token {api_key}"}

r = requests.get(url=url, data=data, headers=headers)


data= r.json()

print(data)

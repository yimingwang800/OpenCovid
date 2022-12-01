import json, requests

url = 'https://api.opencovid.ca/summary'
response = requests.get(url)
print(response.text)
json_data = json.loads(response.text) #? data is JSON object
print(json_data)
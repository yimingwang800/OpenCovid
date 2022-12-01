import json, requests

url = 'https://api.opencovid.ca/summary'
response = requests.get(url)
json_data = json.loads(response.text) #? data is JSON object

with open("Covid Data.json", "w") as import_file:  
   import_file.write(response.text)
# with open("Covid Data.json", "w") as import_file:  
#    import_file.write(json.dumps(json_data))

# print(response.text['data'][0]['region'])
# print(json_data['data'][0]['date'])
# {
#     "data": [
#         {
#             "region": "AB",
#             "date": "2022-10-13",
#             "cases": 610027.0,

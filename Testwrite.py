import json, requests

url = 'https://api.opencovid.ca/summary'
response = requests.get(url)
#print(response.text)
json_data = json.loads(response.text) #? data is JSON object
#json_file = json.dumps(json_data, indent=1)

#for data in json_data["data"]:
    #print(f'{data["region"]}, {data["date"]}, {data["cases"]}')

with open("Cases.csv", "a") as w_file: 
    w_file.write("Region, Cases\n")
    for data in json_data["data"]:
        w_file.write(f'{data["region"]}, {data["cases"]} \n')
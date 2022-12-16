import json, requests, pandas, matplotlib
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://api.opencovid.ca/summary'
response = requests.get(url)
#print(response.text)
json_data = json.loads(response.text) #? data is JSON object
#print(json_data)

with open("Cases.csv", "a") as w_file: 
    w_file.write("Region, Cases\n")
    for data in json_data["data"]:
        w_file.write(f'{data["region"]}, {data["cases"]} \n')


df = pd.read_csv('Cases.csv')
print(df)

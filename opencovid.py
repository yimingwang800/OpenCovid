import json, requests, pandas, matplotlib
import pandas as pd
import matplotlib.pyplot as plt

def thousands(x, pos):
    return f'{x:,.0f}'

def millions(x, pos):
    #return f'{x/1000000:,}'
    return '{:,}'.format(x/1000000)

def region_summary():
    df = pd.read_csv('Cases.csv')
    print(df)

    ax = df.plot.bar(
        x='Region',
        #y='Cases',
        rot=45,
        legend=False
    )
    ax.set_title('Cases by Region', fontsize=16)
    ax.set_xlabel('Region', fontsize=14)
    ax.set_ylabel('Cases (Million)', fontsize=14)
    #ax.yaxis.set_major_formatter(thousands)
    ax.yaxis.set_major_formatter(millions)

    plt.show()

def region(province):
    url = 'https://api.opencovid.ca/timeseries'
    response = requests.get(url)
    data = json.loads(response.text)
    df = pd.read_json(json.dumps(data['data']['cases']))
    print(df)

    # ax = df.query('region == "AB"').plot(
    #     x='date',
    #     y='value',
    #     rot=45,
    # )
    ax = df.query(f'region == "{province}"').plot(
        x='date',
        y='value',
        rot=45,
        legend = False
    )
    ax.set_title('Cases in Province', fontsize=16)
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Cases (Million)', fontsize=14)
    ax.yaxis.set_major_formatter(thousands)
    #ax.yaxis.set_major_formatter(millions)
    plt.show()


#region_summary()
region(province = "QC")
#region("AB")

 
# url = 'https://api.opencovid.ca/summary'
# response = requests.get(url)
# #print(response.text)
# json_data = json.loads(response.text) #? data is JSON object
# # print(json_data)

# with open("Cases.csv", "a") as w_file: 
#     w_file.write("Region, Cases\n")
#     for data in json_data["data"]:
#         w_file.write(f'{data["region"]}, {data["cases"]} \n')




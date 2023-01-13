import json, requests, pandas, matplotlib
import pandas as pd
import matplotlib.pyplot as plt

def millions(x, pos):
    #return f'{x/1000000:,}'
    return '{:,}'.format(x/1000000)

def population():
    # with open("Population.csv", "a") as w_file: 
    #     w_file.write("Province, Population\n")

    df = pd.read_csv('Population.csv')
    print(df)

    ax = df.plot.bar(
        x='Province',
        y='Population',
        rot=45,
        legend=False
    )
    ax.set_title('Population of Provinces', fontsize=16)
    ax.set_xlabel('Provinces', fontsize=14)
    ax.set_ylabel('Population (Million)', fontsize=14)
    # ax.yaxis.set_major_formatter(thousands)
    ax.yaxis.set_major_formatter(millions)

    plt.show()

population()
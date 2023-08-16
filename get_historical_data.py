import pandas as pd
import numpy as np
from urllib.request import urlopen
import urllib.error
import json
import datetime

odata = {}
while True:
    print("Si desea detener el programa, escriba 'None'")
    moneda = input("Pone la moneda: ")
    if moneda == 'None':
        break
    try:
        url = f'https://api.coingecko.com/api/v3/coins/{moneda}/market_chart?vs_currency=usd&days=max&interval=daily&precision=12'
        response = urlopen(url)
        data = json.loads(response.read())
        df = pd.DataFrame(data)
        df['dates'] = [x[0] for x in df['prices']]
        df['dates'] = df['dates'].apply(lambda x: x / 1000)
        df['dates'] = df['dates'].apply(lambda x: datetime.datetime.utcfromtimestamp(x))
        df['prices'] = [x[1] for x in df['prices']]
        df['market_caps'] = [x[1] for x in df['market_caps']]
        df['total_volumes'] = [x[1] for x in df['total_volumes']]
        odata[f'{moneda}'] = {'dates' : list(df['dates']),
                            'prices': list(df['prices']),
                            'market_caps': (df['market_caps']),
                            'total_volumes': list(df['total_volumes'])}
    except urllib.error.HTTPError as e:
        print(f"HTTPError {e.code}: {e.reason}")
        print("La moneda no se encuentra. Intente nuevamente")

df = pd.DataFrame(odata).T
df.to_csv("./data/csv/historical_data.csv", index= True)
print("Se ha exportado correctamente la data.")
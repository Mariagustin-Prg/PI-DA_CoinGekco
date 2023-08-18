import time
import streamlit as st
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import json
from urllib.request import urlopen
import urllib.error
from datetime import datetime

df = pd.read_csv("./data/csv/data_market_.csv")

def randomColor(): 
    clr = '#'
    for t in range(0,6):
        lista = ['a', 'b', 'c', 2, 1, 3, 4, 5, 6, 7, 8, 9, 0]
        rand = np.random.randint(0, 13, 1)
        s = lista[rand[0]]
        clr = clr + str(s)
    return clr


st.title("Criptomonedas.")

st.markdown("En esta pestaña podremos acceder a diferentes tablas donde muestren los datos de las criptomonedas.")

st.subheader("Criptomonedas con mayor capitalización.")

df.dropna(subset= 'market_cap_rank', inplace= True)

df['ath_date'] = pd.to_datetime(df['ath_date'])
df['last_updated'] = pd.to_datetime(df['last_updated'])
df.loc[95, 'atl_date'] = "2023-03-10T05:05:00.000Z"
df['atl_date'] = pd.to_datetime(df['atl_date'])


df.rename(columns= {
    'id': 'ID',
    'symbol': 'Abreviación',
    'name': 'Nombre',
    'image': 'Imagen',
    'current_price': 'Precio Actual',
    'market_cap': 'Capitalización del mercado',
    'market_cap_rank': 'Ranking en capitalización del mercado',
    'fully_diluted_valuation': 'Valoración diluida de la moneda',
    'total_volume': 'Volumen total de transacciones',
    'high_24h': 'Precio más alto en 24 horas',
    'low_24h': 'Precio más bajo en 24 horas',
    'price_change_24h': 'Cambio del precio en 24 horas',
    'price_change_percentage_24h': 'Cambio porcentual del precio en 24 horas',
    'market_cap_change_24h': 'Cambio de la capitalización en 24 horas',
    'market_cap_change_percentage_24h': 'Cambio porcentual de la capitalización en 24 horas',
    'circulating_supply': 'Cantidad de unidades en circulación',
    'total_supply': 'Cantidad total de unidades disponibles',
    'max_supply': 'Máximo de unidades que se crearon',
    'ath': 'Precio histórico más alto',
    'ath_change_percentage':'Cambio porcentual respecto al máximo histórico',
    'ath_date':'Fecha del precio histórico más alto',
    'atl':'Mínimo Histórico',
    'atl_change_percentage': 'Cambio porcentual respecto al mínimo histórico',
    'atl_date': 'Fecha del precio mínimo histórico',
    'last_updated': 'Última actualización',
    'price_change_percentage_1y_in_currency': 'Cambio porcentual del precio en un año',
    'price_change_percentage_30d_in_currency': 'Cambio porcentual del precio en 30 días'
}, inplace= True)
df.drop(columns= ['roi', 'price_change_percentage_24h_in_currency', 'Imagen'], inplace= True) 

st.dataframe(df)
st.markdown("``Puede clickear en las columnas para ordenar``")
st.markdown("***")
st.markdown("A continuación, tiene la posibilidad de ver todos los datos de la moneda que usted busque. Por ejemplo: Pepe.")


coin = st.text_input("Inserte el nombre de la moneda que desea buscar:")
info_to_show_1 = df[df['Nombre'] == coin]

st.dataframe(info_to_show_1)
button = False
prices = False
capt = False
volume = False
valid = False
if info_to_show_1.shape[0] == 1:
    button = st.checkbox("Mostrar distintos gráficos de la Criptomoneda")
    sym = info_to_show_1.iloc[0,0]
    valid = True


if valid is True:
    while True:
        try:
            # st.text(f"{sym}")
            url = f'https://api.coingecko.com/api/v3/coins/{sym}/market_chart?vs_currency=usd&days=max&precision=18'
            response = urlopen(url)
            data = json.loads(response.read())
            h_df = pd.DataFrame(data)

            h_df['dates'] = [x[0] for x in h_df['prices']]
            h_df['dates'] = h_df['dates'].apply(lambda x: x / 1000)
            h_df['dates'] = h_df['dates'].apply(lambda x: datetime.utcfromtimestamp(x))
            h_df['prices'] = [x[1] for x in h_df['prices']]
            h_df['market_caps'] = [x[1] for x in h_df['market_caps']]
            h_df['total_volumes'] = [x[1] for x in h_df['total_volumes']]
            h_df['years'] = h_df['dates'].apply(lambda x: x.year)
            d_min = h_df['years'].min()
            d_max = h_df['years'].max()

            break
        except urllib.error.URLError as e:
            st.markdown("No se obtuvo la información buscada.")
            st.write(f"URLError {e}")
            time.sleep(5)

color1= randomColor()
color2= randomColor()
color3= randomColor()

if button:
    options = st.radio("Seleccione el gráfico que desea observar:", ("", "Precios", "Capitalización", "Volumen de transacciones"))
    
else:
    options = ""

if options == "Precios":
    sns.set(style='darkgrid')
    fig = plt.figure(figsize= (8,6))
    plt.plot(h_df['dates'], h_df['prices'], label= coin, color= color1)
    plt.title(F"Precios históricos de {coin}")
    
    plt.legend()
    
    st.pyplot(fig)

elif options == "Capitalización":
    sns.set(style='darkgrid')
    fig = plt.figure(figsize= (8,6))
    plt.plot(h_df['dates'], h_df['market_caps'], label= coin, color= color2)
    plt.title(f"Capitalización de {coin}")
   
    plt.legend()
    
    st.pyplot(fig)

elif options == "Volumen de transacciones":
    sns.set(style='darkgrid')
    fig = plt.figure(figsize= (14,6))
    plt.plot(h_df['dates'], h_df['total_volumes'], label= coin, color= color3)
    plt.yscale("log")
    plt.legend()
    plt.title("Volumen total de transacciones en el tiempo")
    
    st.pyplot(fig)
    st.markdown("``PD: El eje Y se encuentra en escala logarítmica.``")
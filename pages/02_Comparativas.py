import time
import datetime
import pandas as pd
import numpy as np
from urllib.request import urlopen
from urllib.error import HTTPError
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style= 'darkgrid')

def randomColor(): 
    clr = '#'
    for t in range(0,6):
        lista = ['a', 'b', 'c', 'd', 'e','f', 2, 1, 3, 4, 5, 6, 7, 8, 9, 0]
        rand = np.random.randint(0, 16, 1)
        s = lista[rand[0]]
        clr = clr + str(s)
    return clr

st.title("Comparativas")
st.markdown("***")
st.markdown("En esta pestaña podemos hacer la comparación de las caraterísticas de dos o hasta tres monedas.")

df = pd.read_csv("data\csv\data_market_.csv")

search_coin = st.text_input("Barra de búsqueda:")

searching = df[df['name'].str.contains(search_coin, case=False, na=False)]
if searching.shape[0] < 10:
    st.dataframe(searching)
else:
    st.dataframe(searching.head(10))

st.markdown("``La barra de búsqueda mustra los primeros diez resultados.``")

select = st.radio("Por favor, seleccione la cantidad de monedas que quieras comparar:", ("Dos monedas", "Tres monedas"), horizontal= True)


coin_1 = False
coin_2 = False
coin_3 = False

if select == "Dos monedas":
    coin_1 = st.text_input("Indique la primera moneda:")
    coin_2 = st.text_input("Indique la segunda moneda:")

else:
    coin_1 = st.text_input("Indique la primera moneda:")
    coin_2 = st.text_input("Indique la segunda moneda:")
    coin_3 = st.text_input("Indique la tercer moneda:")

df_c1 = df[df['name'] == coin_1]
df_c2 = df[df['name'] == coin_2]
df_c3 = df[df['name'] == coin_3]

sel = st.selectbox("Seleccione que comparación desea hacer:",
                     ("", "Precio", "Capitalización", "Ranking en el mercado", "Volumen de transacciones", "Cambio porcentual del precio en 24 horas", "Circulación de la monedas", "Precios máximo y mínimo alcanzado", "Cambio porcentual del precio en un año"))
if select == "Dos monedas":
    if sel == "Precio":
        mode = st.radio("Cómo desea visualizar el precio?", ("Barras horizontales", "Columnas", "Tabla"))
        fig = plt.figure(figsize=(10,3))
        if mode == "Barras horizontales":    
            plt.barh([coin_1, coin_2], [float(df_c1.current_price.values), float(df_c2.current_price.values)], color= ['r', 'g'])
            plt.xticks(rotation= 90)
            plt.legend()
            st.pyplot(fig)
        
        if mode == "Columnas":
            plt.bar([coin_1, coin_2], [float(df_c1.current_price.values), float(df_c2.current_price.values)], color= ['r', 'g'])
            plt.legend()
            st.pyplot(fig)

        if mode == "Tabla":
            dicc = pd.DataFrame(data= {
                f"{coin_1}": {"Precio": df_c1.loc[:,'current_price'].values},
                f"{coin_2}": {"Precio": df_c2.loc[:,'current_price'].values}
            })
            st.dataframe(dicc)

    elif sel == "Capitalización":
        mode = st.radio("Como desea visualizar el gráfico?", ("Barras horizontales", "Tabla"))
        if mode == "Barras horizontales":
            fig = plt.figure(figsize=(10,4))
            plt.barh([coin_1, coin_2], [float(df_c1.market_cap.values), float(df_c2.market_cap.values)], color= ['r', 'g'])
            plt.xscale("symlog")
            plt.legend()
            st.pyplot(fig)

        else:
            dicc = pd.DataFrame(data= {
                f"{coin_1}": {"Precio": df_c1.loc[:,'market_cap'].values},
                f"{coin_2}": {"Precio": df_c2.loc[:,'market_cap'].values}
            })
            st.dataframe(dicc)

    elif sel == "Ranking en el mercado":
        st.table({
            f"{coin_1}": {"N° en el ranking":int(df_c1.market_cap_rank.values)},
            f"{coin_2}": {"N° en el ranking":int(df_c2.market_cap_rank.values)},
            })
        
    elif sel == "Volumen de transacciones":
        mode = st.radio("Como desea visualizar los datos?", ("Barras", "Tabla"), horizontal= True)
        if mode == "Barras":
            fig = plt.figure(figsize=(12,5))
            plt.barh([coin_1, coin_2], [int(df_c1['total_volume'].values), int(df_c2['total_volume'].values)], color= ['r', 'g'])
            plt.xscale("symlog")
            st.pyplot(fig)

        else:
            st.table({
                f"{coin_1}": {"Volumen": int(df_c1['total_volume'].values)},
                f"{coin_2}": {"Volumen": int(df_c2['total_volume'].values)}
            })

    elif sel == "Cambio porcentual del precio en 24 horas":
        dicc = {
            f"{coin_1}" : {
                "Precio de hoy": int(df_c1.current_price.values),
                "Precio de ayer": (100 - float(df_c1.price_change_percentage_24h.values)) * int(df_c1.current_price.values) / 100,
                "Cambio porcentual": float(df_c1.price_change_percentage_24h.values),
                "Cambio nominal": float(df_c1.price_change_24h.values)
            },
            f"{coin_2}": {
                "Precio de hoy": int(df_c2.current_price.values),
                "Precio de ayer": (100 - float(df_c2.price_change_percentage_24h.values)) * int(df_c2.current_price.values) / 100,
                "Cambio porcentual": float(df_c2.price_change_percentage_24h.values),
                "Cambio nominal": float(df_c2.price_change_24h.values)
            }
        }
        st.table(dicc)

    elif sel == "Circulación de la monedas":
        dicc = {
            f"{coin_1}": {
                "En circulación" : float(df_c1.circulating_supply.values),
                "Cantidad de monedas en el mercado": float(df_c1.total_supply.values),
                "Cantidad máxima de unidades que pueden existir": float(df_c1.max_supply.values)
            },
            f"{coin_2}": {
                "En circulación" : float(df_c2.circulating_supply.values),
                "Cantidad de monedas en el mercado": float(df_c2.total_supply.values),
                "Cantidad máxima de unidades que pueden existir": float(df_c2.max_supply.values)
            }
        }

        st.dataframe(dicc)

    elif sel == "Precios máximo y mínimo alcanzado":
        mode = st.radio("", ("Máximo", "Mínimo"), horizontal= True)

        if mode == "Máximo":
            dicc = {
                f"{coin_1}" : {
                    "Precio máximo": float(df_c1.ath.values),
                    "Fecha": pd.to_datetime(df_c1['ath_date'].values).date[0],
                    "Cambio nominal" : float(int(df_c1['current_price']) - float(df_c1['ath_change_percentage'].values)),
                    "Precio Actual": float(df_c1.current_price.values)
                },
                f"{coin_2}" : {
                    "Precio máximo": float(df_c2.ath.values),
                    "Fecha": pd.to_datetime(df_c2['ath_date'].values).date[0],
                    "Cambio nominal" : float(int(df_c2['current_price']) - float(df_c2['ath_change_percentage'].values)),
                    "Precio Actual": float(df_c2.current_price.values)
                }
            }
            st.dataframe(dicc)
        if mode == "Mínimo":
            dicc = {
                f"{coin_1}" : {
                    "Precio máximo": float(df_c1.atl.values),
                    "Fecha": pd.to_datetime(df_c1['atl_date'].values).date[0],
                    "Cambio nominal" : float(int(df_c1['current_price']) - float(df_c1['atl_change_percentage'].values)),
                    "Precio Actual": float(df_c1.current_price.values)
                },
                f"{coin_2}" : {
                    "Precio máximo": float(df_c2.atl.values),
                    "Fecha": pd.to_datetime(df_c2['atl_date'].values).date[0],
                    "Cambio nominal" : float(int(df_c2['current_price']) - float(df_c2['atl_change_percentage'].values)),
                    "Precio Actual": float(df_c2.current_price.values)
                }
            }
            st.dataframe(dicc)


    elif sel == "Cambio porcentual del precio en un año":
        dicc = {
            f"{coin_1}" : {
                "Precio de hace un año": float(100 * float(df_c1['current_price'].values) / (100 - float(df_c1['price_change_percentage_1y_in_currency'].values))),
                "Cambio porcentual": float(df_c1['price_change_percentage_1y_in_currency'].values),
                "Cambio Real": float(df_c1['current_price'].values) - float(100 * float(df_c1['current_price'].values) / (100 - float(df_c1['price_change_percentage_1y_in_currency'].values))),
                "Precio actual": float(df_c1['current_price'].values)
            },
            f"{coin_2}" : {
                "Precio de hace un año": float(100 * float(df_c2['current_price'].values) / (100 - float(df_c2['price_change_percentage_1y_in_currency'].values))),
                "Cambio porcentual": float(df_c2['price_change_percentage_1y_in_currency'].values),
                "Cambio Real": float(df_c2['current_price'].values) - float(100 * float(df_c2['current_price'].values) / (100 - float(df_c2['price_change_percentage_1y_in_currency'].values))),
                "Precio actual": float(df_c2['current_price'].values)
            }
        }

        st.dataframe(dicc)

if select == "Tres monedas":
    if sel == "Precio":
        mode1 = st.radio("Cómo desea visualizar el precio?", ("Barras horizontales", "Columnas", "Tabla"))
        fig = plt.figure(figsize=(10,3))
        if mode1 == "Barras horizontales":    
            plt.barh([coin_1, coin_2, coin_3], [float(df_c1.current_price.values), float(df_c2.current_price.values), float(df_c3.current_price.values)], color= ['r', 'g', '#03a1Fd'])
            plt.xticks(rotation= 90)
            plt.legend()
            st.pyplot(fig)
        
        if mode1 == "Columnas":
            plt.bar([coin_1, coin_2, coin_3], [float(df_c1.current_price.values), float(df_c2.current_price.values), float(df_c3.current_price.values)], color= ['r', 'g', '#03a1Fd'])
            plt.legend()
            st.pyplot(fig)

        if mode1 == "Tabla":
            dicc = pd.DataFrame(data= {
                f"{coin_1}": {"Precio": df_c1.loc[:,'current_price'].values},
                f"{coin_2}": {"Precio": df_c2.loc[:,'current_price'].values},
                f"{coin_3}": {"Precio": df_c3.loc[:,'current_price'].values}
            })
            st.dataframe(dicc)

    elif sel == "Capitalización":
        mode1 = st.radio("Como desea visualizar el gráfico?", ("Barras horizontales", "Tabla"))
        if mode1 == "Barras horizontales":
            fig = plt.figure(figsize=(10,4))
            plt.barh([coin_1, coin_2, coin_3], [float(df_c1.market_cap.values), float(df_c2.market_cap.values), float(df_c3['market_cap'].values)], color= ['r', 'g', '#03a1Fd'])
            plt.xscale("symlog")
            plt.legend()
            st.pyplot(fig)

        else:
            dicc = pd.DataFrame(data= {
                f"{coin_1}": {"Precio": df_c1.loc[:,'market_cap'].values},
                f"{coin_2}": {"Precio": df_c2.loc[:,'market_cap'].values},
                f"{coin_3}": {"Precio": df_c3.loc[:,'market_cap'].values}
            })
            st.dataframe(dicc)

    elif sel == "Ranking en el mercado":
        st.table({
            f"{coin_1}": {"N° en el ranking":int(df_c1.market_cap_rank.values)},
            f"{coin_2}": {"N° en el ranking":int(df_c2.market_cap_rank.values)},
            f"{coin_3}": {"N° en el ranking":int(df_c3.market_cap_rank.values)}
            
            })
        
    elif sel == "Volumen de transacciones":
        mode1 = st.radio("Como desea visualizar los datos?", ("Barras", "Tabla"), horizontal= True)
        if mode1 == "Barras":
            fig = plt.figure(figsize=(12,5))
            plt.barh([coin_1, coin_2, coin_3], [int(df_c1['total_volume'].values), int(df_c2['total_volume'].values), int(df_c3['total_volume'].values)], color= ['r', 'g', '#03a1Fd'])
            plt.xscale("symlog")
            st.pyplot(fig)

        else:
            st.table({
                f"{coin_1}": {"Volumen": int(df_c1['total_volume'].values)},
                f"{coin_2}": {"Volumen": int(df_c2['total_volume'].values)},
                f"{coin_3}": {"Volumen": int(df_c3['total_volume'].values)}
            })

    elif sel == "Cambio porcentual del precio en 24 horas":
        dicc = {
            f"{coin_1}" : {
                "Precio de hoy": int(df_c1.current_price.values),
                "Precio de ayer": (100 - float(df_c1.price_change_percentage_24h.values)) * int(df_c1.current_price.values) / 100,
                "Cambio porcentual": float(df_c1.price_change_percentage_24h.values),
                "Cambio nominal": float(df_c1.price_change_24h.values)
            },
            f"{coin_2}": {
                "Precio de hoy": int(df_c2.current_price.values),
                "Precio de ayer": (100 - float(df_c2.price_change_percentage_24h.values)) * int(df_c2.current_price.values) / 100,
                "Cambio porcentual": float(df_c2.price_change_percentage_24h.values),
                "Cambio nominal": float(df_c2.price_change_24h.values)
            },
            f"{coin_3}": {
                "Precio de hoy": int(df_c3.current_price.values),
                "Precio de ayer": (100 - float(df_c3.price_change_percentage_24h.values)) * int(df_c3.current_price.values) / 100,
                "Cambio porcentual": float(df_c3.price_change_percentage_24h.values),
                "Cambio nominal": float(df_c3.price_change_24h.values)
            }
        }
        st.table(dicc)

    elif sel == "Circulación de la monedas":
        dicc = {
            f"{coin_1}": {
                "En circulación" : float(df_c1.circulating_supply.values),
                "Cantidad de monedas en el mercado": float(df_c1.total_supply.values),
                "Cantidad máxima de unidades que pueden existir": float(df_c1.max_supply.values)
            },
            f"{coin_2}": {
                "En circulación" : float(df_c2.circulating_supply.values),
                "Cantidad de monedas en el mercado": float(df_c2.total_supply.values),
                "Cantidad máxima de unidades que pueden existir": float(df_c2.max_supply.values)
            },
            f"{coin_3}": {
                "En circulación" : float(df_c3.circulating_supply.values),
                "Cantidad de monedas en el mercado": float(df_c3.total_supply.values),
                "Cantidad máxima de unidades que pueden existir": float(df_c3.max_supply.values)
            }
        }

        st.dataframe(dicc)
        st.markdown("``De no existir una cantidad máxima de las unidades que pueden existir, siginifica que esa cantidad está indefinida.``")

    elif sel == "Precios máximo y mínimo alcanzado":
        mode1 = st.radio("", ("Máximo", "Mínimo"), horizontal= True)

        if mode1 == "Máximo":
            dicc = {
                f"{coin_1}" : {
                    "Precio máximo": float(df_c1.ath.values),
                    "Fecha": pd.to_datetime(df_c1['ath_date'].values).date[0],
                    "Cambio nominal" : float(int(df_c1['current_price']) - float(df_c1['ath_change_percentage'].values)),
                    "Precio Actual": float(df_c1.current_price.values)
                },
                f"{coin_2}" : {
                    "Precio máximo": float(df_c2.ath.values),
                    "Fecha": pd.to_datetime(df_c2['ath_date'].values).date[0],
                    "Cambio nominal" : float(int(df_c2['current_price']) - float(df_c2['ath_change_percentage'].values)),
                    "Precio Actual": float(df_c2.current_price.values)
                },
                f"{coin_3}" : {
                    "Precio máximo": float(df_c3.ath.values),
                    "Fecha": pd.to_datetime(df_c3['ath_date'].values).date[0],
                    "Cambio nominal" : float(int(df_c3['current_price']) - float(df_c3['ath_change_percentage'].values)),
                    "Precio Actual": float(df_c3.current_price.values)
                }
            }
            st.dataframe(dicc)

        if mode1 == "Mínimo":
            dicc = {
                f"{coin_1}" : {
                    "Precio máximo": float(df_c1.atl.values),
                    "Fecha": pd.to_datetime(df_c1['atl_date'].values).date[0],
                    "Cambio nominal" : float(int(df_c1['current_price']) - float(df_c1['atl_change_percentage'].values)),
                    "Precio Actual": float(df_c1.current_price.values)
                
                },
                f"{coin_2}" : {
                    "Precio máximo": float(df_c2.atl.values),
                    "Fecha": pd.to_datetime(df_c2['atl_date'].values).date[0],
                    "Cambio nominal" : float(int(df_c2['current_price']) - float(df_c2['atl_change_percentage'].values)),
                    "Precio Actual": float(df_c2.current_price.values)
                },
                f"{coin_3}" : {
                    "Precio máximo": float(df_c3.atl.values),
                    "Fecha": pd.to_datetime(df_c3['atl_date'].values).date[0],
                    "Cambio nominal" : float(int(df_c3['current_price']) - float(df_c3['atl_change_percentage'].values)),
                    "Precio Actual": float(df_c3.current_price.values)
                }
            }
            st.dataframe(dicc)

    elif sel == "Cambio porcentual del precio en un año":
        dicc = {
            f"{coin_1}" : {
                "Precio de hace un año": float(100 * float(df_c1['current_price'].values) / (100 - float(df_c1['price_change_percentage_1y_in_currency'].values))),
                "Cambio porcentual": float(df_c1['price_change_percentage_1y_in_currency'].values),
                "Cambio Real": float(df_c1['current_price'].values) - float(100 * float(df_c1['current_price'].values) / (100 - float(df_c1['price_change_percentage_1y_in_currency'].values))),
                "Precio actual": float(df_c1['current_price'].values)
            },
            f"{coin_2}" : {
                "Precio de hace un año": float(100 * float(df_c2['current_price'].values) / (100 - float(df_c2['price_change_percentage_1y_in_currency'].values))),
                "Cambio porcentual": float(df_c2['price_change_percentage_1y_in_currency'].values),
                "Cambio Real": float(df_c2['current_price'].values) - float(100 * float(df_c2['current_price'].values) / (100 - float(df_c2['price_change_percentage_1y_in_currency'].values))),
                "Precio actual": float(df_c2['current_price'].values)
            },
            f"{coin_3}" : {
                "Precio de hace un año": float(100 * float(df_c3['current_price'].values) / (100 - float(df_c3['price_change_percentage_1y_in_currency'].values))),
                "Cambio porcentual": float(df_c3['price_change_percentage_1y_in_currency'].values),
                "Cambio Real": float(df_c3['current_price'].values) - float(100 * float(df_c3['current_price'].values) / (100 - float(df_c3['price_change_percentage_1y_in_currency'].values))),
                "Precio actual": float(df_c3['current_price'].values)
            }
        }

        st.dataframe(dicc)
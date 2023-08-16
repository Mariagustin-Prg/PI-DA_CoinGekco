import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./data/csv/data_market_.csv")

st.title("Criptomonedas.")

st.markdown("En esta pestaña podremos acceder a diferentes tablas donde muestren los datos de las criptomonedas.")

st.subheader("Criptomonedas con mayor capitalización.")

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
    'ath':'Fecha del precio histórico más alto',
    'atl':'Mínimo Histórico',
    'atl_change_percentage': 'Cambio porcentual respecto al mínimo histórico',
    'atl_date': 'Fecha del precio mínimo histórico',
    'last_updated': 'Última actualización',
    'price_change_percentage_1y_in_currency': 'Cambio porcentual del precio en un año',
    'price_change_percentage_30d_in_currency': 'Cambio porcentual del precio en 30 días'
}, inplace= True)
df.drop(columns= ['roi', 'price_change_percentage_24h_in_currency'], inplace= True) 

st.dataframe(df)
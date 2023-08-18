import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Análisis de CoinGekco")

st.markdown("***")
st.markdown("## Introducción.")

st.markdown("```Acceda a las pestañas dentro de la barra lateral para acceder a las visualizaciones y a los datos.```")

st.sidebar.markdown("")

st.image('https://th.bing.com/th/id/R.76c3f3cfcb2ff29bc6089c894fc2d26a?rik=3qDTrvcIMz6eKw&pid=ImgRaw&r=0')

st.markdown("CoinGecko es una plataforma con la que podemos obtener información financiera respecto al mercado cripto. Incluyendo las criptosmonedas, los NFT y datos sobre empresas públicas.")

st.markdown("Dentro de la pestaña lateral, puedes acceder a visualizaciones, tablas y distintas formas de representar los datos en diferentes formatos de gráficos.")

st.image('https://th.bing.com/th/id/OIP.Rx3Hde5bC1j7LcidwfpwwAHaEy?pid=ImgDet&rs=1')
st.markdown("Podemos tener acceso a esta página a través del siguiente [link](https://www.coingecko.com/).")


st.header("¿Qué son las criptomonedas?")
st.markdown("Las criptomonedas son activos digitales descentralizados que utilizan criptografía para garantizar la seguridad de las transacciones y controlar la creación de nuevas unidades. La más conocida es el Bitcoin, pero existen miles de criptomonedas diferentes, cada una con sus características únicas. Estas monedas digitales se basan en la tecnología blockchain, que es un registro público y transparente de todas las transacciones que han tenido lugar. A través de la criptografía y la descentralización, las criptomonedas permiten transacciones directas entre participantes sin necesidad de intermediarios, como bancos. Además, han dado lugar a la posibilidad de crear contratos inteligentes y aplicaciones descentralizadas, abriendo nuevas vías para la innovación en diversos sectores.")
st.markdown("La economía cripto engloba el conjunto de actividades económicas que giran en torno a las criptomonedas y la tecnología blockchain. Esta economía incluye aspectos como la minería de criptomonedas, donde se utilizan poderosos ordenadores para validar transacciones y añadirlas al blockchain, recibiendo recompensas en forma de criptomonedas. También implica la inversión y el comercio de criptomonedas en plataformas de intercambio, con la esperanza de obtener ganancias a través de la volatilidad de los precios. Además, la economía cripto involucra el desarrollo de proyectos basados en blockchain, como aplicaciones descentralizadas y tokens que representan activos digitales específicos. A medida que esta economía evoluciona, se plantean desafíos y oportunidades en términos de regulación, adopción masiva y exploración de casos de uso innovadores.")
st.markdown("Si bien la economía cripto ha demostrado un gran potencial para transformar la forma en que interactuamos con el dinero y los sistemas financieros, también enfrenta críticas y preocupaciones en áreas como la seguridad, la volatilidad extrema de los precios y posibles usos ilegítimos. A medida que gobiernos y reguladores de todo el mundo evalúan cómo abordar esta nueva forma de intercambio de valor, la economía cripto continúa expandiéndose e influyendo en la forma en que concebimos y participamos en transacciones económicas y financieras.")

st.header("Nueva economía tecnológica")
st.markdown("Las nuevas economías, incluida la economía cripto, están intrínsecamente relacionadas con la ciberseguridad. La tecnología blockchain y las criptomonedas presentan desafíos y oportunidades en términos de seguridad digital.")

st.subheader("*Seguridad de las transacciones*:")
st.markdown("La tecnología blockchain, en la que se basan las criptomonedas, se destaca por su seguridad debido a la criptografía y a su naturaleza descentralizada.")
st.markdown("Sin embargo, también es crucial garantizar que las transacciones y las billeteras digitales estén protegidas contra ataques cibernéticos como el robo de claves privadas o la manipulación de transacciones.")
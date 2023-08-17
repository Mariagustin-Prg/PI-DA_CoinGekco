# PI-DA_CoinGekco
## *Data Analysis*

---

En este proyecto se procedió a hacer un análisis profundo de la página de [CoinGekco](https://www.coingecko.com/). Analizando los datos que tienen sobre la economía de las criptomonedas.

<img src= "https://th.bing.com/th/id/OIP.Reg5uBu6n8dtWNWi2R6PLQHaEK?pid=ImgDet&rs=1" height= 200>
En este repositorio podrá encontrar diversos archivos de interés que usted podrá usar para hacer su propio análisis.

## **Contenido**
[Instalación](##instalación)
[Uso](##uso)
[Página Interactiva](##página_interactiva)

## Instalación
Para poder tener los archivos que este repositorio almacena, en tu propia computadora puedes seguir los siguientes pasos:

*Antes que nada, debes tener instalado Git Bash en tu PC. En caso de no tener Git Bash instalado, clickea en el [**_link_**](https://git-scm.com/downloads).*
1. Ahora, dentro de git bash, debes navegar dentro de los archivos de tu PC para acceder a la carpeta donde quieras clonar el repositorio:
```
cd c/Escritorio/Carpeta
```
Puedes usar ``cd carpeta`` para navegar en las distintas carpetas, y para poder ver donde te encuentras navegando puedes usar el comando ``pwd``.

2. Una vez te encuentres dentro de la carpeta en la que quieras almacenar de forma local el repositorio, ejecuta el siguiente comando en la terminal:
```
git clone https://github.com/Marigustin-Prg/PI-DA_CoinGekco.git
```

_Para obtener más información de los comandos de Git Bash, acceda al siguiente [link](https://git-scm.com/doc)._

Antes de poder acceder a todos las herramientas y poder trabajar con el archivo, ejecute este comando dentro del terminal y dentro de la carpeta con el repo:
```
pip install -r requirements.py
```
---

## Uso
Dentro del archivo *Exploratory Data Analysis.ipynb* encontrarán el análisis completo de este proyecto con los datos del día 8 de agosto del 2023. Para obtener los datos más recientes, usted puede ejecutar en un terminal de comandos los archivos *get_market_data.py* y *get_historical_data.py*. 
Dentro de la carpeta con el repositorio, ejecute los siguiente comando y siga las instrucciones:
```
py get_market_data.py
py get_historical_data.py
```

Con esos datos, usted podrá probar y analizar los datos más recientes junto al [Análisis Exploratorio de los datos](Exploratory_Data_Analysis.ipynb) del repositorio.

---
## Página interactiva
Dentro de los múltiples archivos que existen en el repo, está el [dashboard interactivo](Menu_Principal.py), el cuál, junto con la librería Streamlit, se pueden intereactuar con diversos gráficos y tablas para obtener visualizaciones que te ayuden a entender el mercado de las criptomonedas.

Para ejecutarlo en forma local y hacerle modificaciones al mismo timepo, ejecute dentro de la terminal:
```
streamlit run Menu_Principal.py

```
Para acceder a él de forma virtual, está deployada en [Streamlit Cloud]().

---
## Contacto
Para poder comunicarse conmigo, puede hacerlo a través de:

<img src="https://th.bing.com/th/id/R.79309b751fc01736ea1cc3d786b25651?rik=rurHNX620eLm%2fA&pid=ImgRaw&r=0" width=25>[GitHub](https://github.com/Mariagustin-Prg)

<img src="https://th.bing.com/th/id/R.4d6db56fe0851ae7635b0dfd1cd86a72?rik=KvTVJFIPxj8oIQ&pid=ImgRaw&r=0" width=15>[Mail](mariagustin.prog@gmail.com)

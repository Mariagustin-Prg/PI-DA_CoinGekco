print("Iniciando ejecutable...")
import time
time.sleep(2)
print("--------------------------------------------------------------")
print("Bienvenido al ejecutable del Repositorio de Análisis de CoinGekco.")
time.sleep(2)
print("Este archivo les brindará el archivo 'data_market_.csv' con la información más reciente de CoinGekco.")
print("--------------------------------------------------------------")
time.sleep(2)


# Creamos una lista que reciba los datos de la API.
data_list = []

print("Importando librerías...")
import pandas as pd
import json
import urllib.error
from urllib.request import urlopen
print("Librerías importadas.")
time.sleep(2)

print("La API de CoinGekco brinda los datos en bloques/páginas de 250 monedas.")
print("La API de CoinGekco tiene 10000 monedas. La cantidad máxima de páginas permitidas es 40. Ejemplo: '11'")
n_max = input("Indique la cantidad de páginas que desea obtener:")
n_max = int(n_max)
if n_max > 40: n_max = 40
print("")
time.sleep(2)

print("Iniciando la solicitud de las páginas a la API de CoinGekco")
for n_page in range(1, n_max + 1):
    attemps = 0
    max_attemps = 3
    backoff_factor = 5
    attemps_f = 0
    while True:
        time.sleep(20)
        print("")
        print(f"Solicitando la página N°{n_page}. Intento N°{attemps + 1}")
        try:
            url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=1250&page={str(n_page)}&sparkline=false&price_change_percentage=24h%2C30d%2C1y&locale=en&precision=9"
            response = urlopen(url)
            data = json.loads(response.read())
            data_list.extend(data)
            print(f"Página N°{n_page} agregada.")
            print("Próxima solicitud en 20 segundos...")
            break
        except urllib.error.HTTPError as e:
            print(f"HTTPError ({e.code}): {e.reason}")
            if attemps <= max_attemps:
                attemps += 1
                print("Esperando una respuesta del servidor...")
                print("Reintento en 30 segundos...")
                
            else:
                print("Último intento en 90 segundos...")
                time.sleep(30)
                print("")
                print("Último intento en 60 segundos...")
                time.sleep(30)
                print("")
                print("Último intento en 30 segundos...")
                
                print("")
                attemps_f += 1

            if attemps_f == 1:
                attemps = 0
                attemps_f = 0
                print(f"No se ha podido obtener respuesta de la API para la página {n_page}...")
                print("Pasando a la próxima página...")
                print("---> ---> ---> ---> ---> ---> ---> ---> ---> ---> ---> --->")
                break

        except TimeoutError:
            print ("TimeoutError")

        except urllib.error.URLError as r:
            print(f"URLError ({r.code}): {r.reason}")
            break

df = pd.DataFrame(data_list)
df.to_csv("data_market_.csv", index= False)
print("Archivo exportado: 'data_market_.csv'")
print(f"Cantidad de datos obtenidos: {df.shape[0]}.")
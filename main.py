import requests
#1. configurar la url de la API para la revision de moneda
url= "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,cardano&vs_currencies=usd,mxn"
#2.peticion HTTP a la API de CoinGecko
res= requests.get(url)
#3. validacion de la respuesta HTTP 200 = OK
if res.status_code == 200:
    datos = res.json()
    #Extraccion de la seccion del monedas seleccionadas a JSON
    print(f"El precio de Ethereum en dolares es: {datos['ethereum']['usd']}") 
     #4. impresion de los datos necesarios en consola
else:
    print("Error al conectar:", res.status_code)
import requests
#1. configurar la url de la API para la revision de moneda
url= "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,cardano&vs_currencies=usd,mxn"
#2.peticion HTTP a la API de CoinGecko
res= requests.get(url)
#3. validacion de la respuesta HTTP 200 = OK
if res.status_code == 200:
    datos = res.json()
    #Extraccion de la seccion del monedas seleccionadas a JSON
    moneda = input("¿Qué criptomoneda quieres consultar? (bitcoin/ethereum/cardano): ").lower()
    #agreamos que el usuario pueda escoger la moneda de su interes
    divisa = input("¿En qué divisa lo quieres ver? (usd/mxn): ").lower()
    if moneda in datos:
        #con este if hacemos que no haya error por escribir algo fuera del rango
     #4. impresion de los datos necesarios en consola
        if divisa in datos[moneda]:
            print(f"El precio de {moneda} en {divisa.upper()} es: {datos[moneda][divisa]}")
    else:
        print("Erro al escribir, vuelve a intentarlo")
        #en caso de escribir mal saldra este mensaje
else:
    print("Error al conectar:", res.status_code)
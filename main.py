import requests

# 1. Configurar la URL de la API para la revisión de moneda
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,cardano&vs_currencies=usd,mxn"

# 2. Petición HTTP a la API de CoinGecko
res = requests.get(url)

# 3. Validación de la respuesta HTTP 200 = OK
if res.status_code == 200:
    datos = res.json()
    
    # Entrada de datos por parte del usuario
    moneda = input("¿Qué criptomoneda quieres consultar? (bitcoin/ethereum/cardano): ").lower()
    divisa = input("¿En qué divisa lo quieres ver? (usd/mxn): ").lower()
    
    # Validar si la criptomoneda existe en el JSON
    if moneda in datos:
        # Validar si la divisa existe dentro de esa criptomoneda
        if divisa in datos[moneda]:
            # 4. Impresión del precio dinámico en consola
            precio = datos[moneda][divisa]
            # Formateamos 'precio' con comas y 2 decimales (:,.2f)
            print(f"El precio de {moneda} en {divisa.upper()} es: ${precio:,.2f}")
        else:
            print("Divisa no encontrada (solo usd o mxn). Vuelve a intentarlo.")
    else:
        print("Criptomoneda no encontrada en la lista. Vuelve a intentarlo.")
else:
    print("Error al conectar:", res.status_code)
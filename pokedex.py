import requests


def extraer_habilidades(datos):
    habilidades = []
    for habilidad in datos["abilities"]:
        habilidades.append(habilidad["ability"]["name"])
    return habilidades


def extraer_tipos(datos):
    tipos = []
    for tipo in datos["types"]:
        tipos.append(tipo["type"]["name"])
    return tipos


def extraer_peso(datos):
    peso = datos["weight"]
    return peso


def formato_peso(peso_formato):
    peso_kg = peso_formato / 100
    peso_formateado = "{:.2f} KG".format(peso_kg)
    return peso_formateado


def llamar_api(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()

        print("has ingresado los datos del pokemon " + pokemon.capitalize())

        tipos = extraer_tipos(datos)
        print("los tipos de", pokemon.capitalize() + " son " + ":", tipos)

        peso = extraer_peso(datos)
        peso_formateado = formato_peso(peso)

        print(pokemon.capitalize() + " Pesa " +
              ":", peso_formateado)

        habilidades = extraer_habilidades(datos)
        print(pokemon.capitalize() +
              " posee las sigueintes habilidades " + ":", habilidades)

    except requests.exceptions.RequestException as e:
        print("Error al llamar a la API:", e)


if __name__ == "__main__":
    pokemon = input("Por favor ingresa un Pokemon: ")
    llamar_api(pokemon)



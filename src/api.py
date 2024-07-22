# https://realpython.com/python-requests/
# pip install requests
import requests

# https://rickandmortyapi.com/documentation/#character-schema
url  = "https://rickandmortyapi.com/api/character"

data = requests.get(url)

if data: # data.status_code == 200:
    print(data)

    data = data.json()
    personajes = data["results"]

    for personaje in personajes:
        print(
            personaje["name"],
            personaje["species"],
            personaje["gender"],
            sep = ", "
            )
else:
    # https://developer.mozilla.org/es/docs/Web/HTTP/Status
    print("Error:", data.status_code)
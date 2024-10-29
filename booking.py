import requests

# Claves de acceso
key = #Tukey
token = #Tutoken

# ID del tablero que deseas actualizar
board_id = #boardId

# URL para actualizar el tablero
url = f'https://api.trello.com/1/boards/{board_id}?key={key}&token={token}'

# Datos que deseas actualizar (por ejemplo, el nombre y la descripción)
update_data = {
    "name": "TestTable",
    "desc": "TestDescription"
}

# Haciendo la solicitud PUT para actualizar el tablero
response = requests.put(url, json=update_data)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    try:
        # Intentar obtener el JSON de la respuesta
        data = response.json()

        # Confirmar que la respuesta contiene los datos actualizados
        if data.get('name') == update_data['name'] and data.get('desc') == update_data['desc']:
            print(f"Tablero actualizado correctamente. Nombre: {data['name']}, Descripción: {data['desc']}")
        else:
            print("Código 200 recibido, pero los datos no fueron actualizados correctamente.")
            print("Respuesta del servidor:", data)

    except ValueError:
        # Esto captura el error si la respuesta no es JSON válido
        print("Código 200 recibido, pero la respuesta no es JSON válido.")
else:
    print(f"Error al hacer la solicitud: Código de estado {response.status_code}")

# import json
# from types import SimpleNamespace
# import requests

# response = requests.get("https://github.com/rxaviersantos")
# resultado = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))

# print(resultado.name)
# print(resultado.company)
# print(resultado.login+"meu nome é "+ resultado.name)


import requests
import json
from types import SimpleNamespace


username = 'seu_nome_de_usuário'
url = f'https://api.github.com/users/{username}'
response = requests.get(url)


if response.status_code == 200:
    try:
      
        resultado = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
        print(resultado.name)
        print(resultado.company)
        print(resultado.login + " meu nome é " + resultado.name)
    except json.decoder.JSONDecodeError:
        print("Erro: Resposta não é um JSON válido.")
else:
    print(f"Erro na requisição. Código de status: {response.status_code}")

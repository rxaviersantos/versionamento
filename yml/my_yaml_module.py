import yaml
import json

# Carregar dados do arquivo YAML
with open('config.yml', 'r') as file:
    configuration = yaml.safe_load(file)

# Escrever dados em um arquivo JSON
with open('config.json', 'w') as json_file:
    json.dump(configuration, json_file, indent=2)

# Ler dados do arquivo JSON e imprimir formatado
with open('config.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    output = json.dumps(loaded_data, indent=2)
    print(output)

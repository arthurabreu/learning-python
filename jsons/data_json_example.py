import json
from zipfile import Path

# JSON string similar to the image
data_json = '''
{
  "assinantes": [
    {
      "nome": "Adriano Soares",
      "telefone": "51 999999999",
      "email": "adriano@email.com",
      "em_dia": true
    },
    {
      "nome": "Juliano Faccioni",
      "telefone": "51 999999998",
      "email": "juliano@email.com",
      "em_dia": false
    }
  ]
}
'''

# parse and pretty-print
obj = json.loads(data_json)
print(json.dumps(obj, indent=2, ensure_ascii=False))

# convertendo para dicionario
data_converted = json.loads(data_json)
print(data_converted)
print('Type: ' + str(type(data_converted))) # Type: <class 'dict'>

# acessando dados
print('Nome do primeiro assinante: ' + data_converted['assinantes'][0]['nome'])
print('Telefone do primeiro assinante: ' + data_converted['assinantes'][0]['telefone'])
print('Email do primeiro assinante: ' + data_converted['assinantes'][0]['email'])
print('Está em dia? ' + str(data_converted['assinantes'][0]['em_dia']))
print('---')
print('---')

# acessando todos os assinantes
for assinante in data_converted['assinantes']:
    print('Nome: ' + assinante['nome'])
    print('Telefone: ' + assinante['telefone'])
    print('Email: ' + assinante['email'])
    print('Está em dia? ' + str(assinante['em_dia']))
    print('---')
    print('---')

# convertendo de volta para JSON
data_json_converted = json.dumps(data_converted, ensure_ascii=False)
print(data_json_converted)

# lendo arquivos json
# write JSON file first (in the same folder as the script)
DATA_FILE = Path(__file__).parent / 'data.json'
with DATA_FILE.open('w', encoding='utf-8') as file:
    json.dump(data_converted, file, ensure_ascii=False, indent=2)
    print('---')
    print('---')


# now safely read the file back
with DATA_FILE.open('r', encoding='utf-8') as file:
    data_loaded = json.load(file)
    print(data_loaded)
    print('---')
    print('---')


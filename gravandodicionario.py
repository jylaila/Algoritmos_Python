import json

cadastro = {
    'nome': 'Camila Ap. Santos',
    'idade': 30,
    'telefone': '11-3333-3333'
    }
open('cadastro.json','w').write(json.dumps(cadastro))

with open('cadastro.json', 'r') as file_json:
    dados = json.loads(file_json.read())

print(dados)
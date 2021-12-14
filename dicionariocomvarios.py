import json

cadastro = []
dados={'nome':'Carla', 'idade':13, 'telefone':11-3333-3333}
cadastro.append(dados)
dados={'nome':'Daniel', 'idade':30, 'telefone':11-4444-3333}
cadastro.append(dados)
dados={'nome':'Antonio', 'idade':57, 'telefone':11-5555-3333}
cadastro.append(dados)

open('cadastro.json','w').write(json.dumps(cadastro))

try:
    with open('cadastro.json', 'r') as file_json:
        dados = json.loads(file_json.read())
except IOError:
    print("Arquivo não encontrado!")

print(dados)#imprime todos os dados
print(dados[0]['nome']) #imprime o primeiro nome do dicionário




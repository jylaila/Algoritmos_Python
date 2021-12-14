import os
import json

estoqueProdutos=[]
opcaoPrincipal = 0
opcaoEstoque = 4
opcaoLista = 4

#Menu Principal
def menuPrincipal():
    print ("## ESTOQUE DE PRODUTOS ##\n")
    print ("1. CADASTRO DE PRODUTOS")
    print ("2. PESQUISAR PRODUTOS")
    print ("3. ENTRADA/SAÍDA DE PRODUTOS")
    print ("4. LISTAR PRODUTOS")
    print ("5. SAIR")

#Menu Cadastro Produto
def menuCadastro():
    print ("## CADASTRO DE PRODUTOS ##\n")
    print ("1. CADASTRAR PRODUTO")
    print ("2. REMOVER PRODUTO")
    print ("3. ALTERAR PRODUTO")
    print ("4. MENU PRINCIPAL")

#Menu Pesquisar Produto
def menuPesquisa():
    print ("## PESQUISA DE PRODUTOS ##\n")
    print ("1. PESQUISAR POR NOME")
    print ("2. PESQUISAR POR CÓDIGO")
    print ("3. MENU PRINCIPAL")

#Menu Entrada/Saída de Produtos
def menuEstoque():
    print ("## ENTRADA E SAÍDA DE PRODUTOS ##\n")
    print ("1. ENTRADA DE PRODUTO")
    print ("2. SAÍDA DE PRODUTO")
    print ("3. MENU PRINCIPAL")

#Menu Listar Produto
def menuLista():
    print ("## LISTA DE PRODUTOS ##\n")
    print ("1. LISTAR POR NOME")
    print ("2. LISTAR POR CÓDIGO")
    print ("3. MENU PRINCIPAL")

#Função Cadastro de Produto
def cadastro():
    produto = input("Nome do produto: ").strip()
    codigo = int(input("Código do Produto: "))
    quantidade = int(input("Quantidade: "))
    produtoFinal = {'produto':produto, 'codigo':codigo, 'quantidade':quantidade}
    verificarCodigo(codigo, estoqueProdutos, produtoFinal)

    return

#Função Verificar Código
def verificarCodigo(codigo, estoqueProdutos, produtoFinal):
    codigoValido = True
    for x in range(len(estoqueProdutos)):
        if estoqueProdutos[x]['codigo'] == codigo:
          print("\nCódigo já cadastrado!!\n")  
          codigoValido = False
          break

    if codigoValido:
      estoqueProdutos.append(produtoFinal)
      gravarArquivo(estoqueProdutos)
      print("\nProduto Cadastrado com sucesso!!\n")

    return

#Função Remover Produto
def remover(produto, estoque):
    removerProdutos = False
    for x in range(len(estoque)):
        if estoque[x]['produto'] == produto:
            removerProduto = x
            removerProdutos = True
            break

    if removerProdutos:
      del estoque[removerProduto]
      print('\nProduto %s removido!\n' % (produto))
      gravarArquivo(estoque)
    
    else:
      print("\nProduto não encontrado!!\n ")

    return estoque

#Função Alterar Produto
def alterar(produto, estoque):
    alterarProduto = False
    alterarProdutos = False
    for x in range(len(estoque)):
        if estoque[x]['produto'] == produto:
            alterarProduto = x
            alterarProdutos = True
            break

    if alterarProdutos:
      produto = input('Digite o novo nome do produto: ')
      codigo = int(input('Digite o novo código do produto: '))
      quantidade = int(input('Digite a nova quantidade do produto: '))
      produtoAlterado = {'produto':produto, 'codigo':codigo, 'quantidade':quantidade}
      verificarAlterar(produto, codigo, quantidade, alterarProduto, produtoAlterado, estoque)
      #gravarArquivo(estoque)

    else:
      print("\nProduto não encontrado!!\n")

    return estoque

#Função Verificar Código Alterar
def verificarAlterar(produto, codigo, quantidade, alterarProduto, produtoAlterado, estoque):
    codigoValido = True
    for x in range(len(estoqueProdutos)):
        if estoqueProdutos[x]['codigo'] == codigo:
          print("\nCódigo já cadastrado!!\n")  
          codigoValido = False
          break

    if codigoValido:
      estoque[alterarProduto]['produto'] = produto
      estoque[alterarProduto]['codigo'] = codigo
      estoque[alterarProduto]['quantidade'] = quantidade
      print('\nProduto %s alterado!\n' % estoque[alterarProduto])
      gravarArquivo(estoque)

    return


#Função Pesquisar Nome
def pesquisaNome(produto, estoque):
    for x in range(len(estoque)):
        if estoque[x]['produto'] == produto:
            print('\nProduto: %s - Código: %s - Quantidade: %s\n' % (estoque[x]['produto'], estoque[x]['codigo'], estoque[x]['quantidade']))
            NaoEncontrou = False
            break
        else:
            NaoEncontrou = True

    if NaoEncontrou:
        print('\nProduto %s não encontrado!\n' % (produto))

#Função Pesquisar Código
def pesquisaCodigo(codigo, estoque):
    for x in range(len(estoque)):
        if estoque[x]['codigo'] == codigo:
            print('\nProduto: %s - Código: %s - Quantidade: %s\n' % (estoque[x]['produto'], estoque[x]['codigo'], estoque[x]['quantidade']))
            NaoEncontrou = False
            break
        else:
            NaoEncontrou = True

    if NaoEncontrou:
        print('\nCódigo %s não encontrado!\n' % (codigo))

#Função Entrada Produto
def entradaProduto(produto, estoque):
    reporProduto = False
    reporProdutos = False
    for x in range(len(estoque)):
        if estoque[x]['produto'] == produto:
            reporProduto = x
            reporProdutos = True
            break

    if reporProdutos:
      estoque[reporProduto]['quantidade'] += int(input('Digite a quantidade de %s que deseja abastecer: ' % estoque[reporProduto]['produto']))
      print('\nProduto %s abastecido!\n' % estoque[reporProduto])
      gravarArquivo(estoque)

    else:
      print("\nProduto não encontrado!!\n")

    return estoque

#Função Saída Produto
def saidaProduto(produto, estoque):
    retirarProduto = False
    retirarProdutos = False
    for x in range(len(estoque)):
        if estoque[x]['produto'] == produto:
            retirarProduto = x
            retirarProdutos = True
            break

    if retirarProdutos:
      quantidadeAtual = estoque[retirarProduto]['quantidade']  
      quantidadeRetirada = int(input('Digite a quantidade de %s que deseja retirar: ' % estoque[retirarProduto]['produto']))
      quantidadeFinal = quantidadeAtual - quantidadeRetirada
      if quantidadeFinal < 0:
        print("\nProduto em estoque não pode ficar negativo!!\n")

      else:
        estoque[retirarProduto]['quantidade'] -= quantidadeRetirada
        print('\nProduto %s retirado!\n' % estoque[retirarProduto])
        gravarArquivo(estoque)

    else:
      print("\nProduto não encontrado!!\n")

    return estoque

#Função Listar Por nome
def listaNome():
    print ("PRODUTOS CADASTRADOS\n")
    for x in range(len(estoqueProdutos)):
        estoqueProdutos.sort(key=lambda item: item.get("produto"))
        print('Produto: %s - Código: %s - Quantidade: %s\n' % (estoqueProdutos[x]['produto'], estoqueProdutos[x]['codigo'], estoqueProdutos[x]['quantidade']))

#Função Listar Por Código
def listaCodigo():
    print ("PRODUTOS CADASTRADOS\n")
    for x in range(len(estoqueProdutos)):
        estoqueProdutos.sort(key=lambda item: item.get("codigo"))
        print('Código: %s - Produto: %s - Quantidade: %s\n' % (estoqueProdutos[x]['codigo'], estoqueProdutos[x]['produto'], estoqueProdutos[x]['quantidade']))

#Função Gravar Arquivo
def gravarArquivo(produtos):
    with open('estoque_produtos.json', 'w') as json_file:
        json.dump(produtos, json_file, indent=4)

    json_file.close()

#Função Carregar Arquivo
def carregarEstoqueProdutos():
    with open('estoque_produtos.json', 'r') as json_file:
        estoque = json.load(json_file)

    json_file.close()

    return estoque

try:
    estoqueProdutos = carregarEstoqueProdutos()
except IOError:
    print('O arquivo estoque_produtos.json não foi encontrado!!\n')

#Função Menu Cadastro
def cadastroMenu(estoqueProdutos):
  opcaoCadastro = 0
  while opcaoCadastro != 4:
      menuCadastro()
      opcaoCadastro = int(input("\nSelecione uma opção: "))
      os.system('clear')

      if opcaoCadastro == 4:
          gravarArquivo(estoqueProdutos)
          break
      elif opcaoCadastro == 1:
          cadastro()
      elif opcaoCadastro == 2:
          estoqueProdutos = (remover(str(input("Digite o nome do produto que deseja remover: ")), estoqueProdutos))
      elif opcaoCadastro == 3:
          estoqueProdutos = (alterar(str(input("Digite o nome do produto que deseja alterar: ")), estoqueProdutos))
      else:
          opcaoCadastro = 0
          print("\nOpção Inválida!!\n\n")

#Função Menu Pesquisa
def pesquisaMenu(estoqueProdutos):
  opcaoPesquisa = 0  
  while opcaoPesquisa != 3:
      menuPesquisa()
      opcaoPesquisa = int(input("\nSelecione uma opção: "))
      os.system('clear')

      if opcaoPesquisa == 3:
          gravarArquivo(estoqueProdutos)
          break
      elif opcaoPesquisa == 1:
          pesquisaNome(str(input("Digite o nome do produto que deseja buscar: ")), estoqueProdutos)
          opcaoPesquisa = 0
      elif opcaoPesquisa == 2:
          pesquisaCodigo(int(input("Digite o código do produto que deseja buscar: ")), estoqueProdutos)
          opcaoPesquisa = 0
      else:
          opcaoPesquisa = 0
          print("\nOpção Inválida!!\n\n")

#Função Menu Controle de Produtos
def estoqueMenu(estoqueProdutos):
  opcaoEstoque = 0
  while opcaoEstoque != 3:
      menuEstoque()
      opcaoEstoque = int(input("\nSelecione uma opção: "))
      os.system('clear')

      if opcaoEstoque == 3:
          gravarArquivo(estoqueProdutos)
          break
      elif opcaoEstoque == 1:
          entradaProduto(str(input("Digite o nome do produto que deseja repor: ")), estoqueProdutos)
      elif opcaoEstoque == 2:
          saidaProduto(str(input("Digite o nome do produto que deseja retirar: ")), estoqueProdutos)
      else:
          opcaoEstoque = 0
          print("\nOpção Inválida!!\n\n")

#Função Menu Lista
def listaMenu(estoqueProdutos):
  opcaoLista = 0
  while opcaoLista != 3:
      menuLista()
      opcaoLista = int(input("\nSelecione uma opção: "))
      os.system('clear')

      if opcaoLista == 3:
          gravarArquivo(estoqueProdutos)
          break
      elif opcaoLista == 1:
          listaNome()
      elif opcaoLista == 2:
          listaCodigo()
      else:
          opcaoLista = 0
          print("\nOpção Inválida!!\n\n")

#Função Menu Principal
while opcaoPrincipal != 5:
    menuPrincipal()
    opcaoPrincipal = int(input("\nSelecione uma opção: "))
    os.system('clear')

    if opcaoPrincipal == 5:
        gravarArquivo(estoqueProdutos)
        break
    elif opcaoPrincipal == 1:
        cadastroMenu(estoqueProdutos)
    elif opcaoPrincipal == 2:
        pesquisaMenu(estoqueProdutos)
    elif opcaoPrincipal == 3:
        estoqueMenu(estoqueProdutos)
    elif opcaoPrincipal == 4:
        listaMenu(estoqueProdutos)
    else:
        opcaoPrincipal = 0
        print("\nOpção Inválida!!\n\n")
#VisualG
# nome:caractere
# sobrenome:caractere
#leia(nome,sobrenome)
# escreval("Nome ", nome, "Sobrenome ", sobrenome)
#em python

nome = input("Digite o nome ")
sobrenome = input ("Digite o sobrenome ")
#1ª forma
print("Nome", nome, "Sobrenome ", sobrenome)

#2ª forma - + usada quando precisamos converter tipos
print("Nome %s Sobrenome %s" % (nome, sobrenome))

#3ª forma
print("Nome " + str(nome)+ "Sobrenome " + str(sobrenome))

#4ª forma
print("Nome {} Sobrenome {}".format(nome, sobrenome))
print("Nome {0} Sobrenome {1}".format(nome, sobrenome))
print("Nome {nome1} Sobrenome {sobrenome1}".format(nome1 = nome, sobrenome1=sobrenome))

#alinha a esquerda com 8 espaços
#saiba mais https://pyformat.info/#string_pad_align
print("Nome {:>8} Sobrenome {}".format(nome, sobrenome))


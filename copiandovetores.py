frutas = ["Maça", "Pêra", "Uva"]
frutas2 = frutas[:]

frutas = ["Pêra", "Uva", "Banana"]

frutas3 = frutas + frutas2

frutas.append("Uva") #adiciona no final
frutas.insert(1, "Cacau")#adiciona em posição especifica

print(frutas.index("Uva"))

# print(sorted(frutas))
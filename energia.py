tipoIns = input("Tipo: ")
tipoIns = tipoIns.upper() #converter para maiusculo
# tipoIns = tipoIns.lower() #converter para minusculo

kwh = float (input("Kwh: "))
valor = 0

if kwh > 0:
    if tipoIns == 'R':
        if kwh <=500:
            valor = kwh * 0.40
        else:
            valor = kwh * 0.65
    elif tipoIns == 'C':
        if kwh <=1000:
            valor = kwh * 0.55
        else:
            valor = kwh * 0.60
    elif tipoIns == 'I':
        if kwh <=5000:
            valor = kwh * 0.55
        else:
            valor = kwh * 0.60
    else:
        print("Tipo Inexistente")
else:
    print("Informe kwh válido")

print("Valor a pagar %.2f" %valor)
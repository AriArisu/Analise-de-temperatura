temperatura = [[],[]]
umidade = [[],[]]
precipitacao = [[],[]]

alertas = 0

temp = int(input("Digite a temperatura: "))
temperatura[0].append(temp)

umi = int(input("Digite a umidade: "))
umidade[0].append(umi)

pre = int(input("Digite a precipitação: "))
precipitacao[0].append(pre)

if temp >= 40 or temp <= 5:
    print("Alerta de temperatura crítica!")
    alertas += 1
else:
    print("Valores normais")

if umi <= 20 or umi >= 95:
    print("Alerta de umidade crítica!")
    alertas += 1
else:
    print("Valores normais")

if pre >= 80:
    print("Alerta de risco de enchente!")
    alertas += 1
else:
    print("Valores normais")

opcao = input("Deseja fazer a análise completa de temperaturas das últimas duas semanas? ").lower()

if opcao == "sim":
    while len(temperatura[0]) < 5:
        temp = int(input(f"Digite a temperatura para a semana 1, dia {len(temperatura[0])+1}: "))
        temperatura[0].append(temp)

    for i in range(5):
        temp = int(input(f"Digite a temperatura para a semana 2, dia {i+1}: "))
        temperatura[1].append(temp)

    while len(umidade[0]) < 5:
        umi = int(input(f"Digite a umidade para a semana 1, dia {len(umidade[0])+1}: "))
        umidade[0].append(umi)

    for i in range(5):
        umi = int(input(f"Digite a umidade para a semana 2, dia {i+1}: "))
        umidade[1].append(umi)

    while len(precipitacao[0]) < 5:
        pre = int(input(f"Digite a precipitação para a semana 1, dia {len(precipitacao[0])+1}: "))
        precipitacao[0].append(pre)

    for i in range(5):
        pre = int(input(f"Digite a precipitação para a semana 2, dia {i+1}: "))
        precipitacao[1].append(pre)

    for semana in range(2):
        for i in range(5):

            if temperatura[semana][i] >= 40 or temperatura[semana][i] <= 5:
                alertas += 1

            if umidade[semana][i] <= 20 or umidade[semana][i] >= 95:
                alertas += 1

            if precipitacao[semana][i] >= 80:
                alertas += 1

    valor_maximo = max(max(temperatura[0]), max(temperatura[1]))
    valor_min = min(min(temperatura[0]), max(temperatura[1]))
    print("A maior temperatura das semanas é:", valor_maximo)

print("\nMensagem final:")
if alertas > 5:
    print("Risco Alto de Evento Climático Extremo")
else:
    print("Clima sob controle")

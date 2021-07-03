print("#############################################################")
print("##  Faturamento Ticket Veículos Estacionamento Seu Jertuz  ##")
print("#############################################################")

veiculo = int(input("Digite o numero do Veículo: \n 1 - Moto; \n 2 - Carro de passeio; \n 3 - Pick-Up; \n 4 - Caminhão; \nn: "))
horas = float(input("Digite a quantidade de horas estacionado: "))

if(veiculo == 1):
    horas = horas - 1
    valor = 5+(1.25*horas)
    print("\nVeículo: Moto\nO valor a pagar é de: R$",valor)
elif(veiculo == 2):
    horas = horas - 1
    valor = 8+(2*horas)
    print("\nVeículo: Carro de passeio\nO valor a pagar é de: R$",valor)
elif(veiculo == 3):
    horas = horas - 1
    valor = 12+(3*horas)
    print("\nVeículo: Pick-Up\nO valor a pagar é de: R$",valor)
elif(veiculo == 4):
    horas = horas - 1
    valor = 20+(5*horas)
    print("\nVeículo: Caminhão\nO valor a pagar é de: R$",valor)
else:
    print("\nOps, você não digitou um numero de Veículo valido.")
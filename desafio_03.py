print("#############################################################")
print("##  Faturamento Ticket Veículos Estacionamento Seu Jertuz  ##")
print("#############################################################")

veiculo = int(input("Digite o numero do Veículo: \n 1 - Moto; \n 2 - Carro de passeio; \n 3 - Pick-Up; \n 4 - Caminhão; \nn: "))
hora_entrada = int(input("Digite a hora de entrada: "))
minuto_entrada = int(input("Digite o minuto de entrada: "))
hora_saida = int(input("Digite a hora de saída: "))
minuto_saida = int(input("Digite o minuto de saída: "))

minutos_calc = 0
horas_calc = 0
minutos_estacionado = 0
horas_estacionado = 0

if(minuto_entrada >= minuto_saida ):
    minutos_calc = ((hora_saida - hora_entrada)*60)-(minuto_entrada-minuto_saida)
elif(minuto_entrada < minuto_saida):
    minutos_calc = ((hora_saida - hora_entrada)*60)-(minuto_saida-minuto_entrada)

while (minutos_calc >= 60):
        horas_calc = horas_calc + 1
        minutos_calc = minutos_calc - 60

minutos_estacionado = minutos_calc
horas_estacionado = horas_calc

if(minutos_estacionado >= 10):
    horas_calc = horas_calc + 1

if(veiculo == 1):
    horas_calc = horas_calc - 1
    valor = 5+(1.25*horas_calc)
    print(f"\nVeículo: Moto\nTempo: {horas_estacionado}h{minutos_estacionado}\nO valor a pagar é de: R${valor}")
elif(veiculo == 2):
    horas_calc = horas_calc - 1
    valor = 8+(2*horas_calc)
    print(f"\nVeículo: Carro de passeio\nTempo: {horas_estacionado}h{minutos_estacionado}\nO valor a pagar é de: R$",valor)
elif(veiculo == 3):
    horas_calc = horas_calc - 1
    valor = 12+(3*horas_calc)
    print(f"\nVeículo: Pick-Up\nTempo: {horas_estacionado}h{minutos_estacionado}\nO valor a pagar é de: R$",valor)
elif(veiculo == 4):
    horas_calc = horas_calc - 1
    valor = 20+(5*horas_calc)
    print(f"\nVeículo: Caminhão\nTempo: {horas_estacionado}h{minutos_estacionado}\nO valor a pagar é de: R$",valor)
else:
    print("\nOps, você não digitou um numero de Veículo valido.")
 
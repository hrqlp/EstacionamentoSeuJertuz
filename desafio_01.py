print("#############################################################")
print("##  Bonificação de Final de ano Estacionamento Seu Jertuz  ##")
print("#############################################################")

funcao = int(input("Digite o numero da sua função: \n 1 - Segurança; \n 2 - Caixa; \n 3 - Manobrista; \nn: "))
salario = float(input("Digite o valor de seu salário: "))

if(funcao == 1):
    salario = salario * 1.09
    print("O seu salário com bonus será: R$",salario)
elif(funcao == 2):
    print("O seu salário com bonus será: R$",salario)
elif(funcao == 3):
    salario = salario * 1.12
    print("O seu salário com bonus será: R$", salario)
else:
    print("\nOps, você não digitou um numero de função valido.")
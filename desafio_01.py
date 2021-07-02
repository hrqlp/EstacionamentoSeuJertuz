#vinheta definida em uma variavel de string com quebras de linhas
vinheta = "#############################################################\n##  Bonificação de Final de ano Estacionamento Seu Jertuz  ##\n#############################################################"
print(vinheta)

funcao = int(input("Digite o numero da sua função: \n 1 - Segurança; \n 2 - Caixa; \n 3 - Manobrista; \nn: "))
salario = float(input("Digite o valor de seu salário: "))
# criando variavel padrão para o resultado 
msg_bonus = ".\nO seu salário com bonus será: R$"
if(funcao == 1):
    # veja que podemos fazer o calculo do bonus diretamente no print 
    # e alem disso tambem podemos usar a função round(valor, casas_decimais) que fará o arredondamento do resultado do calculo e definira quantas casas decimais será exibida.
    print(msg_bonus,round(salario * 1.09, 2))
elif(funcao == 2):
    print(msg_bonus,round(salario * 1.10, 2))
elif(funcao == 3):
    print(msg_bonus, round(salario * 1.12, 2))
else:
    print("\nOps, você não digitou um numero de função valido.")
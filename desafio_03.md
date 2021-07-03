## Desafio 02 - Faturamento Ticket Veículos V2

### Contexto: 
Seu Jertuz continua com uma grande movimentação no seu estacionamento e precisa que seja desenvolvida uma nova funcionalidade no programa desenvolvido no desafio anterior, a funcionalidade consiste em calcular também o tempo de permanência do veículo no estacionamento:    
> Olá jovem padawan. Poderia me ajudar? Preciso que escreva uma nova funcionalidade no programa do desafio anterior. Quero que o programa também realize o cálculo de permanência do veículo. 
> 
> Tendo como parâmetro as seguintes formulas:  
> - Formula 1 - utilizada para encontrar a quantidade de minutos exata:
>    - ```MinutosExato = ((HS-HE)*60)-(MMA-MME)``` ||| legenda: [ ``((`` hora_saida ``-`` hora_entrada ``)*60)-(``minuto_maior ``-`` minuto_menor``)``]
> - Formula 2 - utilizada para encontrar o resto da divisão e consequentemente a hora e minutos exato.
>   - ``MinutoHora = MinutosExato - ( 60 * horasEstacionado )`` ||| horasEstacionado consiste em um valor que o Seu Jertuz vai substituindo sequencialmente até o primeiro resultado que for menor que 60. 
>       - exemplo: 1° tentativa 124-(60x1) = 64 [ainda não é menor que 60], 2° tentativa 124-(60x2)=4 [é menor que 60], então sabemos que o resto da divisão é 4, depois de 2 tentativas. Então sabemos que neste exemplo o veículo ficou estacionado por 2h04min.
> 
>> Após o cálculo  arredonde para realizar a cobrança. Caso o MinutoHora for maior ou igual a 10 arredonde para hora consecutiva. 
>> Se for menor que 10 cobre a hora atual sem arredondar. neste exemplo acima de _2h04_ será cobrado como 2h apenas.



### Segue Tabela de siglas:  


Sigla             | Valor Fixo 1h (VFH) | Exemplo de dado
------------------- | -------------------| ---------
HE                | Hora Entrada              |  13:49
HS    | Hora Saída               |   22:25
MMA             | Mínuto Maior              |   49
MME            | Mínuto Menor              |   25

  
### Cenário: 
> um motociclista chega às 13:49 ao estacionamento e estaciona sua moto. Às 22:25 o motociclista volta e pede ao Seu Jertuz o ticket para realizar o pagamento. Seu Jertuz pontualmente o atende, pega a tabela de preços, papel e calculadora de cordão. E então verificou que a moto ficou das 13h às 22h e fez o primeiro cálculo  que descobre a quantidade de MinutosExato ```((22-13)*60)-(49-25)``` que nesse caso é ``516``, então ele aplica a segunda formula ``516 - (60 * 8)`` que nesse caso é ``36`` então depois de 8 tentativas ele descobre que o MinutoHora é 36, ou seja **a moto ficou estacionada 8h36min** 
> 
>Seu Jertuz analisa como fará a cobrança, caso o MinutoHora for maior ou igual a 10 ele arredonda a hora pra hora consecutiva e cobra o valor correspondente, senão caso o MinutoHora for menor que 10 ele cobra a hora atual sem arredondar. Neste caso de 8h36 ele cobrará como 9h

##### **Imagem do exemplo de como deve ser o funcionamento do programa:** 

![Imagem de exemplo de interface](https://i.imgur.com/4Y2Eo4O.png)

### E aí, bora cumprir esse desafio??? 👩‍💻

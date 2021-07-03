## Desafio 02 - Faturamento Ticket Veículos

### Contexto: 
Seu Jertuz está com uma grande movimentação no seu estacionamento e já não está mais conseguindo fazer os cálculos dos tickets dos clientes em um tempo hábil com seu bloquinho e com sua calculadora de cordão. Então ele nos escreveu, e propôs o seguinte desafio:    
> Olá jovem padawan, Poderia me ajudar? Preciso que escreva um programa que realize o cálculo do ticket de cada cliente. 
> 
> Tendo como parâmetro a seguinte formula:  ```VFH + (VAH* h)``` [ valor_fixo_1h ```+ (``` valor_adicional_hora ```x``` quantidade_horas_estacionado ```)```]
> 



### Segue Tabela de preços:  


Veículo             | Valor Fixo 1h (VFH) | Valor adicional hora (VAH)
------------------- | -------------------| ---------
Moto                | R$ 5               |   R$ 1.25
Carro de passeio    | R$ 8               |   R$ 2
Pick-Up             | R$ 12              |   R$ 3
Caminhão            | R$ 20              |   R$ 5 

  
### Cenário: 
> um motociclista chega às 12h ao estacionamento e estaciona sua moto. Às 19h o motociclista volta e pede ao Seu Jertuz o ticket para realizar o pagamento. Seu Jetruz pontualmente o atende, pega a tabela de preços, papel e calculadora de cordão. E então verificou que a moto ficou das 12h às 19h e fez o primeiro calculo que descobre a quantidade de horas ```19h - 12h = 7h``` (não é necessário esse cálculo  no programa). 
> 
>Seu Jertuz sabe que o Veículo é uma **moto** e que a primeira hora é **R$5** e as horas adicionais é **R$1.25** e que a moto ficou estacionada por **7h**. Ou seja de **7h serão consideradas 6h adicionais e 1h sera cobrada como Valor fixo**, eis então o calculo ```5+(1.25*6)=12.5```. com base no resultado Seu Jertuz cobra R$12.50 do motocilista.

##### **Imagem do exemplo de como deve ser o funcionamento do programa:** 

![Imagem de exemplo de interface](https://i.imgur.com/anB8cOH.png)

### E aí, bora cumprir esse desafio??? 👩‍💻

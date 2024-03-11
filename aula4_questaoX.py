1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.

O terreno possui 250m2 e custa R$512,490.50

Comente na linha acima de cada instrução uma breve descrição da instrução.

Fórmulas:
area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2

Resposta:
comprimento = int(input("Digite o comprimento do terreno em metros: "))
largura = int(input("Digite a largura do terreno em metros: "))
preco_m2 = float(input("Digite o preço do metro quadrado da região: "))
area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2
print(f'O terreno possui {area_m2}m2 e custa R${preco_total:.2f}')

2) Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:

86 graus Fahrenheit são 30 graus Celsius.

Resposta:
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))
celsius = int((fahrenheit - 32) * (5/9))
print(f'{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.')




3) Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que:
Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito).
A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).
Entrada:
Digite o nome do produto 1: calça
Digite o preço unitário do produto 1: 199.90
Digite a quantidade do produto 1: 3
Digite o nome do produto 2: camisa
Digite o preço unitário do produto 2: 49.95
Digite a quantidade do produto 2: 10
Digite o nome do produto 3: cinto
Digite o preço unitário do produto 3: 25
Digite a quantidade do produto 3: 3

Saída:
Total: R$1,174.20

Resposta:
preco_total = 0
for i in range(1, 4):
    nome_produto = input(f'Digite o nome do produto {i}: ')
    preco_unitario = float(input(f'Digite o preço unitário do produto {i}: '))
    quantidade = int(input(f'Digite a quantidade do produto {i}: '))
    preco_parcial = preco_unitario * quantidade
    preco_total += preco_parcial
print(f'Total: R${preco_total:.2f}')


4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado. 

Entrada:
576

Saída:
5 nota(s) de R$100,00
1 nota(s) de R$50,00
1 nota(s) de R$20,00
0 nota(s) de R$10,00
1 nota(s) de R$5,00
0 nota(s) de R$2,00
1 nota(s) de R$1,00

Resposta:
valor_reais = int(input("Digite a quantia em reais: "))
notas = [100, 50, 20, 10, 5, 2, 1]
for nota in notas:
    qtd_notas = valor_reais // nota
    valor_reais %= nota
    print(f'{qtd_notas} nota(s) de R${nota},00')

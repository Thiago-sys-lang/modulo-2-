1) Transforme o seguinte algoritmo em código. Lembre-se das funções print e type que já conhecemos de forma geral.
Armazene o valor 5 em uma variável e o valor 2 em outra variável
Imprima o tipo de dados dessas duas variáveis
Divida a primeira variável (com o valor 5) pela segunda variável (com o valor 2) e armazene o resultado em uma terceira variável
Imprima a terceira variável e também o seu tipo

resposta:
valor_um = 5
print(type(valor_um))
<class 'int'>
valor_dois= 2 
print(type(valor_dois))
<class 'int'>
divisao = valor_um / valor_dois
print(divisao)
print(type(divisao))



2) Transforme o seguinte algoritmo em código. Lembre-se das funções print e type que já conhecemos de forma geral.
Armazene o texto "o resultado é"  em uma variável, o valor 10 em outra variável, e o valor 3.5 numa terceira variável.
Some os valores da segunda e terceira variável e armazene em outra variável.
Imprima todas as variáveis na ordem de criação e imprima também seus tipos.

resposta:
r1 = "o resultado é"
r2 = 10
r3 = 3.5
print = r2 + r3
13.5
r4 = 13.5
print(r1)
o resultado é
print(r2)
10
print(r3)
3.5
print(r4)
13.5
print(type(r1))
print(type(r2))
print(type(r3))
print(type(r4))
<class 'string'>
<class 'int'>
<class 'float'>
<class 'float'>




3) Dadas duas variáveis v1 = 10 e v2 = 20, utilize uma terceira variável para trocar os valores entre as duas variáveis. Ou seja, ao final v1 terá o valor de v2, e v2 o valor de v1. Você deve usar uma variável auxiliar de troca, não podendo atribuir os novos valores diretamente.

resposta:
v1 = 10
v2 = 20
aux = v1
v1 = v2
v2 = aux

4) Uma conta poupança foi aberta com um depósito de R$500,00. Esta conta é remunerada em 1% de juros ao mês. O código a seguir apresenta uma forma de implementação para calcular três meses de acúmulo de juros. Reescreva esse código usando apenas duas variáveis. 

juros = 1.01
saldo = 500.0
rendimento1 = saldo * juros
rendimento2 = rendimento1 * juros
rendimento3 = rendimento2 * juros
print("Após 3 meses meu novo saldo é")
print(rendimento3)

resposta:
juros = 1.01
saldo = 500.0
print(saldo)
saldo = saldo * juros # 505 rendimento1
print(saldo)
saldo = saldo * juros # 510 rendimento2
print(saldo)
saldo = saldo * juros # 515 rendimento3
print(saldo)
print(type(saldo))


500.0
505.0
510.05
515.1505
<class 'float'>


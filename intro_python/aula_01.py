print("Meu primeiro programa em Python")
a = 10
b = 5

#Operações e variáveis
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

#Print variáveis
print("soma: " + soma)
print("subtração: " + subtracao)
print("multiplicação: " + multiplicacao)
print("divisão: " + divisao)
print("resto: " + resto)

#Tipo do dado
print(type(soma))
print(type("string"))

#Cast
soma = str(soma)
print(type(soma))
num = int('1')
print(type(num))

#f string
print(f'Soma = {soma}')
print(f'Soma: {1}\tSubtracao: {0}'.format(subtracao, soma))

#Input
a = int(input("Digite o primeiro valor"))
b = int(input("Digite o segundo valor"))
print(a+b)
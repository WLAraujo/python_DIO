# Maior valor
a = int(input("Digite o primeiro número"))
b = int(input("Digite o segundo número"))
c = int(input("Digite o terceiro número"))

if a > b and a > c:
    print("O primeiro número é o maior")
elif b > a and b > c:
    print("O segundo número é o maior")
else:
    print("O terceiro número é o maior")

# Número par
a = int(input("Digite o primeiro número"))
b = int(input("Digite o segundo número"))

if a % 2 == 0 or b % 2 == 0:
    print("Foi digitado um número par")
else:
    print("Só foram digitados números ímpares")
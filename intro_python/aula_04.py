for i in range(0, 100):
    print(i)

a = int(input("Digite um número inteiro"))
for i in range(0, a):
    print(a)

x = int(input("Digite um número inteiro"))
div = 0
for i in range(0, x):
    if x % i == 0:
        div += 1
        break
if div >= 1:
    print("O número não é primo")
else:
    print("O número é primo")

a = 100
while a >= 10:
    print(a)
    a -= 1

x = 0
while x > 10 or x < 5:
    x = int(input("Digite um número inteiro"))

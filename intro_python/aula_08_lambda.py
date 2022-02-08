# Lambdas são funções anônimas

contador_letras = lambda lista: [len(palavra) for palavra in lista]

concatena = lambda s1, s2 : s1 + s2

calculadora = {
    'soma' : lambda a, b: a + b, 
    'subtração' : lambda a, b: a - b, 
    'multiplicacao' : lambda a, b: a * b, 
    'divisao' : lambda a, b: a / b, 
}

soma = calculadora['soma']

print(contador_letras(['palavras', 'letras']))
print(concatena("Essa é uma", " frase"))
print(soma(2,3))
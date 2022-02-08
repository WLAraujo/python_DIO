# Métodos - Não retornam nada
# Função - Retorna um valor

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def soma(self):
        return self.a + self.b
    def subtracao(self):
        return self.a - self.b
    def multiplicacao(self):
        return self.a * self.b
    def divisao(self):
        return self.a / self.b

calc = Calculadora(10,2)

print(calc.soma())
print(calc.subtracao())
print(calc.multiplicacao())
print(calc.divisao())

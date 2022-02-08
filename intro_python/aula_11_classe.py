# Clase que herda de Exception
class EntradaInvalida(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem

if __name__ == '__main__':
    while True:
        try:
            x = float(input("Digite um valor entre 0 e 10\n"))
            print(x)
            if x > 10 or x < 0:
                raise EntradaInvalida("Digite uma entrada válida, valor entre 0 e 10")
        except ValueError:
            print("Só digite valores numéricos\n")
        except EntradaInvalida as erro:
            print(erro)

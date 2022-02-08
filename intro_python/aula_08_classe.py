########################
# Acessando uma classe #
########################

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

########################
# Acessando uma função #
########################

def contador_letras(lista_palavras):
    quantidades = []
    for palavra in lista_palavras:
        quantidades.append(len(palavra))
    return quantidades

# O condicional abaixo testa se o próprio arquivo é o main da execução atual
# caso outro arquivo que esteja chamando esse módulo o que está dentro dessa condicional não é chamado
if __name__ == '__main__':
    tv = Televisao()
    tv.power()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)
    print(tv.canal)
    tv.aumenta_canal()
    print(tv.canal)
    lista = ['palavras', 'letras', 'frases']
    print(contador_letras(lista))
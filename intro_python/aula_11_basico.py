# Python exceptions https://docs.python.org/3/library/exceptions.html

def erro_div_zero():
    return 10/0

def erro_indice():
    lista = [0,1,2,3,4,5]
    return lista[6]

def erro_desconhecido():
    return "x" + 10

try:
    arquivo = open('aula_11_teste.txt', 'a')
    print("Try")
    erro_div_zero()
    #erro_indice()
    #erro_desconhecido()
except ZeroDivisionError:
    print("Erro de divisão por zero")
except IndexError:
    print("Erro de indice inexistente")
except BaseException as erro:
    print(f'Erro desconhecido {erro}')
else:
    print("Não ocorreram exceções")
finally:
    arquivo.close()

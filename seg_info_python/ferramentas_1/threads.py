from threading import Thread # https://docs.python.org/3/library/threading.html
import time

chamada = 1

def decrementar(numero, decremento):
    global chamada
    i = chamada
    chamada = chamada + 1
    while numero >= 0:
        print(f'Chamada {i}: {numero}')
        numero -= decremento
        time.sleep(0.5)
    print(f'Chamada {i}: Chegou!!!')

# Abaixo instanciamos uma thread para chamar a função que desejamos com os argumentos desejados
thread_1 = Thread(target=decrementar, args=[10,2])
thread_2 = Thread(target=decrementar, args=[20,3])

# Abaixo começamos as threads concorrentes determinadas
thread_1.start()
thread_2.start()

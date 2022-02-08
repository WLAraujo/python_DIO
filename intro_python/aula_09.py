import shutil

def escrever_arquivo(texto, arq):
    arquivo = open(arq, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto, arq):
    arquivo = open(arq, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(arq):
    arquivo = open(arq, 'r')
    texto = arquivo.read()
    print(texto)

def calcular_medias(arq):
    arquivo = open(arq, 'r')
    texto = arquivo.read()
    alunos = texto.split('\n')
    for aluno in alunos:
        notas = aluno.split(',')
        nome = notas.pop(0)
        print(nome)
        print(notas)
        notas_int = [int(nota) for nota in notas]
        media = sum(notas_int) / len(notas_int)
        print(media)
    arquivo.close()

def copiar_arquivo(arq):
    shutil.copy(arq, 'Bootcamp_Carrefour_DE/intro_python')

def mover_arquivo(arq):
    shutil.move(arq, 'Bootcamp_Carrefour_DE/intro_python')

if __name__ == "__main__":
    escrever_arquivo("Primeira linha", 'teste_aula_9.txt')
    atualizar_arquivo("\nSegunda linha", 'teste_aula_9.txt')
    ler_arquivo('teste_aula_9.txt')
    escrever_arquivo("Rafael, 10, 9, 8\nMarcio, 8, 6, 7, 9\nAna, 10, 9, 9, 5", 'notas_aula_9.txt')
    calcular_medias('notas_aula_9.txt')




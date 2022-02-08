import hashlib # https://docs.python.org/3/library/hashlib.html

if __name__ == "__main__":

    nome_arq_1 = input("Digite o nome do arquivo 1\n")
    nome_arq_2 = input("Digite o nome do arquivo 2\n")

    # Observe que abrimos o arquivo no modo de leitura binário
    arquivo_1 = open(nome_arq_1, 'rb')
    arquivo_2 = open(nome_arq_2, 'rb')

    texto_arq_1 = arquivo_1.read()
    texto_arq_2 = arquivo_2.read()

    # Abaixo construímos um objeto hash que nos permite interagir com os métodos da biblioteca, ele tem como
    # atributo o algoritmo de hash que usaremos
    hash1 = hashlib.new('ripemd160')
    # Abaixo calculamos o hash do arquivo com a função update
    hash1.update(texto_arq_1)

    hash2 = hashlib.new('ripemd160')
    hash2.update(texto_arq_2)

    # Abaixo usamos a função digest para resumir os hashes para que eles sejam comparáveis
    if hash1.digest() == hash2.digest():
        print('Os arquivos são iguais!!!')
    else:
        print('Os arquivos NÃO são iguais!!!')
    
    # Abaixo vamos imprimir os hashes dos dois arquivos
    print(f'Hash do arquivo {nome_arq_1}: {hash1.hexdigest()}')
    print(f'Hash do arquivo {nome_arq_2}: {hash2.hexdigest()}')
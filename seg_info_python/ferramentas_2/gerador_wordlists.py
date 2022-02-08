# wordlists - Arquivos contendo uma palavra por linha, são utilizados em ataques de força bruta como
# quebra de autenticaçã e podem ser usados para testar autenticação e confidencialidade de um sistema.

import itertools

string = input("Digite a string a ser permutada: ")

# A função abaixo retorna todas as permutações dos elemsntos da string
permutacoes = itertools.permutations(string, len(string))

arquivo = open("wordlist.txt", "w")

for combinacao in permutacoes:
    print("".join(combinacao))
    arquivo.write(''.join(combinacao) + "\n")

arquivo.close()

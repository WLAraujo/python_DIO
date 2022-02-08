conjunto = {1,2,3,4,1,3}
print(conjunto)

conjunto.add(10)
conjunto.add(4)
print(conjunto)

conjunto.discard(1)
conjunto.discard(11)
print(conjunto)

conjunto_2 = {5,6,7,8,9}

conj_uniao = conjunto.union(conjunto_2)
print(conj_uniao)

conj_interseccao = conjunto.intersection(conjunto_2)
print(conj_interseccao)

conj_diferenca = conjunto.difference(conjunto_2)
print(conj_diferenca)
conj_diferenca2 = conjunto_2.difference(conjunto)
print(conj_diferenca2)

conj_dif_simetrica = conjunto.symmetric_difference(conjunto_2)
print(conj_dif_simetrica)

subconjunto = {2,3}
print(subconjunto.issubset(conjunto))
print(conjunto.issuperset(subconjunto))

lista = [1, 2, 3, 4, 5, 1, 6, 7, 4]
print(set(lista))
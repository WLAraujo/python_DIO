lista = [1,3,5,7]
lista_animais = ["cão", "gato", "peixe", "cavalo"]

print(lista_animais[0])

for animal in lista_animais[1:]:
    print(animal)

soma = 0

for num in lista:
    soma += num

print(soma)

print(max(lista))

print(max(lista_animais))

if "lobo" in lista_animais:
    print("Existe lobo na lista")
else:
    lista_animais.append("lobo")
    print("Agora existe lobo na lista")

nova_lista = lista * 4
print(nova_lista)

lista.pop(0)
print(lista)
lista.remove(7)
print(lista)

tupla = (1,2,3,4)
print(tupla)

print(str(len(lista)) + ', ' + str(type(lista)))
print(str(len(tupla)) + ', ' + str(type(tupla)))
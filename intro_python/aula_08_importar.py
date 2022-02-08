from aula_8_classe import Televisao
from aula_8_classe import contador_letras

if __name__ == "__main__":
    tv = Televisao()
    print(tv.ligada)
    lista = ["palavra", "letras", "frases", "sentenças"]
    print(contador_letras(lista))


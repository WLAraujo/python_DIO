# Biblioteca ctypes - fornece tipos de dados compatíveis com C e permite funções chamadas de bibliotecas
# compartilhadas entre as duas linguagens. Isso permite trabalhar com nosso programa em mais baixo nível.

import ctypes # https://docs.python.org/3/library/ctypes.html

# Atributos que o arquivo terá e que configura a ocultação
atributos_p_ocultar = 0x02

# Abaixo chamamos a DLL que permite que o arquivo seja manipulado para ser ocultado
retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultado.txt')

if retorno:
    print("Arquivo foi ocultado")
else:
    print("Arquivo não foi ocultado")

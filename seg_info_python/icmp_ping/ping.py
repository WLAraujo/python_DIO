import os
import time

print(60 * "#")

ip_ou_host = input("Digite o IP ou host a ser verificado: ")

print(60 * "-")

# os.system trabalha com a linha de comando
os.system(f"ping -c 5 {ip_ou_host}")

with open('ping_hosts.txt') as file:
    texto = file.read()
    texto_lista = texto.split('\n')
    for endereco in texto_lista:
        print("\n" + 60 * "#")
        print(f"Verificando o ip: {endereco}")
        print(60 * "-")
        os.system(f"ping -c 2 {endereco}")
        time.sleep(5)
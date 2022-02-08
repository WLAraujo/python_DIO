import hashlib

while True:
    print("###################################")
    string = input("Digite a string a qual deseja criar um hash: ")
    print("###################################")
    escolha = input(
'''Escolha o algoritmo para criar o hash:
    \t1. MD5
    \t2. SHA1
    \t3. SHA256
    \t4. SHA512
Digite uma opção ou digite qualquer outra tecla para sair: ''')
    if escolha == '1':
        res = hashlib.md5(string.encode('utf-8'))
        print(f"O hash da string é: {res.hexdigest()}")
    elif escolha == '2':
        res = hashlib.sha1(string.encode('utf-8'))
        print(f"O hash da string é: {res.hexdigest()}")
    elif escolha == '3':
        res = hashlib.sha256(string.encode('utf-8'))
        print(f"O hash da string é: {res.hexdigest()}")
    elif escolha == '4':
        res = hashlib.sha512(string.encode('utf-8'))
        print(f"O hash da string é: {res.hexdigest()}")
    else:
        break

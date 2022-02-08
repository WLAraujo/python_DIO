import socket
import sys
import time

def main():
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as erro:
        print("A conexão falhou!!!")
        print(f"Erro: {erro}")
        sys.exit()
    
    print("Socket criado com sucesso")

    host = 'localhost'
    port = 5432

    # Abaixo configuramos o servidor para ouvir de uma porta
    s.bind((host, port))

    mensagem = "\nServidor: Mensagem recebida"

    vezes = 5
    # O laço while abaixo configura o servidor para fivar escutando mensagens da porta configurada
    # Foi configurado um timer para que o servidor escute 5 mensagens e depois desligue
    while True:
        if vezes == 0:
            print("Servidor: Encerrando escuta!!!")
            sys.exit()
        dados, endereco = s.recvfrom(4096)
        # Servidor enviando mensagem caso tenha recebido mensagem
        if dados:
            print("Servidor enviando mensagem ...")
            s.sendto((dados + mensagem.encode()), endereco)
        vezes -= 1


if __name__ == "__main__":
    main()


import socket
import sys

def main():

    try:
        # Abaixo instanciamos um socket com protocolo TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro:
        print(f"A conexão falhou devido ao erro {erro}")
        # Abaixo saimos da aplicação
        sys.exit()
    
    print("Socket criado com sucesso")

    host_alvo = input("Digite host ou ip a sr conectado: ")

    porta_alvo = input("Digite a porta a ser concetada: ")

    try:
        # Socket TCP se conecta no host alvo através da porta alvo
        s.connect((host_alvo, int(porta_alvo)))
        print("Cliente TCP conectado com sucesso ao host " + host_alvo + " na porta " + porta_alvo)
        # Abaixo desligamos a conexão
        s.shutdown(3)
    except socket.error as erro:
        print("Não foi possível conectar ao host " + host_alvo + " através da porta " + porta_alvo)
        print(f"Erro {erro}")
        # Abaixo saimos da aplicação
        sys.exit()
    
if __name__ == "__main__":
    main()


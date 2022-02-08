import socket
import sys

def main():
    
    try:
        # Abaixo criamos um objeto de conexão UDP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as erro:
        print("Conexão falhou!")
        print(f"Erro: {erro}")
        sys.exit()
    
    host = 'localhost'
    porta = 5433
    mensagem = "Mensagem de teste"

    try:

        # Abaixo empacotamos a mensagem e a enviamos para o host na porta que o servidor está ouvindo
        s.sendto(mensagem.encode(), (host, 5432))

        # Abaixo recebemos uma resposta de 4096 bytes
        dados, servidor = s.recvfrom(4096)
        # Abaixo decodamos a mensagem recebida
        dados = dados.decode()
        print("Cliente: " + dados)

    finally:
        print("Cliente: Fechando a conexão")
        s.close()

if __name__ == "__main__":
    main()
import re # Expressões Regulares
import json # Codificação e Decodificação JSON
from urllib.request import urlopen # Funções e classes que facilitam trabalho com urls

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']

print(f"IP local: {ip}")
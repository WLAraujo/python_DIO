import ipaddress # https://docs.python.org/3/library/ipaddress.html

ip = '192.168.0.1'

# Abaixo transformamos nossa string em um endereço IP
endereco = ipaddress.ip_address(ip)

print(endereco + 256)

rede = '192.168.0.0/24' 

# Abaixo transformamos nossa string em um endereço de rede
rede = ipaddress.ip_network(rede)

print(rede)

# Abaixo printamos todos os IPs perntencentes à rede
for num_ip in rede:
    print(num_ip)
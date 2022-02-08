# A biblitoeca phonenumbers oferece vários recursos como informações básicas de um número e 
# validação de número de telofone

import phonenumbers
from phonenumbers import geocoder

tel = input("Digite o telefone no formato + código_pais codigo_unidade_federativa telefone:\n" )

tel_parseado = phonenumbers.parse(tel)

print(geocoder.description_for_number(tel_parseado, 'pt'))
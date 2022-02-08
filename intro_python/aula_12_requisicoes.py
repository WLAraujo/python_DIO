# biblioteca requests: https://docs.python-requests.org/en/master/
import requests

def retorna_dados_cep(cep):
    resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json')
    print(resposta.status_code)
    print(resposta.text)

def retorna_dados_pokemon(pokemon):
    resposta = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
    print(resposta.status_code)
    print(resposta.json()['species'])
    print(resposta.json()['stats'])
    print(resposta.json()['types'])

def retorna_resposta(url):
    resposta = requests.get(url)
    print(resposta.status_code)
    print(resposta.text)

if __name__ == '__main__':
    retorna_dados_cep('05887240')
    retorna_dados_pokemon('pikachu')
    retorna_resposta('https://catfact.ninja/fact')
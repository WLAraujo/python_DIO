import random # https://docs.python.org/3/library/random.html
import string

tamanho = 16
caracteres = string.ascii_letters + string.digits + "!@#$%&*()"

seed = random.seed()
sys_rand = random.SystemRandom(seed)

senha = ''.join(sys_rand.choice(caracteres) for i in range(tamanho))
print(senha)
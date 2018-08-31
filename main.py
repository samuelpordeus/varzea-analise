from jogador import Jogador
from equipe import Equipe
# from partida import Partida
from random import randint
from faker import Faker
fake = Faker('pt_BR')

posicoes = ["Atacante", "Meio-campista", "Zagueiro", "Lateral", "Goleiro"]

time1 = Equipe("Framengo")
for x in range(0,11):
    time1.add(Jogador(fake.name_male(), randint(20, 35), posicoes[randint(0,4)]))

time2 = Equipe("Vasco")
for x in range(0,11):
    time2.add(Jogador(fake.name_male(), randint(20, 35), posicoes[randint(0,4)]))

time1.info()
time2.info()

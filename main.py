from jogador import Jogador
from equipe import Equipe
from partida import Partida
from random import randint
from faker import Faker
import csv


def prepare_stats_file():
	with open('players_stats.csv', mode='a') as stats_file:
		stats_writer = csv.writer(stats_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	            
		columns = ['Name', 'Age', 'Position', 'Finishing', 'Passing', 'Pacing', 'Defending', 'Keeping',
	    	       'Attacking', 'Defensive', 'Level', 'Overall']
			       
		stats_writer.writerow(columns)


def add_players(team, fake):
	# add goalkeeper
	for i in range(1):
		team.add(Jogador(fake.name_male(), randint(20, 35), 'Goleiro'))

    # add centre backs
	for i in range(2):
		team.add(Jogador(fake.name_male(), randint(20, 35), 'Zagueiro'))
    
    # add wing backs
	for i in range(2):
		team.add(Jogador(fake.name_male(), randint(20, 35), 'Lateral'))

    # add midfielders
	for i in range(4):
		team.add(Jogador(fake.name_male(), randint(20, 35), 'Meio-campista'))

    # add strikers
	for i in range(2):
		team.add(Jogador(fake.name_male(), randint(20, 35), 'Atacante'))


#prepare_stats_file()
fake = Faker('pt_BR')
team1 = Equipe("Framengo")
add_players(team1, fake)
team2 = Equipe("Vaxcão")
add_players(team2, fake)

for i in range(10):
	print('Match number ' + str(i))
	Partida(team1, team2)
	print()
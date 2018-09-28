from random import randint

class Partida:
	def __init__(self, team1, team2):
		self.team1 = team1
		self.team2 = team2
		self.team1_goals = 0
		self.team2_goals = 0

		self.match()


	def match(self):
		team1_ap = round(self.team1.calculate_AP())
		team1_dp = round(self.team1.calculate_DP())
		team2_ap = round(self.team2.calculate_AP())
		team2_dp = round(self.team2.calculate_DP())

		#print(self.team1.name, team1_ap)
		#print(self.team2.name, team2_dp)
		#print(self.team2.name, team2_ap)
		#print(self.team1.name, team1_dp)

		for minute in range(90):
			if team1_ap*randint(0,10) > team2_dp*randint(10,100):
				#print(str(minute) + ': ' + 'Goal: ' + self.team1.name)
				self.team1_goals += 1
			
			if team2_ap*randint(0,10) > team1_dp*randint(10,100):
				#print(str(minute) + ': ' + 'Goal: ' + self.team2.name)
				self.team2_goals += 1

		print('-- Match Score --')
		print(self.team1.name + ' ' + str(self.team1_goals) + ' x ' + str(self.team2_goals) + ' ' + self.team2.name)
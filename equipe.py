class Equipe:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.attacking_power = None
        self.defensive_power = None

        self.calculate_AP()
        self.calculate_DP()


    
    def add(self, player):
        self.players.insert(0, player)
    
    def info(self):
        print(self.name, "-", str(len(self.players)), "players") 
        for player in self.players:
            print(player.name, "-", player.position)

    def calculate_AP(self):
        ap = 0
        for player in self.players:
            ap += player.attacking
        return ap

    def calculate_DP(self):
        dp = 0
        for player in self.players:
            dp += player.defensive
        return dp

class Equipe:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []
        self.team_power = self.calcula_tp()
    
    def add(self, jogador):
        self.jogadores.insert(0, jogador)
    
    def info(self):
        print(self.nome, "-", str(len(self.jogadores)), "jogadores") 
        for jogador in self.jogadores:
            print(jogador.nome, "-", jogador.posicao)

    def calcula_tp(self):
        for jogador in self.jogadores:
            print(jogador.nome, "-", jogador.posicao)
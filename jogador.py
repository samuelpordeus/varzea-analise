from random import randint

class Jogador:
    def __init__(self, nome, idade, posicao):
        # Basico
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        # Skillset
        self.chute = None
        self.velocidade = None
        self.passe = None
        self.defesa = None
        self.maos = None
        self.estrela = None
        self.__generate_stats(self.posicao)

    def info(self):
        print("Nome: %s\nPosição: %s\nIdade: %i\nChute: %i\nVelocidade: %i\nPasse: %i\nDefesa: %i\nHabilidade com as mãos: %i\n"
              %(self.nome, self.posicao, self.idade, self.chute, self.velocidade, self.passe, self.defesa, self.maos))

    def __generate_stats(self, posicao):
        estrela = randint(0,100)
        if estrela >= 60:
            estrela = 'Pereba'
            
        if posicao == "Atacante":
            chute_mod = 1.8
            passe_mod = 1.0
            velocidade_mod = 1.8
            defesa_mod = 0.5
            maos_mod = 0.1
        elif posicao == "Meio-campista":
            chute_mod = 1.5
            passe_mod = 2.0            
            velocidade_mod = 1.0
            defesa_mod = 1.0
            maos_mod = 0.1
        elif posicao == "Zagueiro":
            chute_mod = 0.5
            passe_mod = 0.8            
            velocidade_mod = 0.7
            defesa_mod = 2.0
            maos_mod = 0.2   
        elif posicao == "Lateral":
            chute_mod = 1.0
            passe_mod = 1.5
            velocidade_mod = 1.0
            defesa_mod = 1.5
            maos_mod = 0.1 
        elif posicao == "Goleiro":
            chute_mod = 0.3
            passe_mod = 0.7
            velocidade_mod = 1.0
            defesa_mod = 2.0
            maos_mod = 2.0

        self.chute = round(randint(30, 50)*chute_mod)
        self.passe = round(randint(30, 50)*passe_mod)
        self.velocidade = round(randint(30, 50)*velocidade_mod)
        self.defesa = round(randint(30, 50)*defesa_mod)
        self.maos = round(randint(30, 50)*maos_mod)
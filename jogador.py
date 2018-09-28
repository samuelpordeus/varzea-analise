from random import randint
import csv

class Jogador:
    def __init__(self, name, age, position):
        # basic infos
        self.name       = name
        self.age        = age
        self.position   = position

        # technical skills
        self.finishing  = None
        self.pacing     = None
        self.passing    = None
        self.defending  = None
        self.keeping    = None

        # overall infos
        self.attacking  = None
        self.defensive  = None
        self.level      = None
        self.overall    = None

        self.generate_stats(self.position)
        self.save_stats()

    def info(self):
        print("Name: %s\nPosition: %s\nAge: %i\nFinishing: %i\nPacing: %i\nPassing: %i\ndefending: %i\nKeeping: %i\n"
              %(self.name, self.position, self.age, self.finishing, self.pacing, self.passing, self.defending, self.keeping))

    
    def set_level(self, position):
        if position != 'Atacante':
            prob = randint(0, 1000)
            if prob == 1000:
                self.level = 6

        else:   # striker
            prob = randint(0, 1000)
            if prob >= 999:
                self.level = 6

        if self.level == None:
            prob = randint(0, 100)
            if prob <= 40:
                self.level = 1
            elif prob > 40 and prob <= 67:
                self.level = 2
            elif prob > 67 and prob <= 85:
                self.level = 3
            elif prob > 85 and prob <= 95:
                self.level = 4
            elif prob > 95 and prob <= 100:
                self.level = 5           


    def calculate_stat(self, mod):
        if mod != 0:
            return randint(30, 50)*mod + self.level*100
        else:
            return randint(30, 50)*mod


    def generate_stats(self, position):
        # set modifiers
        if position == "Atacante":
            finishing_mod   = 2.0
            passing_mod     = 1.0
            pacing_mod      = 1.5
            defending_mod   = 0.5
            keeping_mod     = 0.0
        elif position == "Meio-campista":
            finishing_mod   = 1.2
            passing_mod     = 2.0            
            pacing_mod      = 0.8
            defending_mod   = 1.0
            keeping_mod     = 0.0
        elif position == "Zagueiro":
            finishing_mod   = 0.3
            passing_mod     = 0.75            
            pacing_mod      = 0.75
            defending_mod   = 3.2
            keeping_mod     = 0.0   
        elif position == "Lateral":
            finishing_mod   = 0.8
            passing_mod     = 1.5
            pacing_mod      = 1.2
            defending_mod   = 1.5
            keeping_mod     = 0.0 
        elif position == "Goleiro":
            finishing_mod   = 0.0
            passing_mod     = 1.0
            pacing_mod      = 0.5
            defending_mod   = 0.5
            keeping_mod     = 3.0

        
        self.set_level(position)

        self.finishing  = self.calculate_stat(finishing_mod)
        self.passing    = self.calculate_stat(passing_mod)
        self.pacing     = self.calculate_stat(pacing_mod)
        self.defending  = self.calculate_stat(defending_mod)
        self.keeping    = self.calculate_stat(keeping_mod)
        self.attacking  = self.finishing + self.passing + self.pacing
        self.defensive  = self.defending + self.keeping + self.pacing
        self.overall    = self.attacking + self.defensive


    def save_stats(self):
        with open('players_stats.csv', mode='a') as stats_file:
            line = [self.name, self.age, self.position, self.finishing, self.passing, self.pacing, self.defending,
                    self.keeping, self.attacking, self.defensive, self.level, self.overall]

            stats_writer = csv.writer(stats_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
            stats_writer.writerow(line)



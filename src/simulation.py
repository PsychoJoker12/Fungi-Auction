from random import choice
import reference

class Simulation(object):
    def __init__(self):
        self.fungi = []
        self.environment = choice(reference.environments)
    
    def update_environment(self):
        self.environment = choice(reference.environments)
        for fungus in self.fungi:
            fungus.update_environment(self.environment)
    
    def add_fungus(self, fungus):
        fungus.update_environment(self.environment)
        self.fungi.append(fungus)
    
    def print_fungi(self):
        for fungus in self.fungi:
            print(fungus)
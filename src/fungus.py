"""
A fungus object keeps track of growth rate and total growth
and responds to its environment based on its adaptations
"""
import reference

class Fungus(object):
    base_growth_rate = 20

    def __init__(self, adaptation_list=None):
        self.environment_modifier = 1
        self.adapt_rate = 1

        self.adaptations = []

        if adaptation_list is not None:
            for adaptation in adaptation_list:
                self.add_adaptation(adaptation)
    
    def __str__(self):
        out = "Fungus with "
        if len(self.adaptations) > 0:
            out += ", ".join([str(x) for x in self.adaptations])
        else:
            out += "no extra adaptations"
        
        return out
    
    def add_adaptation(self, adaptation):
        self.adaptations.append(adaptation)

    def growth_rate(self):
        return Fungus.base_growth_rate*self.environment_modifier*self.adapt_rate
    
    def update_environment(self, environment=reference.environments[9]):
        self.adapt_rate = 1

        for adaptation in self.adaptations:
            self.adapt_rate *= adaptation.check_environment(environment)

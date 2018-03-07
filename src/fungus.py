"""
A fungus object keeps track of growth rate and total growth
and responds to its environment based on its adaptations
"""
class Fungus(object):

    def __init__(self, adaptation_list=None):
        self.base_growth_rate = 20
        self.environment_modifier = 1
        self.growth_modifier = 1

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
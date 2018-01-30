"""
A fungus object contains a list of adaptations and
responds to its environment based on those adaptations
"""
class Fungus(object):
    """A Fungus"""

    def __init__(self, adaptation_list=None):
        self.base_growth_rate = 20
        self.environment_modifier = 1
        self.growth_modifier = 1

        self.adaptations = {
            "spore_production" : False,
            "heat_tolerance" : False,
            "freeze_tolerance" : False,
            "drought_tolerance" : False,
            "mutualism" : False,
            "haustoria" : False,
            "trapping_hyphae" : False,
            "antibiotics" : False,
            "ultra_hyphae" : False
        }

        if adaptation_list is not None:
            for adaptation in adaptation_list:
                self.add_adaptation(adaptation)

    def add_adaptation(self, adaptation):
        """Add an adaptation to the fungus provided it is in the list of adaptations"""
        if adaptation in self.adaptations:
            self.adaptations[adaptation] = True
        else:
            print(str(adaptation) + "is not an adaptation available for this fungus")

    def has_adaptation(self, adaptation):
        """return if the adaptation given applies to this fungus"""
        if adaptation in self.adaptations:
            return self.adaptations.get(adaptation)
        return False

    def check_growth(self, environment):
        """update growth rate of fungus based on environment variable"""
        self.growth_modifier = 1

        # high presure wind blasts
        if environment == 1:
            self.environment_modifier = 0.5

            if self.has_adaptation("spore_production"):
                self.growth_modifier *= 2
            if self.has_adaptation("heat_tolerance"):
                self.growth_modifier *= 2
            if self.has_adaptation("freeze_resistance"):
                self.growth_modifier *= 2

        # polar blast, arctic transition
        elif environment == 2:
            self.environment_modifier = 0.5

            if self.has_adaptation("freeze_tolerance"):
                self.growth_modifier *= 2
            if self.has_adaptation("drought_resistance"):
                self.growth_modifier *= 2

        # taiga, frozen water and arid conditions
        elif environment == 3:
            self.environment_modifier = 0.5
            if self.has_adaptation("freeze_resistance"):
                self.growth_modifier *= 2

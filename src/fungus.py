"""
A fungus object contains a list of adaptations and
responds to its environment based on those adaptations
"""
class Fungus(object):
    """A Fungus"""
    adaptation_numbers = {
        "spore_production" : 0,
        "heat_tolerance" : 1,
        "freeze_tolerance" : 2,
        "mutualism" :3,
        "haustoria" : 4,
        "trapping_hyphae" : 5,
        "antibiotics" : 6,
        "ultra_hyphae" : 7,
    }

    @staticmethod
    def adaptation_number(adaptation_str=None):
        """
        returns a number associated with a specific adaptation
        returns -1 if adaptation is not recognized
        """
        if adaptation_str is None:
            pass
        else:
            if adaptation_str not in Fungus.adaptation_numbers:
                return -1
            else:
                return Fungus.adaptation_numbers[adaptation_str]

    def __init__(self, adaptation_list=None):
        self.base_growth_rate = 20
        self.environment_modifier = 1
        self.growth_modifier = 1

        self.adaptations = {
            0 : False,
            1 : False,
            2 : False,
            3 : False,
            4 : False,
            5 : False,
            6 : False,
            7 : False,
            8 : False
        }

        if adaptation_list is not None:
            for number in adaptation_list:
                self.add_adaptation(number)

    def add_adaptation(self, number):
        """Add an adaptation to the fungus provided it is in the list of adaptations"""
        if number in self.adaptations:
            self.adaptations[number] = True
        else:
            print("adaptation number " + str(number) + " is not available for this fungus")

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

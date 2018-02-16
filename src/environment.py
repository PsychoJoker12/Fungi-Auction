class Environment(object):
    """An envronment that a fungus interacts with"""

    def __init__(self, name="default", growth_multiplier=1):
        self.name = name
        self.multiplier = multiplier

    def __str__(self):
        return self.name

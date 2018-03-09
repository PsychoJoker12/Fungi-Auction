class Environment(object):
    """An envronment that a fungus interacts with"""

    def __init__(self, name="Default Environment", multiplier=1.0):
        """Specify environment name and multiplier effect"""
        self.name = name
        self.multiplier = multiplier

    def __str__(self):
        return self.name

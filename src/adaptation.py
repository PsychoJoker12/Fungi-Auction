import reference

class Adaptation(object):
    """An adaptation which allows a fungus to accomplish some task"""

    def __init__(self, name="Default Adaptation", multiplier=1, suitable_environments=[]):
        """Specify a name and an optional constant multiplier"""
        self.name = name
        self.multiplier = multiplier
        self.suitable_environments = suitable_environments
    
    def __str__(self):
        return self.name

    def check_environment(self, environment=reference.environments[9]):
        if environment in self.suitable_environments:
            return self.multiplier
        else:
            return 1

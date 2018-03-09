class Adaptation(object):
    """An adaptation which allows a fungus to accomplish some task"""

    def __init__(self, name="Default Adaptation", multiplier=1):
        """Specify a name and an optional constant multiplier"""
        self.name = name
        self.multiplier = multiplier
    
    def __str__(self):
        return self.name

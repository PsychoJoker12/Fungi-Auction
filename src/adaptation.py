class Adaptation(object):
    """An adaptation which allows a fungus to accomplish some task"""

    def __init__(self, name, multiplier=1):
        self.name = name
        self.multiplier = multiplier
    
    def __str__(self):
        return self.name

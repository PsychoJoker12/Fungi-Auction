"""
driver class for fungus simulation
"""
from fungus import Fungus

def main():
    """main method"""
    fungus1_adaptations = {0,1}

    fungus1 = Fungus(fungus1_adaptations)
    print(fungus1.adaptations)

if __name__ == "__main__":
    main()

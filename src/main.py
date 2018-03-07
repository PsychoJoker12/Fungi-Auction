"""
driver class for fungus simulation
"""
from fungus import Fungus
from adaptation import Adaptation
from environment import Environment

def main():
    """main method"""

    adaptations = [
        Adaptation("Vast spore production", 2),
        Adaptation("Heat tolerant enzymes"),
        Adaptation("Freeze tolerant basidiocarp"),
        Adaptation("Drought-resistant chitinous wall"),
        Adaptation("Mutualism with photosynthetic alga", 3),
        Adaptation("Haustoria Hyphae"),
        Adaptation("Trapping Hyphae"),
        Adaptation("Penicillin resistant antibiotics"),
        Adaptation("Ultra-branched hyphae")
    ]

    fungus1_adaptations = [adaptations[3], adaptations[1]]

    fungus1 = Fungus(fungus1_adaptations)
    print("\n" + str(fungus1))

if __name__ == "__main__":
    main()

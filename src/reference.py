from adaptation import Adaptation
from environment import Environment

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

environments = [
        Environment(name="High presure wind blasts", multiplier=0.5),
        Environment(name="Polar blas, arctic transition", multiplier=0.5),
        Environment(name="Taiga, frozen water and arid conditions", multiplier=0.5),
        Environment(name="Bacterial bloom on soil surface"),
        Environment(name="Temerate New England fal (mid-September)", multiplier=0.5),
        Environment(name="Invasive grass biomass (increased biomass, large rainfall)", multiplier=2),
        Environment(name="Spring exponential growth of local rodent populations"),
        Environment(name="Epic drought and desert succession", multiplier=0.5),
        Environment(name="Freshwater flood", multiplier=0.5),
        Environment(name="No notable changes")
    ]
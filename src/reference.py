from adaptation import Adaptation
from environment import Environment

environments = [
    Environment(name="High presure wind blasts", multiplier=0.5),
    Environment(name="Polar blast, arctic transition", multiplier=0.5),
    Environment(name="Taiga, frozen water and arid conditions", multiplier=0.5),
    Environment(name="Bacterial bloom on soil surface", multiplier=0.5),
    Environment(name="Temerate New England fall (mid-September)", multiplier=0.5),
    Environment(name="Invasive grass biomass (increased biomass, large rainfall)", multiplier=2),
    Environment(name="Spring exponential growth of local rodent populations", multiplier=2),
    Environment(name="Epic drought and desert succession", multiplier=0.5),
    Environment(name="Freshwater flood", multiplier=0.5),
    Environment(name="No notable changes", multiplier=1)
]

spore_environments = list(environments[i] for i in [0,3,4,5,6,8])
heat_environments = list(environments[i] for i in [2,3])
freeze_environments = list(environments[i] for i in [0,1,2,4])
drought_environments = list(environments[i] for i in [0,1,4,7])
photosynthetic_environments = environments
haustoria_environments = list(environments[i] for i in [4,5])
trapping_environments = list(environments[i] for i in [6])
antibiotic_environments = list(environments[i] for i in [3])
ultra_branched_environments = list(environments[i] for i in [4,5])

adaptations = [
    Adaptation("Vast spore production", 2, spore_environments),
    Adaptation("Heat tolerance", 2, heat_environments),
    Adaptation("Freeze tolerance", 2, freeze_environments),
    Adaptation("Drought-resistance", 2, drought_environments),
    Adaptation("Mutualism with photosynthetic alga", 3, photosynthetic_environments),
    Adaptation("Haustoria Hyphae", 5, haustoria_environments),
    Adaptation("Trapping Hyphae", 5, trapping_environments),
    Adaptation("Penicillin resistance", 2, antibiotic_environments),
    Adaptation("Ultra-branched hyphae", 10, ultra_branched_environments)
]

"""
driver class for fungus simulation
"""
from fungus import Fungus
from adaptation import Adaptation
from environment import Environment

from simulation import Simulation
from random import choice

import os

import reference

simulation_environment = Simulation()

fungus1_adaptations = list(reference.adaptations[i] for i in [2,4])

simulation_environment.add_fungus(Fungus())
simulation_environment.add_fungus(Fungus(fungus1_adaptations))

def main():
    clear()
    display_fungi()
    introduce()

    while True:
        command = get_input()
        display_fungi()

        if command == -1:
            print("\nUser forcably closed input stream. Exiting program")
            return -1

        elif command == "ABOUT":
            about()
        elif command == "CLEAR":
            pass        
        elif command == "EXIT":
            break
        elif command == "HELP":
            get_help()
        elif command == "NEWADAPT":
            add_adaptation()
        elif command == "NEWENV":
            change_environment()
        elif command == "NEWF":
            add_fungus()
        elif command == "PASSTIME":
            pass_time()
        else:
            print("Unknown command, type \"Help\" to see a list of commands.")

    return 1

def clear():
    """Clear terminal window depending on OS"""
    # windows
    if os.name == "nt":
        os.system("cls")
    # UNIX/MacOS
    elif os.name == "posix":
        os.system("clear")

def display_fungi():
    clear()
    print("Current Environment: ", simulation_environment.environment, end="\n\n")
    print("-"*100)
    print("| Fungus | Size (cm3) | Adaptations")
    print("-"*100)
    i = 1
    for fungus in simulation_environment.fungi:
        print("|  ", i, "   |     ", fungus.size, "    | ", end="")
        print(fungus)
        print("-"*100)
        i += 1
    

def introduce():
    print("Hello, and welcome to the Fungi Auction simulation.")
    print("type \"HELP\" to see a list of commands.")

def about():
    #TODO   update about page
    print("This program is designed to be a helping aid to a simulation done in my AP Biology class.")
    print("The simulation's purpose was to assist students in the understanding of fungi and how")
    print("different fungi with different adaptations respond to environments. These adaptations,")
    print("which were selected from a list, were \"auctioned off\" and each group had a certain ammout")
    print("of money they could spend on adaptations.\n")
    print("While this simulation does not go into the auctioning portion of the activity, it simulates")
    print("the fungi and their responses to environments based on their adaptations.")

def get_input():
    try:
        return input("\n> ").upper()
    except KeyboardInterrupt:
        return -1
    except EOFError:
        return -1

def change_environment():
    simulation_environment.update_environment()
    display_fungi()
    print("Updated environment")

def add_adaptation():
    fungus_selection = int(input("Select a fungus:\n> "))

    if fungus_selection < 1 or fungus_selection > len(simulation_environment.fungi):
        display_fungi()
        print("Not a valid fungus")
        return
    else:
        clear()
        for i in range(9):
            print("| ", i+1, " | ", reference.adaptations[i])
        adaptation_selection = int(input("Select an adaptation:\n> "))
        
        if adaptation_selection < 1 or adaptation_selection > 9:
            display_fungi()
            print("Not a valid adaptation")
            return
        elif reference.adaptations[adaptation_selection-1] in simulation_environment.fungi[fungus_selection-1].adaptations:
            display_fungi()
            print("Fungus already has this adaptation")
            return
        else:
            simulation_environment.fungi[fungus_selection-1].add_adaptation(reference.adaptations[adaptation_selection-1])
            display_fungi()

def pass_time():
    for fungus in simulation_environment.fungi:
        fungus.pass_time()
    display_fungi()

def add_fungus():
    if len(simulation_environment.fungi) >= 9:
        print("Fungi limit reached")
    else:
        simulation_environment.add_fungus(Fungus())
        display_fungi()

def get_help():
    print(
        "ABOUT      Prints information about this program and its purpose",
        "CLEAR      Clears the screen of everything except the table of Fungi",
        "EXIT       Exits the program",
        "HELP       Prints this page",
        "NEWADAPT   Adds an adaptation to a fungus of choice",
        "NEWENV     Changes the current environment",
        "NEWF       Adds a basic fungus to the simulation",
        "PASSTIME   Spend a single unit of time with current fungi and environment",
        sep="\n"
    )

if __name__ == "__main__":
    main()

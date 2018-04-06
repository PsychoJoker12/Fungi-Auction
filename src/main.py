"""
driver class for fungus simulation
"""
from fungus import Fungus
from adaptation import Adaptation
from environment import Environment
from random import choice

import os

import reference

fungi = []
environment = choice(reference.environments)

fungus1_adaptations = list(reference.adaptations[i] for i in [2,4])

fungi.append(Fungus())
fungi.append(Fungus(fungus1_adaptations))

# update all fungi objects with the current environment
for fungus in fungi:
    fungus.update_environment(environment)

# ellapse time for each fungus 3 times (for testing purposes)
for fungus in fungi:
    for i in range(3):
        fungus.pass_time()

def main():
    clear()
    display_fungi()
    introduce()

    while True:
        command = get_input()
        display_fungi()

        if command == -1:
            return -1

        elif command == "NEWENV":
            change_environment()
        elif command == "CLEAR":
            pass
        elif command == "HELP":
            get_help()        
        elif command == "EXIT":
            break
        else:
            print("Unknown command, type \"Help\" to see a list of commands.")
    clear()
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
    print("Current Environment: {}\n".format(environment))
    for fungus in fungi:
        pass
    print("-"*100)

def introduce():
    print("Hello, and welcome to the Fungi Auction simulation.")
    print("type \"HELP\" to see a list of commands.")
                
def get_input():
    try:
        return input("\n> ").upper()
    except KeyboardInterrupt:
        print("\nUser forcably closed input stream. Exiting program")
        return -1
    except EOFError:
        print("\nUser forcably closed input stream. Exiting program")
        return -1

def change_environment():
    env = choice(reference.environments)
    environment = env
    print("Updated environment")

def get_help():
    print(
    "CLEAR      Clears the screen of everything except the table of Fungi",
    "EXIT       Exits the program",
    "HELP       Prints this page",
    sep="\n")

if __name__ == "__main__":
    main()

from models.FleetEngagement.FleetEngagement import FleetEngagement

# instantiate principle FleetEngagement object
test_battle = FleetEngagement()

# determine combatant nationalities
for i in test_battle.combatants.keys():
    test_battle.combatants[i]["NATIONALITY"] = test_battle.determineNationalities(i)
    input("\npress the ENTER key to continue...\n")

# determine combatants' respective fleet compositions
for i in test_battle.combatants.keys():
    test_battle.fleetComposition(i)    

input("pause...")
"""

def main():
    
    test_battle = FleetEngagement()

    # determine combatant nationalities
    test_battle.combatants[0]["NATIONALITY"] = test_battle.determineNationalities(0)
    input("\npress the ENTER key to continue...\n")
    
    test_battle.combatants[1]["NATIONALITY"] = test_battle.determineNationalities(1)
    input("\npress the ENTER key to continue...\n")
    
    for i in test_battle.combatants.keys():
        test_battle.fleetComposition(i)    


if __name__ == "__main__":
	main()

"""
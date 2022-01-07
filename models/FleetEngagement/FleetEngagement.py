import os

# from shipTypes.FleetFactor import Destroyer, Cruiser, BattleShip, PocketBattleShip, BattleCruiser

from formations.TaskForce import TaskForce
from formations.ShipInitializer import ShipInitializer


class FleetEngagement(object):
    """instantiates a fleet engagement between two nationalities, generates TFs as well as ship composition of those TFs"""

    nations_dict = ["GERMANY", "UNITED STATES", "ITALY", "JAPAN", "COMMONWEALTH", "FRANCE", "RUSSIA"]
    ship_classes_dict = ["DESTROYER", "CRUISER", "BATTLECRUISER", "POCKET BATTLESHIP", "BATTLESHIP"]

    def __init__(self):
        self.combatants = {0:{"short_designation": "sideA"}, 1:{"short_designation": "sideB"}}

    def determineNationalities(self,i):
        """lists for user potential nationalities to play as, returns selected nationality as string value"""

        loop_is_done = False
        while loop_is_done == False:

            # clear terminal screen
            os.system('cls' if os.name == 'nt' else 'clear')

            print("\nPlease choose a side for combatant {} from the following:\n".format(self.combatants[i]["short_designation"]))

            # iterate through nations_dict to list nation options to player
            for nation in FleetEngagement.nations_dict:
                print("\n" + nation)

            # player's input 'becomes' nationality
            print("\n")
            player_nationality = input().upper()

            # test to confirm player's selection is valid
            for nation in FleetEngagement.nations_dict:
                if nation == player_nationality:

                    # report player's nationality
                    print("\nYou have chosen " + player_nationality + "\n")

                    return player_nationality

                    loop_is_done = True

            # only print if user choice is invalid, and loop to continue
            print("\nPlayer choice is invalid.  Please confirm your choice is a listed nationality.")
            input("\npress the ENTER key to continue...\n")


    def fleetComposition(self, sideInt):
        """walks player through fleet composition for a given side, updates self.combatants[sideInt]"""

        # create list within combatants dict to hold each side's TFs
        self.combatants[sideInt]["fleet_composition"] = []

        # clear screen, set loop var
        os.system('cls' if os.name == 'nt' else 'clear')
        loop_is_done = False

        # loop to determine # of TFs
        while loop_is_done == False:

            # clear screen, ask "how many TFs" per side
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nFor {} ({}), how many task forces are involved?".format(self.combatants[sideInt]["NATIONALITY"], self.combatants[sideInt]["short_designation"]))
            print("\n")

            number_of_taskforces = input("")

            # bark at the user if their input is invalid (try and if not do the same thing...)
            try:

                if not isinstance(int(number_of_taskforces), int):
                    print("\nPlayer choice is invalid.\n\nPlease confirm your input is an integer equal to or greater than one.")
                    input("\npress the ENTER key to continue...\n")

            except ValueError:
                print("\nPlayer choice is invalid.\n\nPlease confirm your input is an integer equal to or greater than one.")
                input("\npress the ENTER key to continue...\n")                

            else:
                number_of_taskforces = int(number_of_taskforces)
                loop_is_done = True


        # for each TF, determine composition of TF and append to TF obj to FleetEngagement.combatants dict
        for current_tf in range(0, number_of_taskforces):
            os.system('cls' if os.name == 'nt' else 'clear')

            print("\nDetermining composition of {} ({}) taskforce {}...".format(self.combatants[sideInt]["NATIONALITY"], self.combatants[sideInt]["short_designation"], current_tf+1))
            print("\n")
            
            # create TF obj
            taskforce = TaskForce(self.combatants[sideInt]["NATIONALITY"], 0, "UNINVERTED", "FAST")

            # determine TF composition via TF class method 
            taskforce.taskforceComposition(self.combatants, sideInt, current_tf)
            
            # update TF speed
            taskforce.update_tf_speed()
            
            # update TF number of factors
            taskforce.total_naval_factors = taskforce.tf_total_factors()
            print("\nCurrent TF total number of naval factors: " + str(taskforce.total_naval_factors))

            # append TF obj to a given side's "fleet_composition" list
            self.combatants[sideInt]["fleet_composition"].append(taskforce)

    



        # determine forces

        # START OF NAVAL COMBAT ROUND
        #   form combat groups
        ####   carrier-based counterair attacks on enemy air bases
        ####   allocate unused carrier-based air units between Air Strikes and CAP
        ####   allocate land-based air units as Air Cover (convert AAF to AAS as necessary)
        #   Search for enemy combat groups
        #   Reveal found combat groups
        ####   Carrier-based air strikes against naval units at sea
        ####       surprise level
        ####       air combat with air cover
        ####       air combat with CAP
        ####       air defense of naval units
        ####       air strikes versus naval units
        ####   Land-based air attacks against naval units at sea
        ####       (convert AAF to AAS as necessary)
        ####       surprise level (ALWAYS NONE)
        ####       air combat with air cover
        ####       air combat with CAP
        ####       air defense of naval units
        ####       air strikes versus naval units
        #   Fleet combat
        #       Determine which combat groups will engage in fleet combat
        #       Divide ships into heavy, light, and screened
        #       Defender ranks heavy ships from largest to smallest, then light ships, then screened ships.
        #       Heavy ship combat
        #           Attacker selects targets for his heavy ships.
        #           Defender selects targets for his heavy ships.
        #           Resolve all heavy ship fire versus light ships and apply damage.
        #       Light ship combat
        #           Select targets for light ships of both sides.
        #           Resolve all fire versus all heavy ships.
        #           Resolve all light ship fire versus light ships.
        #       Screened ship combat
        #           Resolve all fire versus screened ships if permitted.
        #   Combat groups which engaged in fleet combat may be recombined
        #   Ship withdrawal
        #   Submarine attacks
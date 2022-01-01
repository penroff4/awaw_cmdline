from sys import argv

from models.researchDieRoller import researchDieRoller
from models.shipBuildingLaunchDate import shipBuildingLaunchDate

# import help

if __name__=="__main__":

        if len(argv) < 2 or argv[1] == "help":
            print("""

                Welcome to AWAW helper!

                to use, print on cmd line:
                    python awaw.py (command) [optional parameters]

                existing commands:
                  - "research_rolls"
                    * [number of research die rolls:int]

                  - "shipbuilding_launchdate"
                    * [Season:str]
                    * [Row:int]
                    * [Year construction started:int]
                    * [Construction Rate:str]

                  - "fleet_combat"
                """)


        elif argv[1] == "research_rolls":

            print("\n\nYou asked for research die rolls.\n")

            # need to confirm number of die rolls...

            # ...either via cmd line...
            try:
                if isinstance(int(argv[2]), int) & int(argv[2])>0:
                    requested_number_of_rolls = int(argv[2])

            # ...or prompt
            except:
                requested_number_of_rolls = int(input("How many sets of research die rolls do you need?\n"))

            # instantiate research_die_roller
            research_die_roller = researchDieRoller(requested_number_of_rolls)

            # run main from research_die_roller.py
            research_die_roller.main()


        elif argv[1] == "shipbuilding_launchdate":

            # if expected num of args entered (ie season, row, year, construction rate)
            if len(argv) == 6:

                ship_builder = shipBuildingLaunchDate(argv[2], None, argv[3], argv[4], argv[5], "cmd_line")

            else:
                ship_builder = shipBuildingLaunchDate(None, 0, 0, 0, 0, "text_input")

            ship_builder.setup()

            ship_builder.main()


        elif argv[1] == "fleet_combat":
            pass

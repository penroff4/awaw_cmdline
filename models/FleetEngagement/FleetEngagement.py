import os


class HeavyShip:
    """

    docstring for HeavyShip

    Capital ships and fast carriers are heavy ships
    """

    SHIP_WEIGHT = 'HEAVY'
    NAMED = True

    def __init__(self):
        pass


class LightShip:
    """

    docstring for LightShip

    Destroyers, cruisers, transports and CVEs are light ships.
    """

    SHIP_WEIGHT = 'LIGHT'
    NAMED = False

    def __init__(self):
        pass


class NavalChit:

    """

    docstring for NavalChit

    attributes:
        - number_of_naval_factors (NavalChit)

    """

    DMGED_SPEED = "SLOW"

    # Fleet Factor, Fast Carrier, or Strategic Warfare?
    NAVAL_CHIT_CLASS = ""

    SHIP_CLASS = ""
    SHIP_CLASS_SHORT = ""

    SPEED = ""

    # Heavy or Light?
    SHIP_WEIGHT = ""

    def __init__(self, number_of_factors=0, nationality="", hits=0):

        self.number_of_factors = number_of_factors
        self.nationality = nationality
        self.hits = hits

    def __str__(self):

        return NavalChit.SHIP_CLASS_SHORT + str(self.number_of_factors)

    def short_name(self):

        return self.nationality + " " + SHIP_CLASS_SHORT

    def long_name(self):

        return self.nationality + " " + self.number_of_factors + " factor " + SHIP_CLASS


class StrategicWarfareShip(NavalChit):
    """

    docstring for StrategicWarfareShip


    Asws, transports, submarines
    """
    
    NAVAL_CHIT_CLASS = "Strategic Warfare"

    def __init__(self):
        pass


class FastCarrier(HeavyShip, NavalChit):

    """
    docstring for FastCarrier
    """
    
    SPEED = "FAST"
    NAVAL_CHIT_CLASS = "Fast Carrier"

    SHIP_CLASS = "FAST CARRIER"
    SHIP_CLASS_SHORT = "FC"

    def __init__(self, number_of_factors):
        NavalChit.__init__(self, number_of_factors)
        self.naval_squadron_capacity = number_of_factors

    def __str__(self):
        return FastCarrier.SHIP_CLASS_SHORT + str(self.number_of_factors)


class LightCarrier(FastCarrier):

    """
    docstring for FastCarrier
    """

    SHIP_CLASS = "Light Carrier"
    SHIP_CLASS_SHORT = "CVL"
    
    def __init__(self, number_of_factors):
        FastCarrier.__init__(self, number_of_factors)
        self.naval_squadron_capacity = number_of_factors


class FleetCarrier(FastCarrier):

    """
    docstring for FastCarrier
    """

    SHIP_CLASS = "Fleet Carrier"
    SHIP_CLASS_SHORT = "CV"
    
    def __init__(self, number_of_factors):
        FastCarrier.__init__(self, number_of_factors)
        self.naval_squadron_capacity = number_of_factors


class SuperCarrier(FastCarrier):

    """
    docstring for FastCarrier
    """

    SHIP_CLASS = "Super Carrier"
    SHIP_CLASS_SHORT = "CVB"
    
    def __init__(self, number_of_factors):
        FastCarrier.__init__(self, number_of_factors)
        self.naval_squadron_capacity = number_of_factors


class EscortCarrier(LightShip, StrategicWarfareShip):
    
    SPEED = "SLOW"

    def __init__(self):
        pass


class Submarine(StrategicWarfareShip):
    
    SPEED = "FAST"
    
    def __init__(self):
        pass


class Asw(StrategicWarfareShip):
    
    SPEED = "FAST"
    
    def __init__(self):
        pass


class FleetFactor(NavalChit):

    """

    docstring for FleetFactor

    class attributes:
        - DMGED_SPEED = "SLOW" (NavalChit)
        - NAVAL_CHIT_CLASS (fleetFactor)

    object attributes:
        - number_of_factors (NavalChit)


    """

    NAVAL_CHIT_CLASS = "Fleet Factor"

    SHIP_CLASS = "FLEET FACTOR"
    SHIP_CLASS_SHORT = "FF"
    
    def __init__(self, number_of_factors):
        NavalChit.__init__(self, number_of_factors)

    def __str__(self):
        return FleetFactor.SHIP_CLASS_SHORT + str(self.number_of_factors)


class Destroyer(LightShip, FleetFactor):

    """

    docstring for destroyer

    """
    
    SPEED = "FAST"
    NUMBER_OF_FACTORS = 1
    SHIP_CLASS = "DESTROYER"
    SHIP_CLASS_SHORT = "DD"
    
    def __init__(self, number_of_factors):
        LightShip.__init__(self)
        FleetFactor.__init__(self, number_of_factors)

    def __str__(self):
        return Destroyer.SHIP_CLASS_SHORT + str(self.number_of_factors)

    def counter_title(self):
        return Destroyer.SHIP_CLASS_SHORT + str(self.number_of_factors)


class Cruiser(LightShip, FleetFactor):
    
    """

    docstring for cruiser

    """

    SPEED = "FAST"
    NUMBER_OF_FACTORS = 2
    SHIP_CLASS = "CRUISER"
    SHIP_CLASS_SHORT = "CA"
    
    def __init__(self, number_of_factors):
        LightShip.__init__(self)
        FleetFactor.__init__(self, number_of_factors)


    def __str__(self):
        return Cruiser.SHIP_CLASS_SHORT + str(NUMBER_OF_FACTORS)


class CapitalShip(HeavyShip, FleetFactor):

    """

    docstring for capitalShip

    """

    def __init__(self, number_of_factors, speed="FAST", name=""):
        HeavyShip.__init__(self)
        FleetFactor.__init__(self, number_of_factors)
        self.SPEED = speed
        self.vessel_name = name


class BattleShip(CapitalShip):

    """

    docstring for battleShip

    """

    SHIP_CLASS = "Battleship"
    SHIP_CLASS_SHORT = "BB"
    
    def __init__(self, number_of_factors, speed="FAST", name=""):
        CapitalShip.__init__(self, number_of_factors, speed, name)

    def __str__(self):
        return BattleShip.SHIP_CLASS_SHORT + str(self.number_of_factors)


class PocketBattleShip(CapitalShip):

    """

    docstring for pocketBattleShip

    """

    SHIP_CLASS = "Pocket Battleship"
    SHIP_CLASS_SHORT = "PB"

    def __init__(self, number_of_factors, speed="FAST", name=""):
        CapitalShip.__init__(self, number_of_factors, speed, name)

    def __str__(self):
        return PocketBattleShip.SHIP_CLASS_SHORT + str(self.number_of_factors)


class BattleCruiser(CapitalShip):

    """

    docstring for battleCruiser

    """

    SHIP_CLASS = "Battlecruiser"
    SHIP_CLASS_SHORT = "BC"

    def __init__(self, number_of_factors, speed="FAST", name=""):
        CapitalShip.__init__(self, number_of_factors, speed, name)

    def __str__(self):
        return BattleCruiser.SHIP_CLASS_SHORT + str(self.number_of_factors)


class ShipInitializer(object):
    
    """handles initialization and instantation calls for different ship classes"""

    def __init__(self, ship_class, number_of_factors, speed="", name=""):
        self.ship_class = ship_class.upper()
        self.number_of_factors = number_of_factors
        self.name = name
        self.speed = speed

    def create_ship(self):
        
        if self.ship_class == "DESTROYER":
            return Destroyer(self.number_of_factors)

        elif self.ship_class == "CRUISER":
            return Cruiser(self.number_of_factors)

        elif self.ship_class == "BATTLECRUISER":
            return BattleCruiser(self.number_of_factors, self.speed, self.name)         

        elif self.ship_class == "POCKET BATTLESHIP":
            return PocketBattleShip(self.number_of_factors, self.speed, self.name)

        elif self.ship_class == "BATTLESHIP":
            return BattleShip(self.number_of_factors, self.speed, self.name)


def shipComposition(ship, number_of_ship):
    """walks through ship composition, calls that ship's init func and returns object"""
    if ship == "DESTROYER" or ship == "CRUISER":

        for number in range(0, number_of_ship):

            if ship == "DESTROYER": 
                number_of_factors = number_of_ship * 1

            elif ship == "CRUISER":
                number_of_factors = number_of_ship * 2

            placeholder_ship = ShipInitializer(ship, number_of_factors)
            placeholder_ship = placeholder_ship.create_ship()
            return placeholder_ship # taskforce.assigned_ships.append(placeholder_ship)

    elif ship == "BATTLESHIP" or ship == "BATTLECRUISER" or ship == "POCKET BATTLESHIP":

        print("\nDetermining {} characteristics...\n".format(ship))

        # number of factors, speed, name
        for number in range(0, number_of_ship):

            print("\nFor {} {}:\nHow many naval factors is this {}?  \n\nPlease choose a number between 1 and 5.\n".format(ship, str(number+1), ship))
            number_of_factors = int(input())

            print("\nFor {} {}:\nWhat speed is this {}?  \n\nPlease choose FAST or SLOW.".format(ship, str(number+1), ship))
            speed = input().upper()

            print("\nFor {} {}:\nDoes this {} have a name?\n".format(ship, str(number+1), ship))
            name = input()

            placeholder_ship = ShipInitializer(ship, number_of_factors, speed, name).create_ship()

            return placeholder_ship


class NavalCombatRound(object):
    
    """docstring for NavalCombatRound"""

    def __init__(self, combatants_dict):
        self.combatants_dict = combatants_dict

    def form_combat_groups(self):
        """Each player secretly assigns combat group numbers to his participating TFs."""
        for combantant_int in self.combatants_dict:
            for taskforce in self.combatants_dict[combantant_int]:

                loop_is_done = False
                while loop_is_done == False:

                    try:
                        # clear screen
                        print("\nCombatant {} ({}):\n".format(
                            self.combatants_dict[combantant_int]["NATIONALITY"], self.combatants_dict[combantant_int]["short_designation"]))
                        print("\nFor TF {}, please assign to a combat group (between 1 and 6)".format(
                            self.combatants_dict[combantant_int]["fleet_composition"][taskforce]))
                        temp_combat_group = int(input())

                        if temp_combat_group > 0 and temp_combat_group < 7:

                            taskforce.combat_group = temp_combat_group

                        else:
                            raise ValueError

                        loop_is_done = True

                    except ValueError:
                        print(
                            "\nPlayer choice is invalid.\n\nPlease confirm your input is an integer equal to or greater than zero.")
                        input("\npress the ENTER key to continue...\n")


    def attack_enemy_air_bases(self):
        """
        Each player secretly allocates carrier-based NAS to CAP.  

        Remaining NAS may then coutner air enemy land-based air units (in a single round of air combat per counterair attack.

        Land-based air units not eliminated/aborted may participate in ensuing naval combat.

        """
        pass
    
    
    def allocate_carrier_air_to_air_strikes(self):
        """Carrier NAS (not assigned to CAP, not eliminated/aborted) may conduct air strikes against enemy naval units."""
        pass
    
    
    def allocate_land_based_air_to_air_cover(self):
        """

        Each side announces air cover by land-based air units by (secretly) assigning them to a specific combat group.

        Air units assigned to air cover may be used to defend that CG against enemy air units.

        Land based NAS commited to air cover may not search or attack enemy naval units this combat round.

        Search and attack AAS may not be used to fly air cover.

        """
        pass
    

    def search(self):
        """Each player rolls dice to determine his success in searching for his opponent's combat groups."""

        # for combatant
            # determine number of search rolls

                # SIMPLE METHOD
                    # player input number of search die

                # RAW method
                    # one die per land-based air squadron
                    # one die (and one fewer die for opponent) per tactical codebreaking card played (or via MAGIC intercept)
                    # one die per additional combat round
                    # one die for each friendly ACTIVE CG consisting of at least ten undamaged naval factors
                    # One die for each distant combat group containing at least one fully operational fast carrier at the start of combat round (no additional mod for active CGs containing fast carrier)

            # determine search results
                # each die which matches the number of an enemy CG achieves a search result against that CG
                # With one search result,
                    # CG is FOUND, and must reveal
                        # whether CG consists of less than ten naval factors
                        # how many fast carriers present in CG
                        # CG SPEED
                        # whether CG is carrying cargo
                # with multiple search results against a given CG
                    # CG may be attacked more than once equal to number of search results
                        # Air Strikes: For each search result against an active or distant enemy combat group, one air strike may be made against that combat group (23.72).
                        # Fleet Combat: For each search result against a distant enemy combat group, one active unpaired combat group may initiate fleet combat against that combat group (22.52). No search results are required for fleet combat between active combat groups and such fleet combat does not count against the limit on the number of air strikes.
                        # Effects Cumulative: The effects of search results are cumulative: two search results would allow any one of the following:
                            # Two air strikes against any combat group;
                            # Two fleet combats against a distant combat group; or
                            # One air strike and one fleet combat against a distant combat group.
                        # Submarine Attacks: Submarine attacks do not count against the limit on the number of times a found combat group may be attacked.

        pass
    
    def reveal_combat_groups(self):
        """

        For each combat group found, the owning player reveals:
            - whether CG consists of less than ten naval factors
            - how many fast carriers
            - CG speed (ie Fast or Slow)
            - whether "cargo" is present

        """
        pass

    def air_strikes_and_attacks(self):
        """

        Found enemy CGs may be attacked by land-based and carrier-based air units, in the following order:
            - One surprise carrier-based air strike per naval combat round
            - Non-surprise air strikes

        """
        pass


    def fleet_combat(self):
        """Fleet combat is resolved"""

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
        pass
     

    def submarine_attacks(self):
        """Submarine attacks are resolved"""
        pass


    def main(self):
        self.form_combat_groups()
        self.attack_enemy_air_bases()
        self.allocate_carrier_air_to_air_strikes()
        self.allocate_land_based_air_to_air_cover()
        self.search()
        self.reveal_combat_groups()
        self.air_strikes_and_attacks()
        self.fleet_combat()
        self.submarine_attacks()


class TaskForce(object):
    """represents a TF, essentially a list of ship objs with meta details"""

    # no more than 25 naval factors in a Task Force
    NAVAL_FACTOR_LIMIT = 25
    ship_classes_dict = ["DESTROYER", "CRUISER", "BATTLECRUISER", "POCKET BATTLESHIP", "BATTLESHIP"]


    def __init__(self, nationality="", total_naval_factors=0, status="", speed=""):
        self.nationality = nationality
        self.total_naval_factors = total_naval_factors
        self.status = status
        self.speed = speed
        self.assigned_ships = []
        self.combat_group = None

    
    def update_tf_speed(self):
        """look through ships in TF, if any are SLOW then TF is SLOW, else FAST"""

        ship_speeds = []

        for ship in self.assigned_ships:

            if ship.SPEED not in ship_speeds:

                ship_speeds.append(ship.SPEED)

        if "SLOW" in ship_speeds:

            self.speed = "SLOW"

        else: self.speed = ship_speeds[0]

    
    def tf_total_factors(self):
        """returns total naval factors in TF"""
        total_factors = 0
        
        for ship in self.assigned_ships:
            
            total_factors = total_factors + ship.number_of_factors

        return total_factors

    
    def distinct_ShipTypes(self):
        """Returns a list of distinct ship types in TF"""

        distinct_ShipTypes = []
        
        for ship in self.assigned_ships:

            if ship.SHIP_CLASS not in distinct_ShipTypes:

                distinct_ShipTypes.append(ship.SHIP_CLASS)

        return distinct_ShipTypes

    
    def append_to_tf(self, ship):
        """append ship obj to TF list ie self.assigned_ships"""
        self.assigned_ships.append(ship)


    def assign_combat_group(self, cg_id):
        """updates TF Combat Group value to match inputted cg_id"""
        self.combat_group = cg_id

    
    def taskforceComposition(self, combatants_dict, current_sideInt, current_tf_int):
        """walks player through composition of a given TF, returns TF object"""

        os.system('cls' if os.name == 'nt' else 'clear')

        player_ship_dict = {}

        print("For {} ({}) Taskforce {}...\n".format(combatants_dict[current_sideInt]["NATIONALITY"], combatants_dict[current_sideInt]["short_designation"], current_tf_int+1))

        for ship in TaskForce.ship_classes_dict:
     
            loop_is_done = False
            while loop_is_done == False:

                try:
                    print("\nHow many {}S are a part of taskforce {}?\n".format(ship, current_tf_int+1))

                    number_of_ship = int(input())
                    loop_is_done = True
                    
                except ValueError:
                    print("\nPlayer choice is invalid.\n\nPlease confirm your input is an integer equal to or greater than zero.")
                    input("\npress the ENTER key to continue...\n")

            player_ship_dict[ship] = number_of_ship

        for ship in player_ship_dict:

            if player_ship_dict[ship] > 0:

                self.append_to_tf(shipComposition(ship, player_ship_dict[ship]))


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

        # loop to determine # of TFs
        loop_is_done = False
        while loop_is_done == False:

            # clear screen, ask "how many TFs" per side
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nFor {} ({}), how many task forces are involved?".format(self.combatants[sideInt]["NATIONALITY"], self.combatants[sideInt]["short_designation"]))
            print("\n")
            number_of_taskforces = input("")

            # bark at the user if their input is invalid
            try:

                number_of_taskforces = int(number_of_taskforces)
                loop_is_done = True

            except ValueError:
                print("\nPlayer choice is invalid.\n\nPlease confirm your input is an integer equal to or greater than one.")
                input("\npress the ENTER key to continue...\n")                


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
            
            # append TF obj to a given side's "fleet_composition" list
            self.combatants[sideInt]["fleet_composition"].append(taskforce)


    def begin_naval_combat(self):
        # create combat round obj, feed FleetEngagement dict with TFs per side
        naval_combat_round = NavalCombatRound(self.combatants)

if __name__ == "__main__":
    pass

    



        # determine forces

        # START OF NAVAL COMBAT ROUND
        #   form combat groups
        # carrier-based counterair attacks on enemy air bases
        # allocate unused carrier-based air units between Air Strikes and CAP
        # allocate land-based air units as Air Cover (convert AAF to AAS as necessary)
        #   Search for enemy combat groups
        #   Reveal found combat groups
        # Carrier-based air strikes against naval units at sea
        # surprise level
        # air combat with air cover
        # air combat with CAP
        # air defense of naval units
        # air strikes versus naval units
        # Land-based air attacks against naval units at sea
        # (convert AAF to AAS as necessary)
        # surprise level (ALWAYS NONE)
        # air combat with air cover
        # air combat with CAP
        # air defense of naval units
        # air strikes versus naval units
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
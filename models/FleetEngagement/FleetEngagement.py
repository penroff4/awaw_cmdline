import os
import logging
from random import randint
# from socket import CMSG_SPACE
import pandas

### GLOBAL CONSTANTS ###

# set logging params
logging.basicConfig(
    filename="LogFleetEngagement.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)

# var controls logic for initiating air related segments of combat
# if false, air interactions not allowed and/or skipped
AIR_ALLOWED = False

NAVAL_ATTACK_TABLE = pandas.read_csv(
        "models/tables/navalAttackTablePivoted.csv")


############################## GLOBAL METHODS ##################################


def clear_screen():
    """calls os.system to clear screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def bad_choice(type):
    """inform user they've made a poor input choice"""
    if type == 'str':
        print("bad string choice")
    elif type == 'int':
        print("bad int chocie")

def aggregate_ships(ships_list):
    """accepts list of ship objects, returns total_factors"""
    total_factors = 0

    for ship in ships_list:
        total_factors = total_factors  + ship.factors
    
    return total_factors

def naval_attack_value(attack_type, squadrons_or_factors, die_roll):
    """
    Takes attack_type (air/fleet), number of fleet factors/air squadrons and die
    roll, returns naval attack table result int
    """

    try:
        if ( # type checks
            isinstance(attack_type, str) &
            isinstance(squadrons_or_factors, int) & 
            isinstance(die_roll, int)
        ):
            pass
        else:
            raise ValueError

        # carry out attack pattern
        if attack_type == "fleet":
            pass
        elif attack_type == "air":
            pass
        else:
            raise ValueError
    
    except ValueError:
        print("\nPlayer choice is invalid.\n\nPlease confirm your input is an integer equal to or greater than zero.")
        quit()

    # at the table intersection of fleet factors/air squadrons col and Die Roll...
    result = (
        NAVAL_ATTACK_TABLE.loc[(int(NAVAL_ATTACK_TABLE['FLEET FACTORS']) == squadrons_or_factors) & 
        (int(NAVAL_ATTACK_TABLE['DIE ROLL']) == die_roll)]
    )

    # return result
    result_val = result.loc[result['RESULT']]
    return result_val
    

############################## SHIP SIZE CLASSES ###############################
class HeavyShip(object):
    """

    docstring for HeavyShip

    Capital ships and fast carriers are heavy ships
    """

    SHIP_WEIGHT = 'HEAVY'
    NAMED = True

    def __init__(self):
        pass


class LightShip(object):
    """

    docstring for LightShip

    Destroyers, cruisers, transports and CVEs are light ships.
    """

    SHIP_WEIGHT = 'LIGHT'
    NAMED = False

    def __init__(self):
        pass


############################## NAVAL CHIT CLASSES ##############################
class NavalChit(object):

    """

    docstring for NavalChit

    attributes:
        - number_of_naval_factors (NavalChit)

    """

    DMGED_SPEED = "SLOW"

    # Fleet Factor, Fast Carrier, or Strategic Warfare?
    SHIP_META_CLASS = ""

    SHIP_CLASS = ""
    SHIP_CLASS_SHORT = ""

    SPEED = ""

    # Heavy or Light?
    SHIP_WEIGHT = ""

    def __init__(self, number_of_factors=0, nationality="", hits=0):

        self.number_of_factors = number_of_factors
        self.nationality = nationality
        self.hits = hits
        # self.status = ''

    def __str__(self):

        return NavalChit.SHIP_CLASS_SHORT + str(self.number_of_factors)

    def short_name(self):

        return self.nationality + " " + SHIP_CLASS_SHORT

    def long_name(self):

        return self.nationality + " " + self.number_of_factors + " factor " + SHIP_CLASS


########################## STRATEGIC WARFARE CLASSES ###########################
class StrategicWarfareShip(NavalChit):
    """

    docstring for StrategicWarfareShip


    Asws, transports, submarines
    """

    SHIP_META_CLASS = "Strategic Warfare"

    def __init__(self):
        pass


class Transport(LightShip, StrategicWarfareShip):

    SPEED = "SLOW"

    def __init__(self):
        pass


class Asw(StrategicWarfareShip):

    SPEED = "FAST"

    def __init__(self):
        pass


class Submarine(StrategicWarfareShip):

    SPEED = "FAST"

    def __init__(self):
        pass


############################# CARRIER AIR CLASSES ##############################
class FastCarrier(HeavyShip, NavalChit):

    """
    docstring for FastCarrier
    """

    SPEED = "FAST"
    SHIP_META_CLASS = "Fast Carrier"

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


############################# FLEET FACTOR CLASSES #############################
class FleetFactor(NavalChit):

    """

    docstring for FleetFactor

    class attributes:
        - DMGED_SPEED = "SLOW" (NavalChit)
        - NAVAL_CHIT_CLASS (fleetFactor)

    object attributes:
        - number_of_factors (NavalChit)


    """

    SHIP_META_CLASS = "Fleet Factor"

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
        return Cruiser.SHIP_CLASS_SHORT + str(self.number_of_factors)


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


############################# SHIP RENDER CLASSES ##############################
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
    """walks through ship composition, creates ShipInitializer to handle final instanitation details"""
    if ship == "DESTROYER" or ship == "CRUISER":

        for number in range(0, number_of_ship):

            if ship == "DESTROYER":
                number_of_factors = number_of_ship * 1

            elif ship == "CRUISER":
                number_of_factors = number_of_ship * 2

            placeholder_ship = ShipInitializer(ship, number_of_factors)
            placeholder_ship = placeholder_ship.create_ship()
            # taskforce.assigned_ships.append(placeholder_ship)
            return placeholder_ship

    elif ship == "BATTLESHIP" or ship == "BATTLECRUISER" or ship == "POCKET BATTLESHIP":

        print("\nDetermining {} characteristics...\n".format(ship))

        # number of factors, speed, name
        for number in range(0, number_of_ship):

            print("\nFor {} {}:\nHow many naval factors is this {}?  \n\nPlease choose a number between 1 and 5.\n".format(
                ship, str(number+1), ship))
            number_of_factors = int(input())

            print("\nFor {} {}:\nWhat speed is this {}?  \n\nPlease choose FAST or SLOW.".format(
                ship, str(number+1), ship))
            speed = input().upper()

            print("\nFor {} {}:\nDoes this {} have a name?\n".format(
                ship, str(number+1), ship))
            name = input()

            placeholder_ship = ShipInitializer(
                ship, number_of_factors, speed, name).create_ship()

            return placeholder_ship

####################### ENGAGEMENT AND FORMATION CLASSES #######################
class FleetCombat(object):
    """object to handle for FleetCombat"""

    def resolve_naval_attack(self, attacker_naval_drm=0, defender_naval_drm=0, attacker_special_activity=0, defender_special_activity=0):

        attacker_naval_drm = attacker_naval_drm
        defender_naval_drm = defender_naval_drm
        attacker_special_activity = attacker_special_activity
        defender_special_activity = defender_special_activity

        two_d6_roll = randint(2, 12)
        two_d6_roll_after_mods = two_d6_roll + attacker_naval_drm - \
            defender_naval_drm - attacker_special_activity + defender_special_activity

        if two_d6_roll_after_mods < 2:
            two_d6_roll_after_mods = 2

        pass

    def __init__(self, combatants_dict):
        self.combatants_dict = combatants_dict
        self.combat_group_pairings = {}

    def pair_off_combat_groups(self):
        pass

    def capital_ship_combat_pairing_off(self):
        # opposing capital ships pair off
        #    larger ships ranked higher than smaller ships
        #    faster ships trump slower ships of same size
        #    ships with fewer accumulated hits trump same size, same speed ships
        #    ships with higher Naval Nationality DRM trump ect
        # ships then pair off one to one
        pass

    def surplus_capital_ships_select_targets(self):
        #     surplus capital ships may either
        #         join a friendly capital ship firing on an opposing ship
        #         Fire on opposing light ships
        #         hold fire in hope of firing on opposing screened ships
        pass

    def resolve_capital_ship_fire(self):
        # capital ship fire resolved using Naval Attack Table
        #     A capital ship which is targeted by one or more opposing capital ships must fire against one of the capital ships firing at it.
        #     all enemy light ships treated as single target
        #     light ships sunk by capital ship fire removed from board
        #     cruisiers dmged from capital ship fire automatically screened and need not be sunk to permit fire on other screened ships (22.54G).
        pass

    def light_ships_combat_pairing_off(self):
        # After capital ship fire resolved...
        #     surivivng, undmged opposing light ships pair off
        #     opposing light ships pair off at ratio of up to 3:1 of light ship factors
        #     If one side has more than three times as many light ship factors as the other, that side is considered to have “surplus light ships”.
        pass

    def surplus_light_ships_select_targets(self):
        # surplus light ships may either:
        #     Join with friendly light ships in firing at the opposing light ships
        #     Fire on one or more opposing capital ships, including those that have already been subject to capital ship fire.
        #         A single capital ship may be attacked by any number of surplus light ships;
        #         A second capital ship may only be attacked if the first capital ship is attacked by at least an equal number of surplus light ship factors (so seven surplus light ship factors could attack an opposing four-factor battleship with four, five, six or all seven factors; or up to three surplus light ship factors could instead attack a second opposing four-factor battleship).
        #     Hold their fire in the hope of firing on opposing screened ships.
        pass

    def resolve_light_ship_fire(self):
        pass

    def resolve_fire_against_screened_ships(self):
        # Fire is then resolved against any screened ships selected as targets by capital and light ships that have withheld their fire.
        #     Fire against screened ships is permitted only if all other enemy capital and light ships, other than cruisers damaged by capital ship fire earlier in the round (22.54C), have been sunk by capital ship and light fire.
        #     Screened named ships are targeted individually; screened light ships are targeted as a group.
        #     Capital ships fire first, then the light ships. Capital and light ships which target the same screened ship or group of screened light ships fire in sequence. Light ships select their targets after capital ship fire is resolved.
        #     Screened ships do not fire back (22.531C).
        pass

    def resolve_fleet_combat(self, combat_group_pairing):
        # ship categories in fleet combat
        #    Capital Ships
        #    Lightships
        #    Screened ships
        pass

    def main(self):
        #   Fleet combat
        #       Determine which combat groups will engage in fleet combat
        #           Active combat groups with the same combat group number pair off in fleet combat.
        #           Starting with the lowest numbered unpaired combat group, each active unpaired combat group then pairs off with the next highest unpaired opposing active combat group, until one side has all its active combat groups paired.
        #           Fleet combat is then resolved for these engagements.
        #           Each active combat group which either did not engage in fleet combat with an opposing active combat group or which sank all the naval units in an opposing active combat group it engaged in fleet combat may then engage in fleet combat with:
        #               An opposing active combat group (both fast and slow unpaired active combat groups); or
        #               An opposing distant combat group found by a search roll (fast unpaired active combat groups only).
        #           Fleet combat is then resolved for these engagements.
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

        self.pair_off_combat_groups()
        for combat_group_pairing in self.combat_group_pairings:
            self.resolve_fleet_combat(combat_group_pairing)

        pass


class Combatant(object):
    """i.e. a player, or nation; handles combatant details"""
    def __init__(self, short_designation):
        self.short_designation = short_designation
        self.nationality = None
        self.national_adjective = None
        self.fleet_composition = []
        # self.current_round_search_rolls = []
        self.combatant_round_search_results = 0
        self.search_rolls_list = []
        self.withdrawal_decision = None
        self.allocated_search_results_list = []


class NavalCombatRound(object):
    """represents and executes through all Naval Combat Round segments"""

    def __init__(self, combatants_dict, combat_round_number):
        self.combatants_dict = combatants_dict
        self.combat_round_number = combat_round_number
        self.round_total_search_results = 0

    def begin_naval_combat_round(self):
        """handles any pre-segment work for naval combat round"""
        clear_screen()

        # print("Combatant fleets determined...")

        print("\nBeginning fleet engagement...")

        input("\npress the ENTER key to continue...\n\n")

    def form_combat_groups(self):
        """
        Each player secretly assigns  his participating TFs to a Combat Group.
        """
        clear_screen()

        for combatant_int in self.combatants_dict:
            for taskforce_int in range(0, len(self.combatants_dict[combatant_int].fleet_composition)):

                loop_is_done = False
                while loop_is_done == False:

                    try:
                        clear_screen()

                        print("\nCombatant {} ({}):\n".format(
                            self.combatants_dict[combatant_int].nationality,
                            self.combatants_dict[combatant_int].short_designation))

                        print("\nFor TF {}, please assign to a combat group (between 1 and 6)\n".format(
                            self.combatants_dict[combatant_int].fleet_composition[taskforce_int].number))

                        temp_combat_group = int(input())

                        if temp_combat_group > 0 and temp_combat_group < 7:

                            # set TF combat group value
                            self.combatants_dict[combatant_int].fleet_composition[taskforce_int].combat_group = temp_combat_group

                            # update TF's 'combat group' status, ie whether it's an Active, Distant, or Pending CG
                            # reserved for TFs which have not yet joined combat
                            if self.combatants_dict[combatant_int].fleet_composition[taskforce_int].combat_group == 0:
                                self.combatants_dict[combatant_int].fleet_composition[taskforce_int].combat_group_combat_status = "PENDING"

                            elif self.combatants_dict[combatant_int].fleet_composition[taskforce_int].combat_group <= self.combat_round_number:
                                self.combatants_dict[combatant_int].fleet_composition[taskforce_int].combat_group_combat_status = "ACTIVE"

                            elif self.combatants_dict[combatant_int].fleet_composition[taskforce_int].combat_group > self.combat_round_number:
                                self.combatants_dict[combatant_int].fleet_composition[taskforce_int].combat_group_combat_status = "DISTANT"

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

    def allocate_carrier_air_strikes(self):
        """Carrier NAS (not assigned to CAP, not eliminated/aborted) may conduct air strikes against enemy naval units."""
        pass

    def allocate_land_based_air_cover(self):
        """

        Each side announces air cover by land-based air units by (secretly) assigning them to a specific combat group.

        Air units assigned to air cover may be used to defend that CG against enemy air units.

        Land based NAS commited to air cover may not search or attack enemy naval units this combat round.

        Search and attack AAS may not be used to fly air cover.

        """
        pass

    def roll_search_die(self, method="simple"):
        """
        simple method rolls player inputted number of dice, updates combatants
        search_rolls_list, combatant_round_search_results
        """

        clear_screen()
        print("Combat groups assigned...\n")
        print("\nInitializing search rolls...")

        # player input number of search die
        if method == "simple":
            # for each combatant, request player inputted number of search die
            for combatant_int in self.combatants_dict:

                loop_is_done = False
                while loop_is_done == False:

                    try:
                        clear_screen()

                        print("For {} ({})...\n".format(
                            self.combatants_dict[combatant_int].nationality,
                            self.combatants_dict[combatant_int].short_designation))

                        print("How many search die does your side receive?\n\n")
                        number_of_die = int(input())
                        loop_is_done = True

                    except ValueError:
                        print("\nPlayer choice is invalid.\n\nPlease confirm your input is an integer equal to or greater than zero.")
                        input("\npress the ENTER key to continue...\n")

                # 'clear' a given combatants search_rolls_list
                self.combatants_dict[combatant_int].search_rolls_list = []

                # roll determined number of search die, append to combatants
                # search_rolls_list
                for i in range(0, number_of_die):
                    self.combatants_dict[combatant_int].search_rolls_list.append(randint(1, 6))

        # use Rules as Written to determine number of search die
        elif method == "RAW":
            # RAW method
            # one die per land-based air squadron
            # one die (and one fewer die for opponent) per tactical codebreaking card played (or via MAGIC intercept)
            # one die per additional combat round
            # one die for each friendly ACTIVE CG consisting of at least ten undamaged naval factors
            # One die for each distant combat group containing at least one fully operational fast carrier at the start of combat round (no additional mod for active CGs containing fast carrier)
            pass

    def search_results(self):
        """search_results docsttring"""

        clear_screen()
        print("Search rolls performed.  Determining search results...\n")
        input("\npress the ENTER key to continue...\n\n")

        # reset search results for current round to 0
        self.round_total_search_results = 0

        # for each combatant, determine search results (compare search rolls against opponent CG nums)
        for combatant_int in self.combatants_dict:

            # set opponent combatant int ie identifier, assumes combat is always 1v1
            if combatant_int == 0:
                opponent_int = 1
            elif combatant_int == 1:
                opponent_int = 0

            search_results = 0

            # compare search die against combat group identifier
            for search_roll in self.combatants_dict[combatant_int].search_rolls_list:

                # note 'combat group' is actually a Taskforce object
                for enemy_combat_group in self.combatants_dict[opponent_int].fleet_composition:

                    # if search roll matches combat group, set CG as FOUND
                    if search_roll == enemy_combat_group.combat_group:

                        # update enemy CG search status
                        enemy_combat_group.combat_group_search_status = "FOUND"
                        enemy_combat_group.current_naval_round_number_of_search_results_against = enemy_combat_group.current_naval_round_number_of_search_results_against + 1

                        # increment number of search results
                        search_results = search_results + 1

            # tally combatant's distinct found enemy CGs
            distinct_found_enemy_cgs = 0
            for enemy_combat_group in self.combatants_dict[opponent_int].fleet_composition:
                if enemy_combat_group.combat_group_search_status == "FOUND":
                    distinct_found_enemy_cgs = distinct_found_enemy_cgs + 1

            self.combatants_dict[combatant_int].combatant_round_search_results = search_results
            self.round_total_search_results = self.round_total_search_results + search_results

    def print_found_cg_info(self, opp_national_adj, current_enemy_combat_group):
        # if enemy cg is FOUND
        if current_enemy_combat_group.combat_group_search_status == "FOUND":

            # determine # of Fast Carriers in CG
            tf_meta_class_count_dict = current_enemy_combat_group.ships_meta_class_count_dict()
            tf_fast_carrier_count = 0

            for ship_meta_class in tf_meta_class_count_dict:
                if ship_meta_class == "Fast Carrier":
                    tf_fast_carrier_count = tf_fast_carrier_count + 1

                        # set combat group status re: # of factors
            if current_enemy_combat_group.tf_less_than_ten_naval_factors() is True:
                cg_ten_factor_status = "Combat Group consists of less than ten naval factors"
            else:
                cg_ten_factor_status = "Combat Group consists of ten or more naval factors"

            # set report on combat group speed
            cg_speed = current_enemy_combat_group.speed

            # check cg has cargo status
            if current_enemy_combat_group.escorting_cargo is True:
                combat_group_carrying_cargo_status = "Cargo present"
            else:
                combat_group_carrying_cargo_status = "Cargo not present"

            cg_combat_status = current_enemy_combat_group.combat_group_combat_status

            # print cg, search results against cg, known cg data
            print("\n - {} Combat Group {} ({} search result(s) against)".format(
                opp_national_adj, current_enemy_combat_group.combat_group, current_enemy_combat_group.current_naval_round_number_of_search_results_against))
            # whether CG is DISTANT, has ten+ naval factors, has fast carriers, speed, has cargo
            print("    * {}".format(cg_combat_status))
            print("    * {}".format(cg_ten_factor_status))
            print("    * {} fast carriers present".format(tf_fast_carrier_count))
            print("    * {} combat group".format(cg_speed))
            print("    * {}".format(combat_group_carrying_cargo_status))

    def reveal_combat_groups(self):
        """reveal combat groups, and number of search results per side"""

        # for each player...
        for combatant_int in self.combatants_dict:

            # set opponent combatant int, assumes combat is always 1v1
            if combatant_int == 0:
                opponent_int = 1
            elif combatant_int == 1:
                opponent_int = 0

            clear_screen()

            print("For {} ({})...\n\n".format(
                self.combatants_dict[combatant_int].nationality,
                self.combatants_dict[combatant_int].short_designation))

            print("Search die rolls are as follow...\n\n")
            for die_roll in self.combatants_dict[combatant_int].search_rolls_list:
                print("{}...\n\n".format(die_roll))

            print("{} total search result(s) achieved...\n".format(
                self.combatants_dict[combatant_int].combatant_round_search_results))

            # if any enemy combat groups found...(list found enemy CGs)
            if self.combatants_dict[combatant_int].combatant_round_search_results >= 1:

                print("\nFOUND enemy Combat Groups:")

                # for each enemy combat group in enemy combatant fleet composition dict...
                for enemy_combat_group_int in range(0, len(self.combatants_dict[opponent_int].fleet_composition)):

                    # set current_enemy_combat_group var for shorthand
                    current_enemy_combat_group = self.combatants_dict[opponent_int].fleet_composition[enemy_combat_group_int]
                    national_adjective = self.combatants_dict[opponent_int].national_adjective

                    # call class meth for printing relevant FOUND CG info
                    self.print_found_cg_info(national_adjective, current_enemy_combat_group)

            print("\n\nHIDDEN enemy combat groups:\n")
            hidden_enemy_combat_groups = 0

            # for each cg in enemy fleet
            for enemy_combat_group_int in range(0, len(self.combatants_dict[opponent_int].fleet_composition)):

                # if CG is HIDDEN
                if self.combatants_dict[opponent_int].fleet_composition[enemy_combat_group_int].combat_group_search_status == "HIDDEN":

                    hidden_enemy_combat_groups = hidden_enemy_combat_groups + 1

                    # list CG on screen
                    print("* {} Combat Group {}\n\n".format(
                        self.combatants_dict[opponent_int].national_adjective,
                        self.combatants_dict[opponent_int].fleet_composition[enemy_combat_group_int].combat_group))

            if hidden_enemy_combat_groups == 0:
                print("...there are currently no hidden enemy combat groups...\n\n")

            print("Press enter to continue...\n\n")
            input()

    def no_search_results_present(self):
        """handles interaction if neither side has achieved search results"""
        clear_screen()
            
        print("\nNo search results achieved by either side...\n")
        print("\nPress enter to continue...")
        input()

    def round_has_search_results(self):
        """
        sets round_has_search_results to False, evaluates combatant_dict
        and updates round_has_search_results 
        True
        """
        self.round_has_search_results = False

        for combatant_int in self.combatants_dict: 
    
            if self.combatants_dict[combatant_int].combatant_round_search_results > 0:
                self.round_has_search_results = True

    def allocate_search_results(self):
        """
        updates a dict tying (ie targeting) enemy combat 
        groups to achieved search results
        """
        for combatant_int in self.combatants_dict:

            # relabel for shorthand
            combatant = self.combatants_dict[combatant_int]

            # set opponent_int, assumes fleet engagements are always 1v1
            if combatant_int == 0:
                opponent_int = 1
            elif combatant_int == 1:
                opponent_int = 0
            
            # if combatant has search results...
            if combatant.combatant_round_search_results > 0:

                clear_screen()

                print("Allocating search results for {} ({})...".format(combatant.nationality, combatant.short_designation))
                
                # loop through enemy combat groups...
                for combat_group in self.combatants_dict[opponent_int].fleet_composition:

                    # list them if they're currently FOUND
                    if combat_group.combat_group_search_status == "FOUND":

                        national_adjective = self.combatants_dict[opponent_int].national_adjective
                        self.print_found_cg_info(national_adjective, combat_group)
                
                        # for each search result that CG has against it...
                        for result_int in range(0, combat_group.current_naval_round_number_of_search_results_against):
                    
                            loop_is_done = False
                            while loop_is_done is False:
                            
                                try:

                                    print("\nFor search result {}...".format(result_int+1))

                                    print("\nWhat method of attack do you wish to use for this search result?")
                                    print("\nPlease choose air or fleet.\n")
                                    print("\nNote:")
                                    print("\n  Only DISTANT enemy combat groups may be chosen for FLEET combat.")
                                    print("\n  ACTIVE enemy combat fleets may still be chosen for regular fleet combat later.\n")
                                    print("\n  Active enemy combat groups may still be chosen for air strikes.")
                                    
                                    # upper case user string input
                                    attack_method = input().upper()

                                    # confirm user input is proper value
                                    if (
                                        attack_method != "AIR" and 
                                        attack_method != "FLEET"
                                    ) or (
                                        attack_method == "FLEET" and
                                        combat_group.combat_group_combat_status == "ACTIVE"
                                    ):
                                        raise ValueError

                                    loop_is_done = True

                                except ValueError:
                                    # currently not correct, should push user into loop to make correct choice
                                    print("\nPlayer choice is invalid.  Please confirm your choice is appropriate.")
                                    input("\npress the ENTER key to continue...\n")

                            # update combatant's allocated search results list
                            self.combatants_dict[combatant_int].allocated_search_results_list.append({
                                'target_cg':combat_group.number, 
                                'method': attack_method,
                                })
            
    def air_strikes_attacks(self):
        """

        Found enemy CGs may be attacked by land-based and carrier-based air units, in the following order:
            - One surprise carrier-based air strike per naval combat round
            - Non-surprise air strikes

        """
        clear_screen()
        print("Proceeding to air strikes/attacks phase...\n\n")
        print("Please press enter to continue...\n\n")
        input()

        for combatant_int in self.combatants_dict:
            for allocated_result in self.combatants_dict[combatant_int].allocated_search_results_list:
                if allocated_result["method"] == "AIR":
                    pass

    def fleet_combat(self):
        """Fleet combat is resolved"""

        clear_screen()
        print("Search results achieved...Proceeding to fleet combat phase...\n\n")
        print("Press enter to continue...\n\n")
        input()

        # NOTE: 22.52 RULES OF ENGAGEMENT: Fleet combat must involve at least one active combat group, and may only be avoided if one side evades fleet combat (22.523).

        for combatant_int in self.combatants_dict:

            if self.combatants_dict[combatant_int].combatant_round_search_results < 1:
                # for enemy_combat_group in list_of_enemy_combat_groups

                pass

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

    def determine_combat_round_loser(self):
        """determines 'loser' of combat based on lost naval factors (and hits for ties)"""
        # The loser of the previous round of naval combat announces his intention first
        #     the loser is the player who lost more naval factors in the previous round of naval combat;
        #     if tied, the player who had more naval factors damaged;
        #     if still tied, the intercepting player).

        pass

    def end_combat_round_check(self):
        """for each combatant, updates withdrawal_decision to 1 if withdraws"""

        for combatant_int in self.combatants_dict:

            loop_is_done = False
            while loop_is_done is False:
                # resets withdrawal_decision to 0
                self.combatants_dict[combatant_int].withdrawal_decision = 0

                try:
                    clear_screen()
                    print("\nEnd of Naval Combat Round {}.\n".format(self.combat_round_number))
                    
                    print ("{}, do you want to continue?\n".format(self.combatants_dict[combatant_int].nationality))
                    print("Please choose Yes or No\n\n")
                    
                    player_withdrawal_decision = input().upper()
                    
                    if player_withdrawal_decision == "YES":
                        self.combatants_dict[combatant_int].withdrawal_decision = 0
                    elif player_withdrawal_decision == "NO":
                        self.combatants_dict[combatant_int].withdrawal_decision = 1
                    else:
                        raise ValueError

                    loop_is_done = True
                
                except ValueError:
                    print("\nPlayer choice is invalid.  Please confirm your choice is a listed nationality.")
                    input("\npress the ENTER key to continue...\n")

    def end_naval_combat_round(self):
        """
        ends naval combat round if either combatant has withdrawal_decision set 
        as 1
        """
        clear_screen()

        # an extra for loop so as to update both players withdrawal decisions
        # and THEN reveal withdrawal choices
        for combatant_int in self.combatants_dict:
            if self.combatants_dict[combatant_int].withdrawal_decision == 1:
                print("{} ({}) has elected to withdraw.\n".format(
                    self.combatants_dict[combatant_int].nationality,
                    self.combatants_dict[combatant_int].short_designation))

                print("Press enter to continue...\n")
                input()
                quit()
    
    def main(self):
        
        self.begin_naval_combat_round()

        self.form_combat_groups()

        if AIR_ALLOWED is True:
            self.attack_enemy_air_bases()
            self.allocate_carrier_air_strikes()
            self.allocate_land_based_air_cover()

        # call search function using 'simple' procedure
        self.roll_search_die("simple")

        # determines if search rolls achieve search results
        self.search_results()

        # 'Reveal' FOUND combat groups, list HIDDEN combat groups to user
        self.reveal_combat_groups()

        # update self.round_has_search_results
        self.round_has_search_results()

        # if search results present for either side...
        if self.round_has_search_results is True:

            # players allocate search results
            self.allocate_search_results()

            if AIR_ALLOWED is True:
                self.air_strikes_attacks()
                
            self.fleet_combat()

            self.submarine_attacks()
        
        else:
            self.no_search_results_present()

        self.determine_combat_round_loser()

        self.end_combat_round_check()

        self.end_naval_combat_round()


class TaskForce(object):
    """represents a TF, essentially a list of ship objs with meta details"""

    # no more than 25 naval factors in a Task Force
    NAVAL_FACTOR_LIMIT = 25
    ship_classes_list = [
        "DESTROYER", "CRUISER",
        "BATTLECRUISER", "POCKET BATTLESHIP", "BATTLESHIP"
    ]

    def __init__(self, nationality="", total_naval_factors=0, status="", speed="", number=0):
        self.nationality = nationality
        self.total_naval_factors = total_naval_factors
        self.naval_nationality_drm = 0
        self.status = status
        self.speed = speed
        self.assigned_ships = []
        self.combat_group = None
        self.combat_group_search_status = "HIDDEN"
        self.combat_group_combat_status = ""
        self.current_naval_round_number_of_search_results_against = 0
        self.escorting_cargo = False
        self.number = number
        self.name = "{} TF {}".format(self.nationality, self.number)
        self.name_long = "{} Task Force {}".format(
            self.nationality, self.number)

    def update_tf_speed(self):
        """look through ships in TF, if any are SLOW then TF is SLOW, else FAST"""

        ship_speeds = []

        for ship in self.assigned_ships:

            if ship.SPEED not in ship_speeds:

                ship_speeds.append(ship.SPEED)

        if "SLOW" in ship_speeds:

            self.speed = "SLOW"

        else:
            self.speed = ship_speeds[0]

    def tf_total_factors(self):
        """returns total naval factors in TF"""
        total_factors = 0

        for ship in self.assigned_ships:

            total_factors = total_factors + ship.number_of_factors

        return total_factors

    def tf_less_than_ten_naval_factors(self):
        """returns total naval factors in TF"""
        if self.tf_total_factors() < 10:
            return True
        else:
            return False

    def distinct_ShipClasses(self):
        """Returns a list of distinct ship class in TF"""

        distinct_ShipClasses = []

        for ship in self.assigned_ships:

            if ship.SHIP_CLASS not in distinct_ShipClasses:

                distinct_ShipClasses.append(ship.SHIP_CLASS)

        return distinct_ShipClasses

    def distinct_ShipMetaClasses(self):
        """Returns a list of distinct ship meta classes in TF"""

        distinct_ShipMetaClasses = []

        for ship in self.assigned_ships:

            if ship.SHIP_META_CLASS not in distinct_ShipMetaClasses:

                distinct_ShipMetaClasses.append(ship.SHIP_META_CLASS)

        return distinct_ShipMetaClasses

    def ships_type_count_dict(self):
        """returns a dict of ship types and their number within TF"""
        tf_ship_types_and_count_dict = {}

        # fill tf_ship_types_and_count_dict with keys
        for shiptype in self.distinct_ShipClasses():
            tf_ship_types_and_count_dict[shiptype] = 0

        # update relevant ship count values for keys in dict
        for ship in self.assigned_ships:

            tf_ship_types_and_count_dict[ship] = tf_ship_types_and_count_dict[ship] + 1

        return tf_ship_types_and_count_dict

    def ships_meta_class_count_dict(self):
        """returns a dict of ship meta classes and their number within TF"""
        tf_ship_meta_classes_and_count_dict = {}

        for shipMetaClass in self.distinct_ShipMetaClasses():
            tf_ship_meta_classes_and_count_dict[shipMetaClass] = 0

        for ship in self.assigned_ships:

            tf_ship_meta_classes_and_count_dict[ship.SHIP_META_CLASS] = tf_ship_meta_classes_and_count_dict[ship.SHIP_META_CLASS] + 1

        return tf_ship_meta_classes_and_count_dict

    def append_to_tf(self, ship):
        """append ship obj to TF list ie self.assigned_ships"""
        self.assigned_ships.append(ship)

    def assign_combat_group(self, cg_id):
        """updates TF Combat Group value to match inputted cg_id"""
        self.combat_group = cg_id

    def taskforceComposition(self, combatants_dict, current_sideInt):
        """walks player through composition of a given TF, returns TF object"""

        clear_screen()

        player_ship_dict = {}

        print("For {} ({}) Taskforce {}...\n".format(
            combatants_dict[current_sideInt].national_adjective,
            combatants_dict[current_sideInt].short_designation,
            self.number
        ))

        for ship in TaskForce.ship_classes_list:

            loop_is_done = False
            while loop_is_done == False:

                try:
                    print(
                        "\n\nHow many {}S are a part of this taskforce?\n".format(ship))

                    number_of_ship = int(input())
                    loop_is_done = True

                except ValueError:
                    print(
                        "\nPlayer choice is invalid.\n\nPlease confirm your input is an integer equal to or greater than zero.")

                    input("\npress the ENTER key to continue...\n")

            player_ship_dict[ship] = number_of_ship

        for ship in player_ship_dict:

            if player_ship_dict[ship] > 0:

                self.append_to_tf(shipComposition(
                    ship, player_ship_dict[ship]))


class FleetEngagement(object):
    """
    a fleet engagement between two nationalities, 
    generates TFs as well as ship composition of those TFs
    """

    nations_list = [
        "GERMANY",
        "UNITED STATES",
        "ITALY",
        "JAPAN",
        "COMMONWEALTH",
        "FRANCE",
        "RUSSIA",
    ]

    nations_adjective_dict = {
        "GERMANY": "GERMAN",
        "UNITED STATES": "AMERICAN",
        "ITALY": "ITALIAN",
        "JAPAN": "JAPANESE",
        "COMMONWEALTH": "COMMONWEALTH",
        "FRANCE": "FRENCH",
        "RUSSIA": "RUSSIAN",
    }

    ship_classes_list = [
        "DESTROYER",
        "CRUISER",
        "BATTLECRUISER",
        "POCKET BATTLESHIP",
        "BATTLESHIP"
    ]

    def __init__(self):

        sideA = Combatant("sideA")
        sideB = Combatant("sideB")

        self.combatants = {
            # 0: {"short_designation": "sideA"},
            # 1: {"short_designation": "sideB"}
            0: sideA,
            1: sideB
        }

    def determineNationalities(self, i):
        """
        lists for user potential nationalities to play as, 
        returns selected nationality as string value
        """

        loop_is_done = False
        while loop_is_done == False:

            # clear terminal screen
            clear_screen()

            print("\nPlease choose a side for combatant {} from the following:\n"
                  .format(self.combatants[i].short_designation))

            # iterate through nations_list to list nation options to player
            for nation in FleetEngagement.nations_list:
                print("\n" + nation)

            # player's input 'becomes' nationality
            print("\n")
            player_nationality = input().upper()

            # test to confirm player's selection is valid
            for nation in FleetEngagement.nations_list:
                if nation == player_nationality:

                    # report player's nationality
                    print("\n\nYou have chosen " + player_nationality + "\n")
                    loop_is_done = True
                    return player_nationality

            # only print if user choice is invalid, and loop to continue
            print(
                "\nPlayer choice is invalid.  Please confirm your choice is a listed nationality.")
            input("\npress the ENTER key to continue...\n")

    def fleetComposition(self, sideInt):
        """
        walks player through fleet composition for a given side, 
        updates self.combatants[sideInt]
        """

        # loop to determine # of TFs
        loop_is_done = False
        while loop_is_done == False:

            # clear screen, ask "how many TFs" per side
            clear_screen()

            print("\nFor {} ({}), how many task forces are involved?".format(
                self.combatants[sideInt].nationality,
                self.combatants[sideInt].short_designation))

            print("\n")
            number_of_taskforces = input("")

            # bark at the user if their input is invalid
            try:

                number_of_taskforces = int(number_of_taskforces)
                
                if number_of_taskforces > 0:
                    pass
                else:
                    raise ValueError

                loop_is_done = True

            except ValueError:
                print("\nPlayer choice is invalid.\n\nPlease confirm your input is an integer equal to or greater than one.")

                input("\npress the ENTER key to continue...\n")

        # for each TF,
        # determine composition of TF
        # and append to TF obj to FleetEngagement.combatants dict
        for current_tf in range(0, number_of_taskforces):

            loop_is_done = False
            while loop_is_done == False:

                try:
                    clear_screen()

                    print("\nDetermining composition of {} ({}) taskforce ({})...\n".format(
                        self.combatants[sideInt].nationality,
                        self.combatants[sideInt].short_designation,
                        current_tf+1))

                    print(
                        "\nPlease designate a numbered identity for this task force...\n")
                    print("(choose a number between 1 and 12)\n")
                    taskforce_number = int(input())

                    if taskforce_number < 1 or taskforce_number > 12:
                        raise ValueError
                    else:
                        loop_is_done = True

                except ValueError:
                    print(
                        "\nPlayer choice is invalid.\n\nPlease confirm your input is an integer equal to or greater than one.")
                    input("\npress the ENTER key to continue...\n")

            loop_is_done = False
            while loop_is_done == False:
                try:
                    clear_screen()

                    print("\nDetermining composition of {} ({}) Taskforce {}...\n".format(
                        self.combatants[sideInt].national_adjective,
                        self.combatants[sideInt].short_designation,
                        taskforce_number))

                    print("Set Naval DRM for taskforce:\n")
                    self.naval_nationality_drm = int(input())
                    loop_is_done = True

                except ValueError:
                    print(
                        "\nPlayer choice is invalid.\n\nPlease confirm your input is an integer equal to or greater than zero.")
                    input("\npress the ENTER key to continue...\n")

            # create TF obj
            taskforce = TaskForce(
                self.combatants[sideInt].nationality,  # nationality
                0,  # total_number_of_naval_factors
                "UNINVERTED",  # inversion status
                "FAST",  # speed
                taskforce_number,  # number
            )

            # determine TF composition via TF class method
            taskforce.taskforceComposition(
                self.combatants, sideInt)

            # update TF speed
            taskforce.update_tf_speed()

            # update TF number of factors
            taskforce.total_naval_factors = taskforce.tf_total_factors()

            # append TF obj to a given side's "fleet_composition" list
            self.combatants[sideInt].fleet_composition.append(taskforce)

    def begin_naval_combat(self):

        # naval combat happens in ROUNDs, and keeping track of how many rounds
        # of consecutive combat have occurred is critical
        round_count = 0
        combat_continues = True
        while combat_continues is True:

            # increase to represent 'current' round of naval combat
            round_count = round_count + 1

            # create combat round obj, feed FleetEngagement dict with TFs per side
            naval_combat_round = NavalCombatRound(self.combatants, round_count)

            naval_combat_round.main()

    def main(self):

        # determine combatant nationalities
        for i in self.combatants.keys():

            self.combatants[i].nationality = self.determineNationalities(i)
            self.combatants[i].national_adjective = FleetEngagement.nations_adjective_dict[self.combatants[i].nationality]

            input("\npress the ENTER key to continue...\n")

        # determine combatants' respective fleet compositions
        for i in self.combatants.keys():

            self.fleetComposition(i)

        # initiate and continue naval combat as necessary
        self.begin_naval_combat()


if __name__ == "__main__":
    logging.info("FleetEngagement.py excuted as __main__")
    test_battle = FleetEngagement()
    combat = True
    while combat is True:
        if test_battle.main() == 1:
            combat = False
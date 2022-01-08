import os

from ..shipTypes.ShipInitializer.ShipInitializer import ShipInitializer


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


class TaskForce():
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

    
    def distinct_shiptypes(self):
        """Returns a list of distinct ship types in TF"""

        distinct_shiptypes = []
        
        for ship in self.assigned_ships:

            if ship.SHIP_CLASS not in distinct_shiptypes:

                distinct_shiptypes.append(ship.SHIP_CLASS)

        return distinct_shiptypes

    
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














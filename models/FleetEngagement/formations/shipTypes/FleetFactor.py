from .NavalChit import NavalChit

from .LightShip import LightShip
from .HeavyShip import HeavyShip



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


# fleet factor subtypes
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
        FleetFactor.__init__(self, self.number_of_factors)


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






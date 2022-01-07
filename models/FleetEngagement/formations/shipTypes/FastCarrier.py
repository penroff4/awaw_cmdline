from shipTypes.NavalChit import NavalChit
from shipTypes.HeavyShip import HeavyShip

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

# fast carrier subtypes
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
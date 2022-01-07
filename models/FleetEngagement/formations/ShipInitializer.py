from shipTypes.FleetFactor import Destroyer, Cruiser, BattleShip, PocketBattleShip, BattleCruiser

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
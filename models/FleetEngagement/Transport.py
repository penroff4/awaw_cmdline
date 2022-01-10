from ShipTypes.NavalChit import NavalChit
from ShipTypes.LightShip import LightShip, StrategicWarfareShip

class Transport(NavalChit, LightShip, StrategicWarfareShip):
    
    SPEED = "SLOW"
    def __init__(self):
        pass
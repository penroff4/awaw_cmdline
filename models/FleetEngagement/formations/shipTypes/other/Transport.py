from shipTypes.NavalChit import NavalChit
from shipTypes.LightShip import LightShip, StrategicWarfareShip

class Transport(NavalChit, LightShip, StrategicWarfareShip):
    
    SPEED = "SLOW"
    def __init__(self):
        pass
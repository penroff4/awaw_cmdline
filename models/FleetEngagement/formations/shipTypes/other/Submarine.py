from shipTypes.NavalChit import NavalChit
from shipTypes.StrategicWarfareShip import StrategicWarfareShip

class Submarine(NavalChit, StrategicWarfareShip):
    
    SPEED = "FAST"
    
    def __init__(self):
        pass
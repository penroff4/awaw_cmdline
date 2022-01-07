from shipTypes.NavalChit import NavalChit
from shipTypes.LightShip import LightShip
from shipTypes.StrategicWarfareShip import StrategicWarfareShip

class EscortCarrier(NavalChit, LightShip, StrategicWarfareShip):
    
    SPEED = "SLOW"

    def __init__(self):
        pass
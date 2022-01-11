import unittest
# from unittest.mock import MagicMock

from FleetEngagement import FleetEngagement

class TestFleetEngagement(unittest.TestCase):

    def test_execute(self):
        """
        Test proves FleetEngagement main executes fully
        """
        player_one_nation = 'GERMANY'
        player_one_taskforce_number_of = 1
        player_one_ships = {'DESTROYER':1}
        
        player_two_nation = 'UNITED STATES'
        player_one_taskforce_number_of = 1
        player_one_ships = {'DESTROYER':1}

        self.fleet_engagement = FleetEngagement()

if __name__ == "__main__":
    unittest.main()

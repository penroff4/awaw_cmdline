from unittest import mock
from unittest import TestCase

from FleetEngagement import FleetEngagement

class TestFleetEngagement(TestCase):

    @mock.patch('FleetEngagement.input', create=True)
    def test_fleet_engagement(self, mocked_input):
        """
        Test proves FleetEngagement main executes fully (test supplies mocked user inputs)
        """

        mocked_input.side_effect = ["GERMANY", '', "FRANCE", '', 1, 1, 0, 0, 0, 1, 3, 'FAST', 'LE GERMANY', 1, 1, 0, 0, 0, 1, 3, 'FAST', 'LE FRANCE']
        result = FleetEngagement()
        result = result.main()
        self.assertTrue(result == 1, "result.main() did not return 1" )


# if __name__ == "__main__":
    # unittest.main()

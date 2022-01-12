from unittest import mock
from unittest import TestCase
import unittest

from FleetEngagement import FleetEngagement


class TestFleetEngagement(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setupClass')
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardownClass')
        return super().tearDownClass()
 
    def setUp(self) -> None:
        print('setUp')
        return super().setUp()

    def tearDown(self) -> None:
        print('tearDown')
        return super().tearDown()

    @mock.patch('FleetEngagement.input', create=True)
    def test_fleet_engagement(self, mocked_input):
        """
        Test proves FleetEngagement main executes fully (test supplies mocked user inputs)
        """

        """
        mocked user input where FleetEngagement main would expect it.

        mocked input includes setting GERMANY and FRANCE as combatting nationalities...
        ...with each side have a single TF made up of a destroyer and a named fast 3 factor BB
        """
        mocked_input.side_effect = ["GERMANY", '', "FRANCE", '', # nationality set up
                                    1, # one german task force
                                    3, # TF numbered 3
                                    1, 0, 0, 0, # one destroyer, no CA, PB, BC
                                    1, 3, 'FAST', 'LE GERMANY', # one fast BB3 named LE GERMANY
                                    1, # one french TF
                                    4, # TF numbered 4
                                    1, 0, 0, 0, # one destroyer, no CA, PB, BC
                                    1, 3, 'FAST', 'LE FRANCE',   # one fast BB3 named LE FRANCE
                                    '', # enter past 'beginning fleet engagement' screen
                                    4, # Assign German TF 3 to CG 4
                                    3, # Assign French TF 4 to CG 3
                                    ]
        self.assertTrue(FleetEngagement().main() == 1,
                        "result.main() did not return 1")


if __name__ == "__main__":
    unittest.main()

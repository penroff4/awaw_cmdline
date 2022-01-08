class NavalCombatRound(object):
    
    """docstring for NavalCombatRound"""

    def __init__(self, combatants_dict):
        self.combatants_dict = combatants_dict

    def form_combat_groups(self):
        """Each player secretly assigns combat group numbers to his participating TFs."""
        for combantant_int in self.combatants_dict:
            for taskforce in self.combatants_dict[combantant_int]:

                loop_is_done = False
                while loop_is_done == False:

                    try:
                        # clear screen
                        print("\nCombatant {} ({}):\n".format(
                            self.combatants_dict[combantant_int]["NATIONALITY"], self.combatants_dict[combantant_int]["short_designation"]))
                        print("\nFor TF {}, please assign to a combat group (between 1 and 6)".format(
                            self.combatants_dict[combantant_int]["fleet_composition"][taskforce]))
                        temp_combat_group = int(input())

                        if temp_combat_group > 0 and temp_combat_group < 7:

                            taskforce.combat_group = temp_combat_group

                        else:
                            raise ValueError

                        loop_is_done = True

                    except ValueError:
                        print(
                            "\nPlayer choice is invalid.\n\nPlease confirm your input is an integer equal to or greater than zero.")
                        input("\npress the ENTER key to continue...\n")


    def attack_enemy_air_bases(self):
        """
        Each player secretly allocates carrier-based NAS to CAP.  

        Remaining NAS may then coutner air enemy land-based air units (in a single round of air combat per counterair attack.

        Land-based air units not eliminated/aborted may participate in ensuing naval combat.

        """
        pass
    
    
    def allocate_carrier_air_to_air_strikes(self):
        """Carrier NAS (not assigned to CAP, not eliminated/aborted) may conduct air strikes against enemy naval units."""
        pass
    
    
    def allocate_land_based_air_to_air_cover(self):
        """

        Each side announces air cover by land-based air units by (secretly) assigning them to a specific combat group.

        Air units assigned to air cover may be used to defend that CG against enemy air units.

        Land based NAS commited to air cover may not search or attack enemy naval units this combat round.

        Search and attack AAS may not be used to fly air cover.

        """
        pass
    

    def search(self):
        """Each player rolls dice to determine his success in searching for his opponent's combat groups."""

        # for combatant
            # determine number of search rolls

                # SIMPLE METHOD
                    # player input number of search die

                # RAW method
                    # one die per land-based air squadron
                    # one die (and one fewer die for opponent) per tactical codebreaking card played (or via MAGIC intercept)
                    # one die per additional combat round
                    # one die for each friendly ACTIVE CG consisting of at least ten undamaged naval factors
                    # One die for each distant combat group containing at least one fully operational fast carrier at the start of combat round (no additional mod for active CGs containing fast carrier)

            # determine search results
                # each die which matches the number of an enemy CG achieves a search result against that CG
                # With one search result,
                    # CG is FOUND, and must reveal
                        # whether CG consists of less than ten naval factors
                        # how many fast carriers present in CG
                        # CG SPEED
                        # whether CG is carrying cargo
                # with multiple search results against a given CG
                    # CG may be attacked more than once equal to number of search results
                        # Air Strikes: For each search result against an active or distant enemy combat group, one air strike may be made against that combat group (23.72).
                        # Fleet Combat: For each search result against a distant enemy combat group, one active unpaired combat group may initiate fleet combat against that combat group (22.52). No search results are required for fleet combat between active combat groups and such fleet combat does not count against the limit on the number of air strikes.
                        # Effects Cumulative: The effects of search results are cumulative: two search results would allow any one of the following:
                            # Two air strikes against any combat group;
                            # Two fleet combats against a distant combat group; or
                            # One air strike and one fleet combat against a distant combat group.
                        # Submarine Attacks: Submarine attacks do not count against the limit on the number of times a found combat group may be attacked.

        pass
    
    def reveal_combat_groups(self):
        """

        For each combat group found, the owning player reveals:
            - whether CG consists of less than ten naval factors
            - how many fast carriers
            - CG speed (ie Fast or Slow)
            - whether "cargo" is present

        """
        pass

    def air_strikes_and_attacks(self):
        """

        Found enemy CGs may be attacked by land-based and carrier-based air units, in the following order:
            - One surprise carrier-based air strike per naval combat round
            - Non-surprise air strikes

        """
        pass


    def fleet_combat(self):
        """Fleet combat is resolved"""

        #   Fleet combat
        #       Determine which combat groups will engage in fleet combat
        #       Divide ships into heavy, light, and screened
        #       Defender ranks heavy ships from largest to smallest, then light ships, then screened ships.
        #       Heavy ship combat
        #           Attacker selects targets for his heavy ships.
        #           Defender selects targets for his heavy ships.
        #           Resolve all heavy ship fire versus light ships and apply damage.
        #       Light ship combat
        #           Select targets for light ships of both sides.
        #           Resolve all fire versus all heavy ships.
        #           Resolve all light ship fire versus light ships.
        #       Screened ship combat
        #           Resolve all fire versus screened ships if permitted.
        pass
     

    def submarine_attacks(self):
        """Submarine attacks are resolved"""
        pass


    def main(self):
        self.form_combat_groups()
        self.attack_enemy_air_bases()
        self.allocate_carrier_air_to_air_strikes()
        self.allocate_land_based_air_to_air_cover()
        self.search()
        self.reveal_combat_groups()
        self.air_strikes_and_attacks()
        self.fleet_combat()
        self.submarine_attacks()
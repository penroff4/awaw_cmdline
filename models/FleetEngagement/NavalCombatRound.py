class NavalCombatRound(object):
	
	"""docstring for NavalCombatRound"""

	def __init__(self, arg):
		self.arg = arg


	def form_combat_groups(self):
		"""Each player secretly assigns combat group numbers to his participating TFs."""
		pass


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
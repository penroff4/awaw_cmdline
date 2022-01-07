class NavalChit:

    """

    docstring for NavalChit

    attributes:
        - number_of_naval_factors (NavalChit)

    """

    DMGED_SPEED = "SLOW"

    # Fleet Factor, Fast Carrier, or Strategic Warfare?
    NAVAL_CHIT_CLASS = ""

    SHIP_CLASS = ""
    SHIP_CLASS_SHORT = ""


    SPEED = ""

    # Heavy or Light?
    SHIP_WEIGHT = ""

    def __init__(self, number_of_factors=0, nationality="", hits=0):

        self.number_of_factors = number_of_factors
        self.nationality = nationality
        self.hits = hits

    def __str__(self):

        return NavalChit.SHIP_CLASS_SHORT + str(self.number_of_factors)


    def short_name(self):

        return self.nationality + " " + SHIP_CLASS_SHORT

    def long_name(self):

        return self.nationality + " " + self.number_of_factors + " factor " + SHIP_CLASS
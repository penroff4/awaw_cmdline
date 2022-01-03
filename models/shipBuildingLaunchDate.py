
class shipBuildingLaunchDate():

    # class vars
    seasons_num_dict = {1:"SPRING", 2:"SUMMER", 3:"FALL", 4:"WINTER"}
    seasons_name_dict = {"SPRING": 1, "SUMMER": 2, "FALL": 3, "WINTER": 4}
    
    # init with allowable None/0 values for init params
    def __init__(self, season_name="", row=0, year=0, construction_rate=0, set_up_style=None):
        self.season_name = season_name.upper()
        self.row = int(row)
        self.year = int(year)
        self.construction_rate = construction_rate

        self.set_up_style = set_up_style

        try:
            season_num = shipBuildingLaunchDate.seasons_name_dict[self.season_name]
        except KeyError:
            season_num = None
            

        # initialize ship dockyard position
        self.ship_dockyard_position = {"row": self.row, "season_name": self.season_name, "season_num": season_num, "year": self.year}

    def all_correct_args(self):

        self.season_arg_is_correct = (
            (self.season_name == 'SPRING') or 
            (self.season_name == 'SUMMER') or 
            (self.season_name == 'FALL') or 
            (self.season_name == 'WINTER')
        )

        self.row_arg_is_int = (
            isinstance(int(self.row), int) and 
            (
                int(self.row) <= 5 and 
                int(self.row) >= 1
            )
        )
        
        self.year_arg_is_int = isinstance(int(self.year), int)
        
        self.construction_rate_arg_is_int = (
            isinstance(self.construction_rate, str) and 
            (
                self.construction_rate == 'normal' or 
                self.construction_rate == 'fast' or 
                self.construction_rate == 'max'
            )
        )

        self.all_args_proper = (
            self.season_arg_is_correct == True and 
            self.row_arg_is_int == True and 
            self.year_arg_is_int == True and 
            self.construction_rate_arg_is_int == True
        )

    # confirm input vars valid, if not ask for user inputted vars
    def setup(self):

        print("\n\nYou asked for ship building launch date (" + self.set_up_style + ").\n")

        shipBuildingLaunchDate.all_correct_args(self)

        if self.all_args_proper == False:
            print("\nSetting ship building parameters...")

            # Ask user for starting parameters (season of construction, initial row placement, year construction started)
            print("\nWhat column is your ship on?\nNote: Input should be 'Spring', 'Summer', 'Fall', or 'Winter'\n\n")
            self.season_name = input().upper()
            self.season_num = self.seasons_name_dict[self.season_name]

            print("\nWhat row is your ship on?\nNote: Input should be 5, 4, 3, 2, or 1 (for Launch)\n\n")
            self.row = int(input())
            
            print("\nWhat year did your vessel begin construction?\n\n")
            self.year = int(input())

            # confirm user requested construction speed
            print("\nWhat construction rate are you interested in?\nNote: Input should be 'normal', 'fast', or 'max'\n\n")
            self.construction_rate = input()

            # line breaks for spaceing
            print('\n\n')

            # create ship dockyard position
            self.ship_dockyard_position = {
                'row': self.row,
                'season_name': self.season_name,
                'season_num': self.season_num,
                'year': self.year
            }

    def construction(self):

        construction_speed_dict = {'normal': 0, 'fast': -1, 'max': -2}
        self.construction_rate_num = construction_speed_dict[self.construction_rate]

        construction_finished = False

        # account for time lapse between ship being laid down and next year's construction
        if self.row > 1:
            self.ship_dockyard_position["year"] = self.ship_dockyard_position["year"] + 1

        # while constructing...
        while construction_finished == False:

            # iterate through each season of a given year
            for current_season in shipBuildingLaunchDate.seasons_name_dict:

                # if current_season matches ship's season on construction chart
                if current_season == self.ship_dockyard_position["season_name"]:

                    # advance to next row on construction chart
                    self.ship_dockyard_position["row"] = self.ship_dockyard_position["row"] - 1

                    # update ship's season per acceleration (0, -1, or -2)
                    if self.ship_dockyard_position["row"] > 1:
                        self.ship_dockyard_position["season_num"] = self.ship_dockyard_position["season_num"] + self.construction_rate_num

                        # adjust season num if -2 or -1 (e.g. 1 (Spr) - 2 = -2, so -2 + 4 = 2 ie Summer)
                        if self.ship_dockyard_position["season_num"] < 1:
                            self.ship_dockyard_position["season_num"] = self.ship_dockyard_position["season_num"] + 4

                        # update ship's season name (critical for current_season == self.season_name)
                        self.ship_dockyard_position["season_name"] = shipBuildingLaunchDate.seasons_num_dict[self.ship_dockyard_position["season_num"]]
        
                if current_season == "WINTER" and self.ship_dockyard_position["row"] != 1:
                    self.ship_dockyard_position["year"] = self.ship_dockyard_position["year"] + 1
                
            if self.ship_dockyard_position["row"] == 1:

                # output projected ship launch date
                print("\nYour ship will be launched in " + self.ship_dockyard_position["season_name"] + " of " + str(self.ship_dockyard_position["year"]) + "\n")
                construction_finished = True


    # function determines ship launch date
    def main(self):
        
        shipBuildingLaunchDate.construction(self)

class shipBuildingLaunchDate():

    # class vars
    seasons_num_dict = {1:"Spring", 2:"Summer", 3:"Fall", 4:"Winter"}
    seasons_name_dict = {"Spring": 1, "Summer": 2, "Fall": 3, "Winter": 4}
    
    # init with allowable None/0 values for init params
    def __init__(self, season_name=None, season_num=0, row=0, year=0, construction_rate=0, set_up_style=None):
        self.season_name = season_name
        self.season_num = shipBuildingLaunchDate.seasons_name_dict[season_name]
        self.row = int(row)
        self.year = int(year)
        self.construction_rate = construction_rate

        self.set_up_style = set_up_style

    def setup(self):

        print("\n\nYou asked for ship building launch date (" + self.set_up_style + ").\n")

        season_arg_is_correct = (
            (self.season_name == 'Spring') or 
            (self.season_name == 'Summer') or 
            (self.season_name == 'Fall') or 
            (self.season_name == 'Winter')
        )

        row_arg_is_int = (
            isinstance(int(self.row), int) and 
            (
                int(self.row) <= 5 and 
                int(self.row) >= 1
            )
        )
        
        year_arg_is_int = isinstance(int(self.year), int)
        
        construction_rate_arg_is_int = (
            isinstance(self.construction_rate, str) and 
            (
                self.construction_rate == 'normal' or 
                self.construction_rate == 'fast' or 
                self.construction_rate == 'max'
            )
        )

        all_args_proper = (
            season_arg_is_correct == True and 
            row_arg_is_int == True and 
            year_arg_is_int == True and 
            construction_rate_arg_is_int == True
        )

        if 1==1: #all_args_proper == True:
            print("\nseason_arg_is_correct = " + str(season_arg_is_correct))
            print("\nrow_arg_is_int = " + str(row_arg_is_int))
            print("\nyear_arg_is_int = " + str(year_arg_is_int))
            print("\nconstruction_rate_arg_is_int = " + str(construction_rate_arg_is_int))

        else:

            print("\nSetting ship building parameters...")

            # Ask user for starting parameters (season of construction, initial row placement, year construction started)
            print("\nWhat column is your ship on?\nNote: Input should be 'Spring', 'Summer', 'Fall', or 'Winter'\n\n")
            self.season_name = input()
            self.season_num = self.seasons_name_dict[self.season_name]

            print("\nWhat row is your ship on?\nNote: Input should be 5, 4, 3, 2, or 1 (for Launch)\n\n")
            self.row = int(input())
            
            print("\nWhat year did your vessel begin construction?\n\n")
            self.year = int(input())

            # confirm user requested construction speed
            print("\nWhat construction rate are you interested in?\nNote: Input should be 'normal', 'fast', or 'max'\n\n")
            self.construction_rate = input()


    # function determines ship launch date
    def main(self):
        
        # initialize ship dockyard position
        self.ship_dockyard_position = {"row": self.row, "season_name": self.season_name, "season_num": self.season_num, "year": self.year}

        # "Normal" construction rate features a shift down one row each year
        if self.construction_rate == 'normal':

            for i in range(1, row):

                self.ship_dockyard_position["row"] = self.ship_dockyard_position["row"] - 1
                self.ship_dockyard_position["year"] = self.ship_dockyard_position["year"] + 1
            
            # output projected ship launch date
            print("\nYour ship will be launched in " + self.ship_dockyard_position["season_name"] + " of " + str(ship_dockyard_position["year"]) + "\n")

        # "Fast" construction rate features a shift down and to the 'left' during the appropriate season
        else:

            # set construction_speed var, which we'll use to modify season var
            if self.construction_rate == 'fast':

                self.construction_rate_num = -1

            elif self.construction_rate == 'max':

                self.construction_rate_num = -2

            while self.ship_dockyard_position["row"] > 1:

                print("\n")
                print(self.ship_dockyard_position)

                # on row two, we can't accelerate: only shift row and year
                if self.ship_dockyard_position["row"] == 2:

                    self.ship_dockyard_position["row"] = self.ship_dockyard_position["row"] - 1
                    self.ship_dockyard_position["year"] = self.ship_dockyard_position["year"] + 1

                else:
                    
                    # shift vessel 'down' to next construction row
                    self.ship_dockyard_position["row"] = self.ship_dockyard_position["row"] - 1

                    # shift vessel to 'prior' season (i.e. Winter to Fall, or Spring to Winter etc)
                    # size of shift depends on construction_rate_num var
                    # do not increment year value if acceleration moves season later in year (rather than to season in next year)
                    if (self.ship_dockyard_position["season_num"] == 1 and self.construction_rate_num == -1) or (self.ship_dockyard_position["season_num"] == 2 and self.construction_rate_num == -2):

                        self.ship_dockyard_position["season_num"] = 4
                        self.ship_dockyard_position["season_name"] = self.seasons_num_dict[self.ship_dockyard_position["season_num"]]

                    elif (self.ship_dockyard_position["season_num"] == 1 and self.construction_rate_num == -2):

                        self.ship_dockyard_position["season_num"] = 3
                        self.ship_dockyard_position["season_name"] = self.seasons_num_dict[self.ship_dockyard_position["season_num"]]

                    else:

                        self.ship_dockyard_position["season_num"] = self.ship_dockyard_position["season_num"]-1
                        self.ship_dockyard_position["season_name"] = self.seasons_num_dict[self.ship_dockyard_position["season_num"]]
                        self.ship_dockyard_position["year"] = self.ship_dockyard_position["year"]+1
            
            # output expected ship launch date
            print("\nYour ship will be launched in " + self.ship_dockyard_position["season_name"] + " of " + str(self.ship_dockyard_position["year"]) + "\n")
























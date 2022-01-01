from random import randint

class researchDieRoller:

    def __init__(self, number_of_requested_rolls):
        self.number_of_requested_rolls = number_of_requested_rolls

    def main(self):
        
        # set remaining var
        main_number_of_rolls = 1
        rolls = {}

        # while number of rolls less than requested number of rolls
        while main_number_of_rolls <= self.number_of_requested_rolls:

            current_rolls = []

            # roll a d6 three times
            for number in range(1,4):
                current_rolls.append(randint(1,6))

            main_number_of_rolls = main_number_of_rolls+1

            rolls[main_number_of_rolls] = current_rolls

        # print die rolls
        print("\nYour die rolls are as follow:\n")

        for i in rolls:

            new_array = rolls[i]
            new_array.sort()
            print(new_array)

        print("\n")

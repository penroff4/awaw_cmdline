#import csv
import pandas as pd


# def make_table(csv_file):

#     with open(csv_file) as csvfile:

#     	table = from_csv(csvfile)
#     	return table


awaw_ships_csv = 'resources/AWAWNamedShips.csv'

awaw_ships = pd.read_csv(awaw_ships_csv)

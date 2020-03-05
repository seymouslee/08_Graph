# open csv file printing the rows
import csv
from csv import writer
import pandas as pd
import csv as cv

# to parse a csv containing nodes
def openNode(csv_name):
    with open(csv_name, newline='') as csvfile:
        colnames = ['id', 'name', 'latitude', 'longitude']
        data = pd.read_csv(csv_name, header=None, names=colnames)
        return data

# to parse a csv containing edges
def openEdge(csv_name):
    with open(csv_name, newline='') as csvfile:
        colnames = ['start', 'end', 'distance', 'time', 'service']
        data = pd.read_csv(csv_name, header=None, names=colnames)
        return data


def copy_csv(csv_name):
    df = pd.read_csv(csv_name)
    df.to_csv('copy_of_' + csv_name)

# append new row to the last row
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:

        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

    # List of strings
    #row_contents = [32, 'Shaun', 'Java', 'Tokyo', 'Morning'] #example
    # Append a list as new line to an old csv file
    #append_list_as_row('copy_of_hdb-coordinates.csv', row_contents)

def serachAttribute(csv_name, attribute, data):
    # user_input = "1.397847151"  # hard code
    # search based on user input
    df = pd.read_csv(csv_name)

    for index, row in df.iterrows():
        if row[attribute] == data:
            print(row)









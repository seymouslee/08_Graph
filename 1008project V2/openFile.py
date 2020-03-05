# open csv file printing the rows
import csv
from csv import writer
import pandas as pd
import csv as cv

def openfile():
    with open('hdb-coordinates.csv', newline='') as csvfile:
        colnames = ['postal', 'latitude', 'longtitude', 'searchval', 'blk_no', 'road_name', 'buidling', 'address']
        data = pd.read_csv('hdb-coordinates.csv', header=None, names=colnames)
        return data

def ogOpenfile():
    with open('hdb-coordinates.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return reader

def copy_csv(filename):
    df = pd.read_csv('hdb-coordinates.csv')
    df.to_csv('copy_of_' + 'hdb-coordinates.csv')

def getNodes(data):
    postal = data.postal.tolist()
    return postal

def getLatitude(data):
    latitude = data.latitude.tolist()
    return latitude

def getlongtitude(data):
    longtitude = data.longtitude.tolist()
    return longtitude

def getblk_no(data):
    blk_no = data.blk_no.tolist()
    return blk_no

def getaddress(data):
    address = data.address.tolist()
    return address

def getroad_name(data):
    road_name = data.road_name.tolist()
    return road_name


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

def serachLatitude(attribute, data):
    # user_input = "1.397847151"  # hard code
    # search based on user input
    df = pd.read_csv("copy_of_hdb-coordinates.csv")
    print

    for index, row in df.iterrows():
        if row[attribute] == data:
            print(row)




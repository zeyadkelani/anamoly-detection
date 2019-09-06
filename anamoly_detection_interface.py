import pandas as pd
import readline
from os import system, name

# path to CSV data file
DATA_FILE_PATH = "./GES/first_cut.dta"

def openFile():
    global DATA_FILE_PATH
    if DATA_FILE_PATH[-3:] == "csv":
        data = pd.read_csv(DATA_FILE_PATH)
    elif DATA_FILE_PATH[-3:] == "dta":
        data = pd.read_stata(DATA_FILE_PATH)
    return data


# clear function from https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

""" takes the whole dataset and retunrns a df with only spafified specified yiled"""
def ask_yield(data):
    yields =  data['yield'].unique()
    index = 1
    for option in yields:
        print(str(index) + ". " + str(option))
        index = index + 1
    usrinput = input("select a yield option from 1 to " + str(len(yields))+" ")
    return data.loc[data['yield'] == yields[int(usrinput)-1]]

""" takes dataset with one yield and retunrns a df with only spafified specified density"""
def ask_density(data):
    densities = data['density'].unique()
    index = 1
    for option in densities:
        print(str(index) + ". " + str(option))
        index = index + 1
    usrinput = input("select a density option from 1 to " + str(len(densities))+" ")
    return data.loc[data['density'] == densities[int(usrinput)-1]]

""" takes dataset with one yield and retunrns a df with only spafified specified density"""
def ask_location(data):
    locations = data['location'].unique()
    index = 1
    for option in locations:
        print(str(index) + ". " + str(option))
        index = index + 1
    usrinput = input("select a location option from 1 to " + str(len(locations))+" ")
    return data.loc[data['location'] == locations[int(usrinput)-1]]


def do_not_ask_again():
    usrinput = input("exit interface? (Enter Y/N) ")
    if usrinput == "y" or usrinput == "Y":
        return True
    elif usrinput == "n" or usrinput == "N":
        return False
    else:
        do_not_ask_again()

def main():
    try:
        data = openFile()
    except:
        print("data file not found")
        return
    clear()
    print("anamoly detection per density")
    while True:
        df1 = ask_yield(data)
        clear()
        df2 = ask_density(df1)
        clear()
        df3 = ask_location(df2)
        clear()
        print(df3)
        if do_not_ask_again():
            break

main()

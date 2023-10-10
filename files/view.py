from files.load_data import *
import os


def get_data():
    files = os.listdir("files")
    sets = [i.removesuffix('.json') for i in files if i not in ["__pycache__", "load_data.py", 'view.py']]
    options = {}
    for i in range(len(sets)):
        options[i + 1] = sets[i]
        print(f"{i+1}: {sets[i]}")
    data = load_data(options[int(input("Which Study Set Would You Like?\n"))])
    return data
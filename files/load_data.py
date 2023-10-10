import json


def load_data(file: str):
    with open('files/' + file + '.json', 'r') as read_file:
        data = json.load(read_file)
        return data

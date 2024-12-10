import json
def get_data():
    with open("config/data.json", "r") as file:
        return json.load(file)
    
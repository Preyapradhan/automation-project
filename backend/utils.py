import json

def save_to_file(data, filename="organizations.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_from_file(filename="organizations.json"):
    with open(filename, "r") as file:
        return json.load(file)

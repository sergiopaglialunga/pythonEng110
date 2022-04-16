
# JSON
# javaScript Object Notation
# API ==> Application Programme Interface

import json

car = {
    "make": "tesla",
    "engine": "electric",
    "faults": "lots",
    "is_expensive": True,
    "driver": None
    }

# json_dumps = json.dumps(car)
# print(json_dumps, type(json_dumps))

# dumps ==> takes a dictionary and "dumps" it as a string

# with open("car_json_file.json", "w") as jsonfile:
#     json.dump(car, jsonfile)

with open("new_car_json_file.json", "r") as jsonfile:
    new_car = json.load(jsonfile)

print(new_car, type(new_car))



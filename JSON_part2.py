import json

states_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
}

with open("_1_variable_and_datatypes\_2_operator_\json_&_OOP\StateCapitals.json", "w") as outfile:
    json.dump(states_capitals, outfile)

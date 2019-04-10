# https://medium.com/python-pandemonium/json-the-python-way-91aac95d4041

import json
# Serialize - dumps
serial = json.dumps({
    "name": "Foo Bar",
    "age": 78,
    "friends": ["Jane", "John"],
    "balance": 345.80,
    "other_names": ("Doe", "Joe"),
    "active": True,
    "spouse": None}, sort_keys=True, indent=4)
#print (serial)

# Serialize - dump
with open('user.json', 'w') as file:
    json.dump({
        "name": "Foo Bar",
        "age": 78,
        "friends": ["Jane", "John"],
        "balance": 345.00,
        "other_names": ("Doe", "Joe"),
        "active": True,
        "spouse": None
    }, file, sort_keys=True, indent=4)

# Deserialize - loads
deserial = json.loads(serial)
# print (deserial)

# Deserialize - load
with open('user.json', 'r') as file:
    user_data = json.load(file)
# print (user_data)


# Serialize - dump - custom class objects
from json_user import User
new_user = User(
    name = "Foo Bar",
    age = 78,
    friends = ["Jane", "John"],
    balance = 345.80,
    other_names = ("Doe", "Joe"),
    active = True,
    spouse = None)
# json.dumps(new_user)
# TypeError: Object of type 'User' is not JSON serializable

from json_convert_to_dict import convert_to_dict
data = json.dumps(new_user, default=convert_to_dict, indent=4, sort_keys=True)
#print(data)
#user_data = json.loads(data)
print(type(data))
print(data)

# Deserialize - loads - custom class objects
from json_dict_to_obj import dict_to_obj
new_object = json.loads(data, object_hook=dict_to_obj)
print(type(new_object))
print(new_object)
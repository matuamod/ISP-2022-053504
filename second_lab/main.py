from sympy import sec
from source import JSON_Serializer
from source import JSON_Parser
import inspect
import toml
import yaml

price = 3000343

car = "BMW 335i"

cylinders = "6 cylinders"

power = 400.76

spec_list = [
    "n54",
    "twinturbo",
    "custom upgrades"
]

tuple_spec = (
    4,
    448,
    335
)

dict_spec = {
    "BMW": 1,
    "Mercedes-Benz": 2,
    "Audi": 3 
}

def car_method(v):
    speed = "Fast"
    v = price
    print(v)
    
json_serializer = JSON_Serializer()
json_serializer.dump(car_method, "all_data.json")
buffer = json_serializer.load("all_data.json")
print(buffer)

# json_serializer.dump(tuple_spec, "all_data.json")
# json_string = json_serializer.dumps(tuple_spec)
# buffer = json_serializer.loads(json_string)
# print(buffer)

# json_serializer.dump(dict_spec, "all_data.json")

#json_serializer.dump(spec_list, "all_data.json")

# first_type = json_serializer.dumps(car)
# second_type = json_serializer.dumps(cylinders)
# third_type = json_serializer.dumps(spec_list)
# fouth_type = json_serializer.dumps(power)
# fifth_type = json_serializer.dumps(tuple_spec)

# file = open("all_data.json", "a")
# file.write(first_type)
# file.close()
# file = open("all_data.json", "a")
# file.write(second_type)
# file.close()
# file = open("all_data.json", "a")
# file.write(third_type)
# file.close()
# file = open("all_data.json", "a")
# file.write(fouth_type)
# file.close()
# file = open("all_data.json", "a")
# file.write(fifth_type)
# file.close()




from sympy import sec
from source import JSON_Serializer
from source import JSON_Parser
import inspect

price = 300

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
    cylinders,
    335
)

dict_spec = {
    "BMW" : 1,
    "Mercedes_Benz" : 2,
    "Audi" : 3 
}

def car_method(v):
    speed = "Fast"
    v = price
    print(v)
    
json_serializer = JSON_Serializer()
json_serializer.dump(car_method, "all_data.json")

json_parser = JSON_Parser()
json_parser.print_smth()

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




from sympy import sec
from source import JSON_Serializer

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

json_serializer = JSON_Serializer()

first_type = json_serializer.dumps(car)
second_type = json_serializer.dumps(cylinders)
third_type = json_serializer.dumps(spec_list)
fouth_type = json_serializer.dumps(power)
fifth_type = json_serializer.dumps(tuple_spec)

file = open("all_data.json", "a")
file.write(first_type)
file.close()
file = open("all_data.json", "a")
file.write(second_type)
file.close()
file = open("all_data.json", "a")
file.write(third_type)
file.close()
file = open("all_data.json", "a")
file.write(fouth_type)
file.close()
file = open("all_data.json", "a")
file.write(fifth_type)
file.close()




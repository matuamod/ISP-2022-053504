from sympy import sec
from source import JSON_Serializer
from source import JSON_Parser
import inspect
import toml
import yaml

chip = b'\x00\x00\x00\x00\x00'

price = 300

car = "BMW 335i"

cylinders = "6 cylinders"

power = 400.76

xdrive = False

touring = None

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
    v = price + 200
    print(v)

class BMW_Group():

    def __init__(self, country: str, city: str):
        self.country = country
        self.city = city
    
    db = 1916

    models = [
        "1-series", "3-series", 
        "5-series", "7-series"
    ]

    def buy_car(self, car_type: str):
        if car_type == self.models[0]:
            price = 45000
        elif car_type == self.models[1]:
            price = 55000
        elif car_type == self.models[2]:
            price = 70000
        elif car_type == self.models[3]:
            price = 95000
        else:
            print("No such car in autohaus")
            price = 0
        return (car_type, price)

    def get_bought_car(self, car_type: str, price: int):
        if price > 0:
            print(f"New customer bought {car_type} for {price}")
        else:
            print("Choose correct car please")

class Dog():
    # name = "Cherry"
    pass

json_serializer = JSON_Serializer()
json_serializer.dump(Dog, "all_data.json")
buffer = json_serializer.load("all_data.json")
# autoidea = BMW_Group("Germany", "Munich")
# autoidea.buy_car("3-series")

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




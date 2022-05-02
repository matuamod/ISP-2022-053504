from matuamod_serializer import JSON_Serializer, TOML_Serializer, YAML_Serializer
from matuamod_serializer import JSON_Parser, TOML_Parser, YAML_Parser
from matuamod_serializer import Converter
import inspect
import toml
import yaml
import module

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

digits = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

hard = [{"Matua": 1}, {"Kefir": 2}, {"Maksus": 3}]

dict_spec = {
    "BMW": 1,
    "Mercedes-Benz": 2,
    "Audi": 3 
}

def sum_method(a, b):
    speed_alg = "Fast"
    c = a + b
    print(c)

class BMW_Group():

    def __init__(self, country: str, city: str):
        self.country = country
        self.city = city
    
    db = 1916

    loveable = True

    models = [
        "1-series", "3-series", 
        "5-series", "7-series"
    ]

    def buy_car(self, car_type: str):
        if car_type in self.models:
            if car_type == self.models[0]:
                price = 45000
            elif car_type == self.models[1]:
                price = 55000
            elif car_type == self.models[2]:
                price = 70000
            elif car_type == self.models[3]:
                price = 95000
            self.get_bought_car(car_type, price)
        else:
            print("No_such_car_in_autohaus")
            price = 0
        return (car_type, price)

    def get_bought_car(self, car_type: str, price: int):
        if price > 0:
            print(f"New_customer_bought_{car_type}_for_{price}_dollars")

Autoidea = BMW_Group("Belarus", "Minsk")


json_serializer = JSON_Serializer()
json_serializer.dump(BMW_Group, "all_data.json")
buffer1 = json_serializer.load("all_data.json")
# Puppy = buffer1.Dog("Cherry")
# Puppy.make_voice()
# buffer.buy_car("3-series")
# Autoidea = buffer("Belarus", "Minsk")
# Autoidea.buy_car("3-series")

toml_serializer = TOML_Serializer()
toml_serializer.dump(Autoidea, "all_data.toml")
buffer2 = toml_serializer.load("all_data.toml")
# car_shop = buffer2("Russia", "Sochi")
# car_shop.buy_car("5-series")
# Puppy = buffer2.Dog("Cherry")
# Puppy.make_voice()

yaml_serializer = YAML_Serializer()
yaml_serializer.dump(module, "all_data.yaml")
buffer3 = yaml_serializer.load("all_data.yaml")
# car_shop = buffer3("Russia", "Sochi")
# car_shop.buy_car("7-series")
# Puppy = buffer3.Dog("Cherry")
# Puppy.make_voice()



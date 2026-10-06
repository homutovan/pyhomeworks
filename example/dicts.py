from pprint import pprint

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year" : 1964,
#     }

car = dict()

car["brand"] = "BMW"
car["model"] = "x7"

# car["brand"] = "Audi"

# result = car.pop("model")
# result = car.popitem()
# print(f"result: {result}")

# car.clear()

car_addons_data = {
    "color":"red",
    "price": 20,
}

car.update(car_addons_data)
print(car)
# print(type(car))

# print(car["color"])
# print(car.get("year", "No colour"))

# for key in car:
#     print(key, car[key])

for key, value in car.items():
    print(key, value)
# Week-5-Python-Assignment
Object Orientated Programming

class CarManufacturer:
    def __init__(self, name, founded_year, country):
        self.name = name
        self.founded_year = founded_year
        self.country = country
        self._car_models = []  # Encapsulated list of car models

    def introduce(self):
        return f"{self.name} was founded in {self.founded_year} in {self.country}."

    def produce_car(self, model, year, is_electric):
        car = Car(model, year, is_electric)
        self._car_models.append(car)
        print(f"{self.name} has produced a new car: {car.model} ({car.year}) - Electric: {car.is_electric}")

    def get_car_models(self):
        return [car.model for car in self._car_models]

class Tesla(CarManufacturer):
    def __init__(self, founded_year, country):
        super().__init__("Tesla", founded_year, country)

    def produce_car(self, model, year):
        super().produce_car(model, year, True)  # Tesla always produces electric cars

class Toyota(CarManufacturer):
    def __init__(self, founded_year, country):
        super().__init__("Toyota", founded_year, country)

    def produce_car(self, model, year, is_hybrid=False):
        super().produce_car(model, year, is_hybrid)

class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden in subclasses")

class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying through the clouds ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing across the waves 🚢"

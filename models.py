#smartphone class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

# Inheritance example
class SuperSmartphone(Smartphone):
    def __init__(self, brand, model, storage, ai_assistant):
        super().__init__(brand, model, storage)
        self.ai_assistant = ai_assistant

    def use_ai(self):
        print(f"{self.brand} {self.model} is using {self.ai_assistant} to help you!")

# Polymorphism example
class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚤")

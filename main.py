# main.py
from models import Smartphone, SuperSmartphone, Car, Plane, Boat

# Assignment 1: Create objects from the classes
phone1 = Smartphone("Samsung", "S24", "256GB")
phone1.call("123456789")

super_phone = SuperSmartphone("Apple", "iPhone 15 Pro", "512GB", "Siri")
super_phone.call("987654321")
super_phone.use_ai()

print("\n--- Polymorphism Demo ---")

# Activity 2: Polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()

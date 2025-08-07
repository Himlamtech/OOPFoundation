"""
Explanation: Different types of instance variables in __init__

This demonstrates why some variables are parameters and others are defaults.
"""

class Car:
    def __init__(self, make, model, year, color="Unknown"):
        # TYPE 1: Variables from PARAMETERS (user provides these)
        self.make = make          # User must specify: "Toyota"
        self.model = model        # User must specify: "Camry" 
        self.year = year          # User must specify: 2022
        self.color = color        # User can specify or use default: "Unknown"
        
        # TYPE 2: Variables with DEFAULT VALUES (same for all new cars)
        self.is_running = False   # All cars start turned OFF
        self.speed = 0           # All cars start with 0 speed
        self.mileage = 0         # All cars start with 0 miles
        
        # These make logical sense as defaults:
        # - A new car shouldn't be running when created
        # - A new car shouldn't be moving when created  
        # - A new car should have 0 miles when created

def demonstrate_initialization():
    print("Creating cars to show initialization...")
    
    # When we create a car, we specify make, model, year
    # But is_running, speed, mileage start with sensible defaults
    
    car1 = Car("Toyota", "Camry", 2022, "Blue")
    car2 = Car("Honda", "Civic", 2021)  # Using default color
    
    print(f"\nCar 1 - {car1.make} {car1.model}:")
    print(f"  Color: {car1.color}")           # From parameter: "Blue"
    print(f"  Running: {car1.is_running}")    # From default: False
    print(f"  Speed: {car1.speed}")           # From default: 0
    print(f"  Mileage: {car1.mileage}")       # From default: 0
    
    print(f"\nCar 2 - {car2.make} {car2.model}:")
    print(f"  Color: {car2.color}")           # From default: "Unknown"
    print(f"  Running: {car2.is_running}")    # From default: False
    print(f"  Speed: {car2.speed}")           # From default: 0
    print(f"  Mileage: {car2.mileage}")       # From default: 0

# Alternative design (BAD IDEA - but shows why we don't do this):
class BadCarExample:
    def __init__(self, make, model, year, color, is_running, speed, mileage):
        # This would be annoying - user has to specify everything!
        self.make = make
        self.model = model  
        self.year = year
        self.color = color
        self.is_running = is_running  # User would have to pass False every time
        self.speed = speed            # User would have to pass 0 every time
        self.mileage = mileage        # User would have to pass 0 every time

def show_bad_example():
    print("\n" + "="*50)
    print("BAD DESIGN EXAMPLE:")
    print("="*50)
    
    # With bad design, creating a car is annoying:
    bad_car = BadCarExample("Toyota", "Camry", 2022, "Blue", False, 0, 0)
    #                                                        ^^^^^^^^^^^^
    #                                                        Always the same!
    
    print("Bad design forces user to specify obvious defaults:")
    print("BadCarExample('Toyota', 'Camry', 2022, 'Blue', False, 0, 0)")
    print("                                               ^^^^^^^^^^^^")
    print("                                               Always False, 0, 0!")

if __name__ == "__main__":
    demonstrate_initialization()
    show_bad_example()
    
    print("\n" + "="*60)
    print("KEY TAKEAWAY:")
    print("="*60)
    print("✅ Parameters: Things that vary between objects")
    print("   (make, model, year, color)")
    print()
    print("✅ Default values: Things that start the same for all objects")
    print("   (is_running=False, speed=0, mileage=0)")
    print()
    print("Both are initialized in __init__, but serve different purposes!")

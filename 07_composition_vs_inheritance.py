"""
Object-Oriented Programming Foundation - Lesson 7: Composition vs Inheritance

This lesson covers the design decision between composition and inheritance:
- What is composition?
- When to use inheritance vs composition
- "Has-a" vs "Is-a" relationships
- Favor composition over inheritance principle
- Dependency injection
- Aggregation vs composition
- Real-world examples and trade-offs

Author: AI Senior Engineer
"""

from abc import ABC, abstractmethod
from typing import List, Optional
import math


# INHERITANCE APPROACH EXAMPLES

class Vehicle:
    """Base vehicle class for inheritance examples."""
    
    def __init__(self, make, model, year):
        """Initialize vehicle."""
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
    
    def start_engine(self):
        """Start the vehicle engine."""
        self.is_running = True
        return f"{self.make} {self.model} engine started"
    
    def stop_engine(self):
        """Stop the vehicle engine."""
        self.is_running = False
        return f"{self.make} {self.model} engine stopped"


class InheritanceCar(Vehicle):
    """
    Car using INHERITANCE approach.
    
    This demonstrates the "IS-A" relationship:
    A Car IS-A Vehicle
    """
    
    def __init__(self, make, model, year, doors=4):
        """Initialize car using inheritance."""
        super().__init__(make, model, year)
        self.doors = doors
        self.trunk_open = False
    
    def open_trunk(self):
        """Open car trunk."""
        self.trunk_open = True
        return "Trunk opened"
    
    def honk(self):
        """Car-specific behavior."""
        return "Beep beep!"


class InheritanceMotorcycle(Vehicle):
    """
    Motorcycle using INHERITANCE approach.
    
    Another "IS-A" relationship:
    A Motorcycle IS-A Vehicle
    """
    
    def __init__(self, make, model, year, engine_size):
        """Initialize motorcycle using inheritance."""
        super().__init__(make, model, year)
        self.engine_size = engine_size
        self.has_helmet = False
    
    def put_on_helmet(self):
        """Put on helmet."""
        self.has_helmet = True
        return "Helmet on - safety first!"
    
    def rev_engine(self):
        """Motorcycle-specific behavior."""
        return "Vrooooom!"


# COMPOSITION APPROACH EXAMPLES

class Engine:
    """
    Engine component for composition examples.
    
    This represents a separate component that can be composed
    into different types of vehicles.
    """
    
    def __init__(self, horsepower, fuel_type="Gasoline"):
        """
        Initialize engine.
        
        Args:
            horsepower (int): Engine power
            fuel_type (str): Type of fuel
        """
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False
        self.temperature = 70  # Fahrenheit
    
    def start(self):
        """Start the engine."""
        if not self.is_running:
            self.is_running = True
            self.temperature = 180
            return f"{self.horsepower}HP {self.fuel_type} engine started"
        return "Engine already running"
    
    def stop(self):
        """Stop the engine."""
        if self.is_running:
            self.is_running = False
            self.temperature = 70
            return f"{self.horsepower}HP engine stopped"
        return "Engine already stopped"
    
    def get_status(self):
        """Get engine status."""
        status = "Running" if self.is_running else "Stopped"
        return f"Engine: {status}, Temp: {self.temperature}°F"


class Wheels:
    """
    Wheels component for composition examples.
    """
    
    def __init__(self, count, size, wheel_type="Standard"):
        """
        Initialize wheels.
        
        Args:
            count (int): Number of wheels
            size (int): Wheel size in inches
            wheel_type (str): Type of wheels
        """
        self.count = count
        self.size = size
        self.wheel_type = wheel_type
        self.pressure = 32  # PSI
    
    def check_pressure(self):
        """Check tire pressure."""
        return f"{self.count} {self.size}\" {self.wheel_type} wheels at {self.pressure} PSI"
    
    def inflate(self, psi):
        """Inflate tires."""
        self.pressure = min(50, self.pressure + psi)
        return f"Tires inflated to {self.pressure} PSI"


class GPS:
    """GPS component that can be added to vehicles."""
    
    def __init__(self):
        """Initialize GPS."""
        self.current_location = "Unknown"
        self.destination = None
        self.is_on = False
    
    def turn_on(self):
        """Turn on GPS."""
        self.is_on = True
        self.current_location = "Current Location"
        return "GPS activated"
    
    def set_destination(self, destination):
        """Set navigation destination."""
        if self.is_on:
            self.destination = destination
            return f"Destination set to {destination}"
        return "GPS is off"
    
    def get_directions(self):
        """Get directions."""
        if self.is_on and self.destination:
            return f"Navigate from {self.current_location} to {self.destination}"
        return "GPS not ready for navigation"


class CompositionCar:
    """
    Car using COMPOSITION approach.
    
    This demonstrates the "HAS-A" relationship:
    A Car HAS-A Engine, HAS-A Wheels, etc.
    
    Instead of inheriting from Vehicle, we compose the car
    from separate, reusable components.
    """
    
    def __init__(self, make, model, year, engine, wheels, has_gps=False):
        """
        Initialize car using composition.
        
        Args:
            make (str): Car manufacturer
            model (str): Car model
            year (int): Manufacturing year
            engine (Engine): Engine component
            wheels (Wheels): Wheels component
            has_gps (bool): Whether car has GPS
        """
        # Basic vehicle properties
        self.make = make
        self.model = model
        self.year = year
        
        # Composed components (HAS-A relationships)
        self.engine = engine
        self.wheels = wheels
        self.gps = GPS() if has_gps else None
        
        # Car-specific properties
        self.doors = 4
        self.trunk_open = False
    
    def start_engine(self):
        """Start engine using composition."""
        return self.engine.start()
    
    def stop_engine(self):
        """Stop engine using composition."""
        return self.engine.stop()
    
    def check_tires(self):
        """Check tire status using composition."""
        return self.wheels.check_pressure()
    
    def open_trunk(self):
        """Open trunk."""
        self.trunk_open = True
        return "Trunk opened"
    
    def navigate_to(self, destination):
        """Use GPS if available."""
        if self.gps:
            self.gps.turn_on()
            return self.gps.set_destination(destination)
        return "No GPS system installed"
    
    def get_status(self):
        """Get complete car status."""
        status = [
            f"Car: {self.year} {self.make} {self.model}",
            self.engine.get_status(),
            self.wheels.check_pressure()
        ]
        
        if self.gps and self.gps.is_on:
            status.append(f"GPS: Active ({self.gps.current_location})")
        
        return "\n".join(status)


class CompositionMotorcycle:
    """
    Motorcycle using COMPOSITION approach.
    
    Shows how the same components can be reused
    in different vehicle types.
    """
    
    def __init__(self, make, model, year, engine):
        """
        Initialize motorcycle using composition.
        
        Args:
            make (str): Motorcycle manufacturer
            model (str): Motorcycle model
            year (int): Manufacturing year
            engine (Engine): Engine component
        """
        self.make = make
        self.model = model
        self.year = year
        
        # Composed components
        self.engine = engine
        self.wheels = Wheels(2, 18, "Sport")  # 2 wheels, 18 inches
        
        # Motorcycle-specific properties
        self.has_helmet = False
        self.sidecar = False
    
    def start_engine(self):
        """Start engine."""
        return self.engine.start()
    
    def stop_engine(self):
        """Stop engine."""
        return self.engine.stop()
    
    def put_on_helmet(self):
        """Put on helmet."""
        self.has_helmet = True
        return "Helmet on - safety first!"
    
    def rev_engine(self):
        """Rev the engine."""
        if self.engine.is_running:
            return "Vrooooom!"
        return "Start engine first"


# ADVANCED COMPOSITION PATTERNS

class AudioSystem:
    """Audio system component."""
    
    def __init__(self, brand, watts):
        """Initialize audio system."""
        self.brand = brand
        self.watts = watts
        self.volume = 0
        self.is_on = False
    
    def turn_on(self):
        """Turn on audio system."""
        self.is_on = True
        return f"{self.brand} audio system on"
    
    def set_volume(self, volume):
        """Set volume level."""
        if self.is_on:
            self.volume = max(0, min(100, volume))
            return f"Volume set to {self.volume}"
        return "Audio system is off"


class ClimateControl:
    """Climate control component."""
    
    def __init__(self):
        """Initialize climate control."""
        self.temperature = 72
        self.is_on = False
        self.mode = "Auto"
    
    def turn_on(self):
        """Turn on climate control."""
        self.is_on = True
        return "Climate control activated"
    
    def set_temperature(self, temp):
        """Set target temperature."""
        if self.is_on:
            self.temperature = max(60, min(85, temp))
            return f"Temperature set to {self.temperature}°F"
        return "Climate control is off"


class LuxuryCar:
    """
    Luxury car using composition with many components.
    
    This demonstrates how composition allows for flexible
    configuration of features.
    """
    
    def __init__(self, make, model, year, engine_hp=300):
        """Initialize luxury car with premium components."""
        self.make = make
        self.model = model
        self.year = year
        
        # Core components
        self.engine = Engine(engine_hp, "Premium")
        self.wheels = Wheels(4, 20, "Performance")
        
        # Luxury features (optional components)
        self.gps = GPS()
        self.audio = AudioSystem("Bose", 1000)
        self.climate = ClimateControl()
        
        # Luxury-specific features
        self.leather_seats = True
        self.sunroof = True
    
    def start_luxury_experience(self):
        """Start all luxury systems."""
        actions = []
        actions.append(self.engine.start())
        actions.append(self.gps.turn_on())
        actions.append(self.audio.turn_on())
        actions.append(self.climate.turn_on())
        actions.append("Luxury experience activated")
        return actions
    
    def set_comfort_settings(self, temp=72, volume=30):
        """Set comfort preferences."""
        settings = []
        settings.append(self.climate.set_temperature(temp))
        settings.append(self.audio.set_volume(volume))
        return settings


# DEPENDENCY INJECTION EXAMPLE

class VehicleFactory:
    """
    Factory demonstrating dependency injection.
    
    Components are injected rather than created internally,
    making the system more flexible and testable.
    """
    
    @staticmethod
    def create_economy_car(make, model, year):
        """Create an economy car with basic components."""
        engine = Engine(120, "Regular")
        wheels = Wheels(4, 15, "Standard")
        return CompositionCar(make, model, year, engine, wheels, has_gps=False)
    
    @staticmethod
    def create_sport_car(make, model, year):
        """Create a sport car with performance components."""
        engine = Engine(400, "Premium")
        wheels = Wheels(4, 19, "Performance")
        return CompositionCar(make, model, year, engine, wheels, has_gps=True)
    
    @staticmethod
    def create_electric_car(make, model, year):
        """Create an electric car."""
        engine = Engine(300, "Electric")
        wheels = Wheels(4, 18, "Low Rolling Resistance")
        return CompositionCar(make, model, year, engine, wheels, has_gps=True)


# AGGREGATION VS COMPOSITION EXAMPLE

class University:
    """
    University demonstrating aggregation.
    
    University HAS Students, but students can exist
    independently of the university (aggregation).
    """
    
    def __init__(self, name):
        """Initialize university."""
        self.name = name
        self.students = []  # Aggregation - students exist independently
    
    def enroll_student(self, student):
        """Enroll an existing student."""
        self.students.append(student)
        student.university = self.name
    
    def graduate_student(self, student):
        """Graduate a student (remove from university)."""
        if student in self.students:
            self.students.remove(student)
            student.university = None


class Student:
    """Student that can exist independently."""
    
    def __init__(self, name, age):
        """Initialize student."""
        self.name = name
        self.age = age
        self.university = None
    
    def __str__(self):
        """String representation."""
        uni = f" at {self.university}" if self.university else ""
        return f"Student: {self.name}{uni}"


class House:
    """
    House demonstrating composition.
    
    House HAS Rooms, but rooms cannot exist
    independently of the house (composition).
    """
    
    def __init__(self, address):
        """Initialize house."""
        self.address = address
        # Composition - rooms are created with house and destroyed with house
        self.rooms = [
            Room("Living Room", 300),
            Room("Kitchen", 150),
            Room("Bedroom", 200),
            Room("Bathroom", 50)
        ]
    
    def get_total_area(self):
        """Calculate total house area."""
        return sum(room.area for room in self.rooms)
    
    def list_rooms(self):
        """List all rooms."""
        return [f"{room.name}: {room.area} sq ft" for room in self.rooms]


class Room:
    """Room that exists only as part of a house."""
    
    def __init__(self, name, area):
        """Initialize room."""
        self.name = name
        self.area = area


def demonstrate_composition_vs_inheritance():
    """
    Demonstration function showing composition vs inheritance trade-offs.
    """
    print("=" * 80)
    print("OBJECT-ORIENTED PROGRAMMING - LESSON 7: COMPOSITION VS INHERITANCE")
    print("=" * 80)
    
    # Inheritance approach
    print("\n1. INHERITANCE APPROACH (IS-A RELATIONSHIPS):")
    print("-" * 55)
    
    inheritance_car = InheritanceCar("Toyota", "Camry", 2023)
    inheritance_bike = InheritanceMotorcycle("Harley", "Street 750", 2023, 750)
    
    print("Inheritance car:")
    print(f"  {inheritance_car.start_engine()}")
    print(f"  {inheritance_car.honk()}")
    print(f"  {inheritance_car.open_trunk()}")
    
    print("\nInheritance motorcycle:")
    print(f"  {inheritance_bike.start_engine()}")
    print(f"  {inheritance_bike.put_on_helmet()}")
    print(f"  {inheritance_bike.rev_engine()}")
    
    # Composition approach
    print("\n2. COMPOSITION APPROACH (HAS-A RELATIONSHIPS):")
    print("-" * 55)
    
    # Create reusable components
    car_engine = Engine(200, "Gasoline")
    car_wheels = Wheels(4, 17, "All-Season")
    
    bike_engine = Engine(750, "Gasoline")
    
    composition_car = CompositionCar("Honda", "Civic", 2023, car_engine, car_wheels, has_gps=True)
    composition_bike = CompositionMotorcycle("Yamaha", "R1", 2023, bike_engine)
    
    print("Composition car:")
    print(f"  {composition_car.start_engine()}")
    print(f"  {composition_car.check_tires()}")
    print(f"  {composition_car.navigate_to('Downtown')}")
    print(f"  {composition_car.open_trunk()}")
    
    print("\nComposition motorcycle:")
    print(f"  {composition_bike.start_engine()}")
    print(f"  {composition_bike.put_on_helmet()}")
    print(f"  {composition_bike.rev_engine()}")
    
    # Component reusability
    print("\n3. COMPONENT REUSABILITY:")
    print("-" * 30)
    
    print("Same engine type used in different vehicles:")
    sports_engine = Engine(500, "Premium")
    
    sports_car = CompositionCar("Ferrari", "488", 2023, sports_engine, Wheels(4, 20, "Performance"))
    sports_bike = CompositionMotorcycle("Ducati", "Panigale", 2023, Engine(500, "Premium"))
    
    print(f"Sports car engine: {sports_car.engine.get_status()}")
    print(f"Sports bike engine: {sports_bike.engine.get_status()}")
    
    # Flexible configuration
    print("\n4. FLEXIBLE CONFIGURATION:")
    print("-" * 35)
    
    luxury_car = LuxuryCar("BMW", "7 Series", 2023)
    luxury_actions = luxury_car.start_luxury_experience()
    
    print("Luxury car startup sequence:")
    for action in luxury_actions:
        print(f"  {action}")
    
    comfort_settings = luxury_car.set_comfort_settings(75, 25)
    print("\nComfort settings:")
    for setting in comfort_settings:
        print(f"  {setting}")
    
    # Factory with dependency injection
    print("\n5. DEPENDENCY INJECTION:")
    print("-" * 30)
    
    economy = VehicleFactory.create_economy_car("Nissan", "Versa", 2023)
    sport = VehicleFactory.create_sport_car("Porsche", "911", 2023)
    electric = VehicleFactory.create_electric_car("Tesla", "Model 3", 2023)
    
    vehicles = [("Economy", economy), ("Sport", sport), ("Electric", electric)]
    
    for name, vehicle in vehicles:
        print(f"\n{name} car:")
        print(f"  Engine: {vehicle.engine.horsepower}HP {vehicle.engine.fuel_type}")
        print(f"  Wheels: {vehicle.wheels.wheel_type}")
        print(f"  GPS: {'Yes' if vehicle.gps else 'No'}")
    
    # Aggregation vs Composition
    print("\n6. AGGREGATION VS COMPOSITION:")
    print("-" * 40)
    
    # Aggregation example
    university = University("Tech University")
    student1 = Student("Alice", 20)
    student2 = Student("Bob", 22)
    
    university.enroll_student(student1)
    university.enroll_student(student2)
    
    print("Aggregation (students exist independently):")
    print(f"  {student1}")
    print(f"  {student2}")
    
    university.graduate_student(student1)
    print(f"After graduation: {student1}")  # Student still exists
    
    # Composition example
    house = House("123 Main St")
    
    print("\nComposition (rooms are part of house):")
    print(f"  House at {house.address}")
    print(f"  Total area: {house.get_total_area()} sq ft")
    print("  Rooms:")
    for room_info in house.list_rooms():
        print(f"    {room_info}")
    
    # When to use each approach
    print("\n7. WHEN TO USE EACH APPROACH:")
    print("-" * 40)
    
    print("Use INHERITANCE when:")
    print("  ✓ True 'IS-A' relationship exists")
    print("  ✓ Shared behavior is extensive")
    print("  ✓ Polymorphism is important")
    print("  ✓ Hierarchy is stable")
    
    print("\nUse COMPOSITION when:")
    print("  ✓ 'HAS-A' relationship exists")
    print("  ✓ Need flexible configuration")
    print("  ✓ Want to reuse components")
    print("  ✓ Avoiding deep inheritance hierarchies")
    print("  ✓ Runtime behavior changes needed")
    
    # Trade-offs summary
    print("\n8. TRADE-OFFS SUMMARY:")
    print("-" * 25)
    
    print("INHERITANCE:")
    print("  Pros: Code reuse, polymorphism, clear hierarchy")
    print("  Cons: Tight coupling, inflexible, deep hierarchies")
    
    print("\nCOMPOSITION:")
    print("  Pros: Flexible, loose coupling, component reuse")
    print("  Cons: More complex, potential interface explosion")
    
    print("\n✨ PRINCIPLE: 'Favor composition over inheritance'")
    print("   Use inheritance for 'IS-A', composition for 'HAS-A'")


if __name__ == "__main__":
    """
    Main execution block.
    """
    demonstrate_composition_vs_inheritance()


"""
KEY CONCEPTS LEARNED IN THIS LESSON:

1. INHERITANCE: "IS-A" relationship
   - Child class IS-A type of parent class
   - Car IS-A Vehicle, Dog IS-A Animal
   - Shares interface and implementation
   - Good for polymorphism and code reuse

2. COMPOSITION: "HAS-A" relationship
   - Object HAS-A component or collaborator
   - Car HAS-A Engine, House HAS-A Room
   - Objects are built from other objects
   - More flexible than inheritance

3. WHEN TO USE INHERITANCE:
   - True "IS-A" relationship exists
   - Extensive shared behavior
   - Polymorphism is important
   - Stable hierarchy
   - Liskov Substitution Principle applies

4. WHEN TO USE COMPOSITION:
   - "HAS-A" relationship exists
   - Need flexible configuration
   - Want component reusability
   - Avoiding deep inheritance trees
   - Runtime behavior changes needed

5. AGGREGATION VS COMPOSITION:
   - Aggregation: Parts can exist independently (University HAS Students)
   - Composition: Parts cannot exist independently (House HAS Rooms)
   - Both are forms of composition in broader sense

6. DEPENDENCY INJECTION:
   - Dependencies are provided externally
   - Makes code more testable and flexible
   - Reduces coupling between components
   - Easier to swap implementations

7. BENEFITS OF COMPOSITION:
   - Loose coupling between components
   - Runtime behavior modification
   - Component reusability
   - Easier testing (mock components)
   - Avoids inheritance problems

8. PROBLEMS WITH INHERITANCE:
   - Tight coupling between parent and child
   - Fragile base class problem
   - Deep hierarchies become complex
   - Hard to change behavior at runtime
   - Diamond problem in multiple inheritance

9. FAVOR COMPOSITION OVER INHERITANCE:
   - Modern design principle
   - Composition is more flexible
   - Easier to maintain and extend
   - Better for complex systems
   - Use inheritance judiciously

10. DESIGN GUIDELINES:
    - Ask "IS-A" or "HAS-A"?
    - Prefer composition for flexibility
    - Use inheritance for true specialization
    - Keep inheritance hierarchies shallow
    - Design for change and reusability

NEXT LESSON: We'll create a comprehensive project combining all OOP concepts!
"""


"""
Object-Oriented Programming Foundation - Lesson 1: Classes and Objects

This lesson covers the fundamental concepts of OOP:
- What are classes and objects?
- How to define a class
- How to create objects (instances)
- Basic class structure
- Instance variables and methods

Author: AI Senior Engineer
"""


class Car:
    """
    A simple Car class to demonstrate basic OOP concepts.
    
    This class represents a car with basic properties and behaviors.
    It demonstrates:
    - Class definition
    - Instance variables (attributes)
    - Instance methods (behaviors)
    - Constructor (__init__ method)
    """
    
    def __init__(self, make, model, year, color="Unknown"):
        """
        Constructor method to initialize a Car object.
        
        Args:
            make (str): The manufacturer of the car (e.g., "Toyota")
            model (str): The model of the car (e.g., "Camry")
            year (int): The year the car was manufactured
            color (str, optional): The color of the car. Defaults to "Unknown"
        
        Note:
            __init__ is a special method called when creating a new object.
            'self' refers to the instance being created.
        """
        # Instance variables (attributes) - unique to each object
        self.make = make          # Brand/manufacturer
        self.model = model        # Model name
        self.year = year          # Manufacturing year
        self.color = color        # Car color
        self.is_running = False   # Current engine state
        self.speed = 0           # Current speed in mph
        self.mileage = 0         # Total miles driven
    
    def start_engine(self):
        """
        Start the car's engine.
        
        Returns:
            str: Message indicating the engine status
        """
        if not self.is_running:
            self.is_running = True
            return f"The {self.year} {self.make} {self.model} engine is now running!"
        else:
            return f"The {self.make} {self.model} engine is already running."
    
    def stop_engine(self):
        """
        Stop the car's engine.
        
        Returns:
            str: Message indicating the engine status
        """
        if self.is_running:
            self.is_running = False
            self.speed = 0  # Car stops when engine is turned off
            return f"The {self.year} {self.make} {self.model} engine is now stopped."
        else:
            return f"The {self.make} {self.model} engine is already stopped."
    
    def accelerate(self, speed_increase):
        """
        Increase the car's speed.
        
        Args:
            speed_increase (int): Amount to increase speed by (mph)
        
        Returns:
            str: Message about the current speed
        """
        if self.is_running:
            self.speed += speed_increase
            return f"Accelerating! Current speed: {self.speed} mph"
        else:
            return "Cannot accelerate. Engine is not running!"
    
    def brake(self, speed_decrease):
        """
        Decrease the car's speed.
        
        Args:
            speed_decrease (int): Amount to decrease speed by (mph)
        
        Returns:
            str: Message about the current speed
        """
        if self.speed > 0:
            self.speed = max(0, self.speed - speed_decrease)  # Don't go below 0
            return f"Braking! Current speed: {self.speed} mph"
        else:
            return "Car is already stopped."
    
    def drive(self, distance):
        """
        Drive the car for a certain distance.
        
        Args:
            distance (float): Distance to drive in miles
        
        Returns:
            str: Message about the trip
        """
        if self.is_running and self.speed > 0:
            self.mileage += distance
            return f"Drove {distance} miles. Total mileage: {self.mileage} miles"
        else:
            return "Cannot drive. Make sure engine is running and speed > 0!"
    
    def get_info(self):
        """
        Get detailed information about the car.
        
        Returns:
            str: Formatted string with car details
        """
        status = "Running" if self.is_running else "Stopped"
        return (f"Car Info:\n"
                f"  Make: {self.make}\n"
                f"  Model: {self.model}\n"
                f"  Year: {self.year}\n"
                f"  Color: {self.color}\n"
                f"  Status: {status}\n"
                f"  Speed: {self.speed} mph\n"
                f"  Mileage: {self.mileage} miles")


def demonstrate_classes_and_objects():
    """
    Demonstration function showing how to use classes and objects.
    """
    print("=" * 60)
    print("OBJECT-ORIENTED PROGRAMMING - LESSON 1: CLASSES & OBJECTS")
    print("=" * 60)
    
    # Creating Car objects (instances of the Car class)
    print("\n1. CREATING CAR OBJECTS:")
    print("-" * 30)
    
    # Create first car
    my_car = Car("Toyota", "Camry", 2022, "Blue")
    print("Created my_car:", my_car.get_info())
    
    # Create second car
    friends_car = Car("Honda", "Civic", 2021, "Red")
    print("\nCreated friends_car:", friends_car.get_info())
    
    # Demonstrate that objects are independent
    print("\n2. DEMONSTRATING OBJECT INDEPENDENCE:")
    print("-" * 40)
    
    print("\nStarting my car:")
    print(my_car.start_engine())
    
    print("\nMy car status:", "Running" if my_car.is_running else "Stopped")
    print("Friend's car status:", "Running" if friends_car.is_running else "Stopped")
    
    print("\nAccelerating my car:")
    print(my_car.accelerate(30))
    print(my_car.accelerate(20))
    
    print("\nDriving my car:")
    print(my_car.drive(15.5))
    
    print("\nFinal car states:")
    print("My car speed:", my_car.speed, "mph")
    print("Friend's car speed:", friends_car.speed, "mph")


if __name__ == "__main__":
    demonstrate_classes_and_objects()

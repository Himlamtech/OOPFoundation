"""
Object-Oriented Programming Foundation - Lesson 2: Inheritance

This lesson covers inheritance concepts in OOP:
- What is inheritance?
- Single inheritance
- Multiple inheritance  
- Method overriding
- super() function
- Method Resolution Order (MRO)
- isinstance() and issubclass()

Author: AI Senior Engineer
"""


class Vehicle:
    """
    Base class representing a general vehicle.
    
    This class serves as a parent class for more specific vehicle types.
    It demonstrates:
    - Base class definition
    - Common attributes and methods
    - Constructor with default values
    """
    
    def __init__(self, make, model, year, fuel_type="Gasoline"):
        """
        Initialize a Vehicle object.
        
        Args:
            make (str): Vehicle manufacturer
            model (str): Vehicle model
            year (int): Manufacturing year
            fuel_type (str, optional): Type of fuel. Defaults to "Gasoline"
        """
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.is_running = False
        self.speed = 0
        self.mileage = 0
    
    def start_engine(self):
        """
        Start the vehicle's engine.
        
        Returns:
            str: Status message
        """
        if not self.is_running:
            self.is_running = True
            return f"The {self.year} {self.make} {self.model} engine is now running!"
        return f"The {self.make} {self.model} engine is already running."
    
    def stop_engine(self):
        """
        Stop the vehicle's engine.
        
        Returns:
            str: Status message
        """
        if self.is_running:
            self.is_running = False
            self.speed = 0
            return f"The {self.year} {self.make} {self.model} engine is now stopped."
        return f"The {self.make} {self.model} engine is already stopped."
    
    def accelerate(self, speed_increase):
        """
        Increase vehicle speed.
        
        Args:
            speed_increase (int): Amount to increase speed
        
        Returns:
            str: Speed status message
        """
        if self.is_running:
            self.speed += speed_increase
            return f"Accelerating! Current speed: {self.speed} mph"
        return "Cannot accelerate. Engine is not running!"
    
    def get_info(self):
        """
        Get vehicle information.
        
        Returns:
            str: Formatted vehicle details
        """
        status = "Running" if self.is_running else "Stopped"
        return (f"Vehicle Info:\n"
                f"  Make: {self.make}\n"
                f"  Model: {self.model}\n"
                f"  Year: {self.year}\n"
                f"  Fuel Type: {self.fuel_type}\n"
                f"  Status: {status}\n"
                f"  Speed: {self.speed} mph\n"
                f"  Mileage: {self.mileage} miles")


class Car(Vehicle):
    """
    Car class that inherits from Vehicle.
    
    This class demonstrates:
    - Single inheritance (Car inherits from Vehicle)
    - Adding new attributes specific to cars
    - Method overriding
    - Using super() to call parent methods
    """
    
    def __init__(self, make, model, year, fuel_type="Gasoline", doors=4, transmission="Automatic"):
        """
        Initialize a Car object.
        
        Args:
            make (str): Car manufacturer
            model (str): Car model
            year (int): Manufacturing year
            fuel_type (str, optional): Type of fuel. Defaults to "Gasoline"
            doors (int, optional): Number of doors. Defaults to 4
            transmission (str, optional): Transmission type. Defaults to "Automatic"
        """
        # Call parent class constructor using super()
        super().__init__(make, model, year, fuel_type)
        
        # Add car-specific attributes
        self.doors = doors
        self.transmission = transmission
        self.trunk_open = False
        self.air_conditioning = False
    
    def open_trunk(self):
        """
        Open the car's trunk.
        
        Returns:
            str: Trunk status message
        """
        if not self.trunk_open:
            self.trunk_open = True
            return "Trunk is now open."
        return "Trunk is already open."
    
    def close_trunk(self):
        """
        Close the car's trunk.
        
        Returns:
            str: Trunk status message
        """
        if self.trunk_open:
            self.trunk_open = False
            return "Trunk is now closed."
        return "Trunk is already closed."
    
    def toggle_ac(self):
        """
        Toggle air conditioning on/off.
        
        Returns:
            str: AC status message
        """
        if self.is_running:
            self.air_conditioning = not self.air_conditioning
            status = "on" if self.air_conditioning else "off"
            return f"Air conditioning is now {status}."
        return "Cannot control AC. Engine is not running!"
    
    def get_info(self):
        """
        Override parent's get_info method to include car-specific details.
        
        Returns:
            str: Formatted car details
        """
        # Get base info from parent class
        base_info = super().get_info()
        
        # Add car-specific information
        trunk_status = "Open" if self.trunk_open else "Closed"
        ac_status = "On" if self.air_conditioning else "Off"
        
        car_specific_info = (f"  Doors: {self.doors}\n"
                           f"  Transmission: {self.transmission}\n"
                           f"  Trunk: {trunk_status}\n"
                           f"  AC: {ac_status}")
        
        # Replace "Vehicle Info:" with "Car Info:" and add car-specific details
        return base_info.replace("Vehicle Info:", "Car Info:") + "\n" + car_specific_info


class Motorcycle(Vehicle):
    """
    Motorcycle class that inherits from Vehicle.
    
    This class demonstrates:
    - Another example of single inheritance
    - Different specialization from the same parent
    - Method overriding with different behavior
    """
    
    def __init__(self, make, model, year, fuel_type="Gasoline", engine_size=600, has_sidecar=False):
        """
        Initialize a Motorcycle object.
        
        Args:
            make (str): Motorcycle manufacturer
            model (str): Motorcycle model
            year (int): Manufacturing year
            fuel_type (str, optional): Type of fuel. Defaults to "Gasoline"
            engine_size (int, optional): Engine size in cc. Defaults to 600
            has_sidecar (bool, optional): Whether motorcycle has sidecar. Defaults to False
        """
        super().__init__(make, model, year, fuel_type)
        self.engine_size = engine_size
        self.has_sidecar = has_sidecar
        self.helmet_count = 0
    
    def put_on_helmet(self):
        """
        Put on a helmet (safety first!).
        
        Returns:
            str: Helmet status message
        """
        max_helmets = 2 if self.has_sidecar else 1
        if self.helmet_count < max_helmets:
            self.helmet_count += 1
            return f"Helmet put on. Total helmets: {self.helmet_count}"
        return f"Maximum helmets ({max_helmets}) already worn!"
    
    def remove_helmet(self):
        """
        Remove a helmet.
        
        Returns:
            str: Helmet status message
        """
        if self.helmet_count > 0:
            self.helmet_count -= 1
            return f"Helmet removed. Total helmets: {self.helmet_count}"
        return "No helmets to remove!"
    
    def accelerate(self, speed_increase):
        """
        Override accelerate method - motorcycles accelerate faster!
        
        Args:
            speed_increase (int): Amount to increase speed
        
        Returns:
            str: Speed status message
        """
        if self.is_running:
            if self.helmet_count == 0:
                return "Safety first! Put on a helmet before riding!"
            
            # Motorcycles accelerate 1.5x faster than regular vehicles
            actual_increase = int(speed_increase * 1.5)
            self.speed += actual_increase
            return f"Vrooom! Rapid acceleration! Current speed: {self.speed} mph"
        return "Cannot accelerate. Engine is not running!"
    
    def get_info(self):
        """
        Override parent's get_info method for motorcycle-specific details.
        
        Returns:
            str: Formatted motorcycle details
        """
        base_info = super().get_info()
        sidecar_status = "Yes" if self.has_sidecar else "No"
        
        motorcycle_info = (f"  Engine Size: {self.engine_size}cc\n"
                         f"  Has Sidecar: {sidecar_status}\n"
                         f"  Helmets Worn: {self.helmet_count}")
        
        return base_info.replace("Vehicle Info:", "Motorcycle Info:") + "\n" + motorcycle_info


class ElectricVehicle:
    """
    Mixin class for electric vehicle functionality.
    
    This class demonstrates:
    - Mixin pattern (class designed to be inherited with other classes)
    - Adding specific functionality that can be combined with other classes
    - Multiple inheritance preparation
    """
    
    def __init__(self, battery_capacity=100, charging_speed="Standard"):
        """
        Initialize electric vehicle components.
        
        Args:
            battery_capacity (int, optional): Battery capacity in kWh. Defaults to 100
            charging_speed (str, optional): Charging speed type. Defaults to "Standard"
        """
        self.battery_capacity = battery_capacity
        self.battery_level = 100  # Start with full battery
        self.charging_speed = charging_speed
        self.is_charging = False
    
    def start_charging(self):
        """
        Start charging the battery.
        
        Returns:
            str: Charging status message
        """
        if not self.is_charging and self.battery_level < 100:
            self.is_charging = True
            return f"Charging started. Current battery: {self.battery_level}%"
        elif self.battery_level >= 100:
            return "Battery is already full!"
        return "Already charging!"
    
    def stop_charging(self):
        """
        Stop charging the battery.
        
        Returns:
            str: Charging status message
        """
        if self.is_charging:
            self.is_charging = False
            return f"Charging stopped. Current battery: {self.battery_level}%"
        return "Not currently charging!"
    
    def use_battery(self, amount):
        """
        Use battery power.
        
        Args:
            amount (int): Amount of battery to use (percentage)
        
        Returns:
            bool: True if enough battery, False otherwise
        """
        if self.battery_level >= amount:
            self.battery_level -= amount
            return True
        return False
    
    def get_electric_info(self):
        """
        Get electric vehicle specific information.
        
        Returns:
            str: Formatted electric vehicle details
        """
        charging_status = "Charging" if self.is_charging else "Not Charging"
        return (f"  Battery Capacity: {self.battery_capacity} kWh\n"
                f"  Battery Level: {self.battery_level}%\n"
                f"  Charging Speed: {self.charging_speed}\n"
                f"  Charging Status: {charging_status}")


class ElectricCar(Car, ElectricVehicle):
    """
    Electric car class demonstrating multiple inheritance.
    
    This class inherits from both Car and ElectricVehicle, demonstrating:
    - Multiple inheritance
    - Method Resolution Order (MRO)
    - Combining functionality from multiple parent classes
    - Diamond problem resolution
    """
    
    def __init__(self, make, model, year, doors=4, transmission="Automatic", 
                 battery_capacity=100, charging_speed="Fast"):
        """
        Initialize an ElectricCar object.
        
        Args:
            make (str): Car manufacturer
            model (str): Car model
            year (int): Manufacturing year
            doors (int, optional): Number of doors. Defaults to 4
            transmission (str, optional): Transmission type. Defaults to "Automatic"
            battery_capacity (int, optional): Battery capacity in kWh. Defaults to 100
            charging_speed (str, optional): Charging speed type. Defaults to "Fast"
        """
        # Initialize Car with electric fuel type
        Car.__init__(self, make, model, year, "Electric", doors, transmission)
        
        # Initialize ElectricVehicle
        ElectricVehicle.__init__(self, battery_capacity, charging_speed)
        
        # Electric car specific attributes
        self.regenerative_braking = True
        self.eco_mode = False
    
    def toggle_eco_mode(self):
        """
        Toggle eco mode on/off.
        
        Returns:
            str: Eco mode status message
        """
        self.eco_mode = not self.eco_mode
        status = "enabled" if self.eco_mode else "disabled"
        return f"Eco mode {status}."
    
    def accelerate(self, speed_increase):
        """
        Override accelerate method for electric cars.
        
        Args:
            speed_increase (int): Amount to increase speed
        
        Returns:
            str: Speed status message
        """
        if not self.is_running:
            return "Cannot accelerate. Vehicle is not on!"
        
        # Check battery level
        battery_needed = speed_increase // 10  # Rough calculation
        if not self.use_battery(battery_needed):
            return "Insufficient battery power!"
        
        # Apply eco mode effects
        if self.eco_mode:
            speed_increase = int(speed_increase * 0.8)  # Reduce acceleration in eco mode
        
        self.speed += speed_increase
        return f"Silent acceleration! Current speed: {self.speed} mph (Battery: {self.battery_level}%)"
    
    def brake(self, speed_decrease):
        """
        Override brake method to include regenerative braking.
        
        Args:
            speed_decrease (int): Amount to decrease speed
        
        Returns:
            str: Braking status message
        """
        if self.speed > 0:
            self.speed = max(0, self.speed - speed_decrease)
            
            # Regenerative braking recovers some battery
            if self.regenerative_braking and self.battery_level < 100:
                recovery = min(speed_decrease // 5, 100 - self.battery_level)
                self.battery_level += recovery
                return (f"Regenerative braking! Speed: {self.speed} mph "
                       f"(Battery recovered: +{recovery}%, Total: {self.battery_level}%)")
            
            return f"Braking! Current speed: {self.speed} mph"
        return "Car is already stopped."
    
    def get_info(self):
        """
        Override get_info to include electric car details.
        
        Returns:
            str: Formatted electric car details
        """
        # Get car info
        car_info = super().get_info()
        
        # Get electric vehicle info
        electric_info = self.get_electric_info()
        
        # Add electric car specific info
        eco_status = "Enabled" if self.eco_mode else "Disabled"
        regen_status = "Enabled" if self.regenerative_braking else "Disabled"
        
        electric_car_info = (f"  Eco Mode: {eco_status}\n"
                           f"  Regenerative Braking: {regen_status}")
        
        return (car_info.replace("Car Info:", "Electric Car Info:") + 
                "\n" + electric_info + "\n" + electric_car_info)


def demonstrate_inheritance():
    """
    Demonstration function showing inheritance concepts.
    
    This function demonstrates:
    - Single inheritance
    - Multiple inheritance
    - Method overriding
    - super() usage
    - isinstance() and issubclass()
    - Method Resolution Order (MRO)
    """
    print("=" * 70)
    print("OBJECT-ORIENTED PROGRAMMING - LESSON 2: INHERITANCE")
    print("=" * 70)
    
    # Single Inheritance Examples
    print("\n1. SINGLE INHERITANCE:")
    print("-" * 30)
    
    # Create instances
    regular_car = Car("Toyota", "Camry", 2023, doors=4)
    motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2023, engine_size=750)
    
    print("Regular Car:")
    print(regular_car.get_info())
    
    print("\nMotorcycle:")
    print(motorcycle.get_info())
    
    # Demonstrate method overriding
    print("\n2. METHOD OVERRIDING:")
    print("-" * 25)
    
    print("Starting vehicles...")
    print(regular_car.start_engine())
    print(motorcycle.start_engine())
    
    print("\nPutting on helmet for motorcycle safety:")
    print(motorcycle.put_on_helmet())
    
    print("\nAccelerating both vehicles:")
    print("Car acceleration:", regular_car.accelerate(20))
    print("Motorcycle acceleration:", motorcycle.accelerate(20))  # Should be faster
    
    # Multiple Inheritance Example
    print("\n3. MULTIPLE INHERITANCE:")
    print("-" * 30)
    
    electric_car = ElectricCar("Tesla", "Model 3", 2023, battery_capacity=75)
    
    print("Electric Car Info:")
    print(electric_car.get_info())
    
    print("\nStarting electric car and testing features:")
    print(electric_car.start_engine())
    print(electric_car.toggle_eco_mode())
    print(electric_car.accelerate(30))
    print(electric_car.brake(15))  # Should show regenerative braking
    
    # Demonstrate isinstance and issubclass
    print("\n4. TYPE CHECKING:")
    print("-" * 20)
    
    vehicles = [regular_car, motorcycle, electric_car]
    
    for i, vehicle in enumerate(vehicles, 1):
        vehicle_name = ["Regular Car", "Motorcycle", "Electric Car"][i-1]
        print(f"\n{vehicle_name} type checks:")
        print(f"  isinstance(Vehicle): {isinstance(vehicle, Vehicle)}")
        print(f"  isinstance(Car): {isinstance(vehicle, Car)}")
        print(f"  isinstance(ElectricVehicle): {isinstance(vehicle, ElectricVehicle)}")
    
    print("\nClass hierarchy checks:")
    print(f"Car is subclass of Vehicle: {issubclass(Car, Vehicle)}")
    print(f"ElectricCar is subclass of Car: {issubclass(ElectricCar, Car)}")
    print(f"ElectricCar is subclass of ElectricVehicle: {issubclass(ElectricCar, ElectricVehicle)}")
    
    # Method Resolution Order (MRO)
    print("\n5. METHOD RESOLUTION ORDER (MRO):")
    print("-" * 40)
    
    print("ElectricCar MRO:")
    for i, cls in enumerate(ElectricCar.__mro__):
        print(f"  {i+1}. {cls.__name__}")
    
    # Demonstrate super() usage
    print("\n6. SUPER() DEMONSTRATION:")
    print("-" * 30)
    
    print("When ElectricCar.get_info() is called:")
    print("1. ElectricCar.get_info() calls super().get_info()")
    print("2. This calls Car.get_info() (next in MRO)")
    print("3. Car.get_info() calls super().get_info()")
    print("4. This calls Vehicle.get_info() (next in MRO)")
    print("5. ElectricCar adds its own information")
    
    # Polymorphism demonstration
    print("\n7. POLYMORPHISM IN ACTION:")
    print("-" * 35)
    
    all_vehicles = [regular_car, motorcycle, electric_car]
    
    print("Accelerating all vehicles by 10 mph:")
    for i, vehicle in enumerate(all_vehicles):
        vehicle_names = ["Regular Car", "Motorcycle", "Electric Car"]
        print(f"{vehicle_names[i]}: {vehicle.accelerate(10)}")


if __name__ == "__main__":
    """
    Main execution block.
    """
    demonstrate_inheritance()


"""
KEY CONCEPTS LEARNED IN THIS LESSON:

1. INHERITANCE: A mechanism where a class (child/derived) inherits attributes 
   and methods from another class (parent/base)
   - Child class gets all functionality of parent class
   - Child class can add new functionality
   - Child class can override parent functionality

2. SINGLE INHERITANCE: One class inherits from one parent class
   - Example: Car inherits from Vehicle
   - Use super() to call parent class methods
   - Child class extends parent functionality

3. MULTIPLE INHERITANCE: One class inherits from multiple parent classes
   - Example: ElectricCar inherits from both Car and ElectricVehicle
   - More complex but very powerful
   - Need to be careful about method conflicts

4. METHOD OVERRIDING: Child class provides specific implementation of parent method
   - Child method replaces parent method
   - Can still call parent method using super()
   - Allows specialization of behavior

5. super() FUNCTION: Used to call parent class methods
   - super().__init__() calls parent constructor
   - super().method_name() calls parent method
   - Ensures proper inheritance chain execution

6. METHOD RESOLUTION ORDER (MRO): Order in which Python looks for methods
   - Uses C3 linearization algorithm
   - Can view with ClassName.__mro__
   - Determines which method gets called in multiple inheritance

7. isinstance() and issubclass(): Functions to check object and class relationships
   - isinstance(obj, Class): checks if obj is instance of Class
   - issubclass(Child, Parent): checks if Child inherits from Parent

8. POLYMORPHISM: Different classes can have methods with same name but different behavior
   - Same interface, different implementations
   - Allows treating different objects uniformly
   - Method overriding enables polymorphism

NEXT LESSON: We'll explore encapsulation and access modifiers!
"""


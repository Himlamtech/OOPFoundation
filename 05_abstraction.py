"""
Object-Oriented Programming Foundation - Lesson 5: Abstraction

This lesson covers abstraction concepts in OOP:
- What is abstraction?
- Abstract Base Classes (ABC)
- Abstract methods and properties
- Interface-like behavior
- Template Method pattern
- Design by contract
- Real-world abstraction examples

Author: AI Senior Engineer
"""

from abc import ABC, abstractmethod, abstractproperty
from typing import Protocol, runtime_checkable
import math


class Animal(ABC):
    """
    Abstract base class representing a general animal.
    
    This class demonstrates:
    - Abstract base class definition using ABC
    - Abstract methods that must be implemented by subclasses
    - Concrete methods that provide common functionality
    - Template method pattern
    """
    
    def __init__(self, name, species, age):
        """
        Initialize an Animal object.
        
        Args:
            name (str): Animal's name
            species (str): Animal's species
            age (int): Animal's age
        """
        self.name = name
        self.species = species
        self.age = age
        self.energy = 100
        self.hunger = 0
    
    @abstractmethod
    def make_sound(self):
        """
        Abstract method - each animal must implement its own sound.
        
        Returns:
            str: The sound the animal makes
        
        Note:
            This method MUST be implemented by any concrete subclass
        """
        pass
    
    @abstractmethod
    def move(self):
        """
        Abstract method - each animal moves differently.
        
        Returns:
            str: Description of how the animal moves
        """
        pass
    
    @abstractmethod
    def eat(self, food):
        """
        Abstract method - each animal has different eating behavior.
        
        Args:
            food (str): Type of food
        
        Returns:
            str: Description of eating behavior
        """
        pass
    
    @property
    @abstractmethod
    def habitat(self):
        """
        Abstract property - each animal has a specific habitat.
        
        Returns:
            str: Animal's natural habitat
        """
        pass
    
    # Concrete methods (implemented in base class)
    def sleep(self):
        """
        Concrete method - all animals sleep similarly.
        
        Returns:
            str: Sleep description
        """
        self.energy = min(100, self.energy + 30)
        return f"{self.name} is sleeping and recovering energy. Energy: {self.energy}"
    
    def get_hungry(self):
        """
        Concrete method - all animals get hungry.
        
        Returns:
            str: Hunger status
        """
        self.hunger = min(100, self.hunger + 20)
        self.energy = max(0, self.energy - 10)
        return f"{self.name} is getting hungry. Hunger: {self.hunger}, Energy: {self.energy}"
    
    def get_status(self):
        """
        Concrete method - common status reporting.
        
        Returns:
            str: Animal's current status
        """
        return (f"Animal Status:\n"
                f"  Name: {self.name}\n"
                f"  Species: {self.species}\n"
                f"  Age: {self.age}\n"
                f"  Habitat: {self.habitat}\n"
                f"  Energy: {self.energy}\n"
                f"  Hunger: {self.hunger}")
    
    def daily_routine(self):
        """
        Template method - defines the structure of daily routine.
        
        This method uses other methods (some abstract, some concrete)
        to define a standard daily routine for all animals.
        
        Returns:
            str: Description of daily activities
        """
        activities = []
        activities.append(f"{self.name} wakes up and {self.make_sound()}")
        activities.append(f"{self.name} starts {self.move()}")
        activities.append(self.eat("food"))
        activities.append(self.move())
        activities.append(self.sleep())
        
        return "Daily Routine:\n" + "\n".join(f"  {activity}" for activity in activities)


class Dog(Animal):
    """
    Concrete Dog class implementing the Animal abstract class.
    
    This class demonstrates:
    - Implementation of all abstract methods
    - Specific behavior for dog type
    - Concrete implementation of abstract properties
    """
    
    def __init__(self, name, breed, age):
        """
        Initialize a Dog object.
        
        Args:
            name (str): Dog's name
            breed (str): Dog's breed
            age (int): Dog's age
        """
        super().__init__(name, "Canine", age)
        self.breed = breed
        self.loyalty = 100
    
    def make_sound(self):
        """
        Implementation of abstract make_sound method.
        
        Returns:
            str: Dog's sound
        """
        return "says 'Woof! Woof!'"
    
    def move(self):
        """
        Implementation of abstract move method.
        
        Returns:
            str: Dog's movement description
        """
        return "running around and wagging tail"
    
    def eat(self, food):
        """
        Implementation of abstract eat method.
        
        Args:
            food (str): Type of food
        
        Returns:
            str: Dog's eating behavior
        """
        self.hunger = max(0, self.hunger - 30)
        self.energy = min(100, self.energy + 20)
        return f"{self.name} is eating {food} enthusiastically"
    
    @property
    def habitat(self):
        """
        Implementation of abstract habitat property.
        
        Returns:
            str: Dog's habitat
        """
        return "Domestic environment"
    
    def fetch(self, item="ball"):
        """
        Dog-specific method not in the abstract class.
        
        Args:
            item (str): Item to fetch
        
        Returns:
            str: Fetch behavior description
        """
        return f"{self.name} fetches the {item} and brings it back!"


class Bird(Animal):
    """
    Concrete Bird class implementing the Animal abstract class.
    
    This class demonstrates another implementation of the same interface
    with bird-specific behaviors.
    """
    
    def __init__(self, name, species, age, can_fly=True):
        """
        Initialize a Bird object.
        
        Args:
            name (str): Bird's name
            species (str): Bird's species
            age (int): Bird's age
            can_fly (bool): Whether the bird can fly
        """
        super().__init__(name, species, age)
        self.can_fly = can_fly
        self.altitude = 0
    
    def make_sound(self):
        """
        Implementation of abstract make_sound method.
        
        Returns:
            str: Bird's sound
        """
        return "chirps and tweets melodiously"
    
    def move(self):
        """
        Implementation of abstract move method.
        
        Returns:
            str: Bird's movement description
        """
        if self.can_fly:
            self.altitude = 50
            return f"flying at {self.altitude} feet high"
        else:
            return "hopping and walking on the ground"
    
    def eat(self, food):
        """
        Implementation of abstract eat method.
        
        Args:
            food (str): Type of food
        
        Returns:
            str: Bird's eating behavior
        """
        self.hunger = max(0, self.hunger - 25)
        self.energy = min(100, self.energy + 15)
        return f"{self.name} is pecking at {food}"
    
    @property
    def habitat(self):
        """
        Implementation of abstract habitat property.
        
        Returns:
            str: Bird's habitat
        """
        return "Trees and sky"
    
    def build_nest(self):
        """
        Bird-specific method.
        
        Returns:
            str: Nest building description
        """
        return f"{self.name} is building a cozy nest in a tree"


# Protocol-based abstraction (Python 3.8+)
@runtime_checkable
class Drawable(Protocol):
    """
    Protocol defining the interface for drawable objects.
    
    This demonstrates interface-like behavior without inheritance.
    Any class that implements these methods can be treated as Drawable.
    """
    
    def draw(self) -> str:
        """Draw the object."""
        ...
    
    def get_area(self) -> float:
        """Get the area of the object."""
        ...


class GeometricShape(ABC):
    """
    Abstract base class for geometric shapes.
    
    This class demonstrates:
    - Abstract methods for calculations
    - Abstract properties for shape characteristics
    - Template methods using abstract components
    """
    
    def __init__(self, name):
        """
        Initialize a GeometricShape.
        
        Args:
            name (str): Name of the shape
        """
        self.name = name
    
    @abstractmethod
    def calculate_area(self):
        """
        Abstract method to calculate area.
        
        Returns:
            float: Area of the shape
        """
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        """
        Abstract method to calculate perimeter.
        
        Returns:
            float: Perimeter of the shape
        """
        pass
    
    @property
    @abstractmethod
    def dimensions(self):
        """
        Abstract property for shape dimensions.
        
        Returns:
            dict: Dictionary of dimension names and values
        """
        pass
    
    def draw(self):
        """
        Implementation of Drawable protocol.
        
        Returns:
            str: ASCII art representation
        """
        return f"Drawing a {self.name}"
    
    def get_area(self):
        """
        Implementation of Drawable protocol.
        
        Returns:
            float: Area of the shape
        """
        return self.calculate_area()
    
    def describe_shape(self):
        """
        Template method using abstract methods.
        
        Returns:
            str: Complete shape description
        """
        return (f"Shape: {self.name}\n"
                f"Dimensions: {self.dimensions}\n"
                f"Area: {self.calculate_area():.2f}\n"
                f"Perimeter: {self.calculate_perimeter():.2f}")


class Square(GeometricShape):
    """
    Concrete Square class implementing GeometricShape.
    """
    
    def __init__(self, side_length):
        """
        Initialize a Square.
        
        Args:
            side_length (float): Length of square's sides
        """
        super().__init__("Square")
        self.side_length = side_length
    
    def calculate_area(self):
        """
        Calculate square area.
        
        Returns:
            float: Area (side²)
        """
        return self.side_length ** 2
    
    def calculate_perimeter(self):
        """
        Calculate square perimeter.
        
        Returns:
            float: Perimeter (4 × side)
        """
        return 4 * self.side_length
    
    @property
    def dimensions(self):
        """
        Get square dimensions.
        
        Returns:
            dict: Square dimensions
        """
        return {"side_length": self.side_length}
    
    def draw(self):
        """
        Override draw method for square-specific ASCII art.
        
        Returns:
            str: ASCII square
        """
        if self.side_length <= 5:
            size = int(self.side_length)
            square = "\n".join("* " * size for _ in range(size))
            return f"Drawing a {self.name}:\n{square}"
        return f"Drawing a large {self.name} (too big to display)"


class RightTriangle(GeometricShape):
    """
    Concrete RightTriangle class implementing GeometricShape.
    """
    
    def __init__(self, base, height):
        """
        Initialize a RightTriangle.
        
        Args:
            base (float): Base length
            height (float): Height
        """
        super().__init__("Right Triangle")
        self.base = base
        self.height = height
    
    def calculate_area(self):
        """
        Calculate triangle area.
        
        Returns:
            float: Area (½ × base × height)
        """
        return 0.5 * self.base * self.height
    
    def calculate_perimeter(self):
        """
        Calculate triangle perimeter.
        
        Returns:
            float: Perimeter (base + height + hypotenuse)
        """
        hypotenuse = math.sqrt(self.base ** 2 + self.height ** 2)
        return self.base + self.height + hypotenuse
    
    @property
    def dimensions(self):
        """
        Get triangle dimensions.
        
        Returns:
            dict: Triangle dimensions
        """
        hypotenuse = math.sqrt(self.base ** 2 + self.height ** 2)
        return {
            "base": self.base,
            "height": self.height,
            "hypotenuse": hypotenuse
        }


# Example of interface-like behavior without ABC
class PaymentProcessor:
    """
    Interface-like class for payment processing.
    
    This class demonstrates how to create interface-like behavior
    without using ABC, relying on documentation and conventions.
    """
    
    def process_payment(self, amount, currency="USD"):
        """
        Process a payment (to be overridden by subclasses).
        
        Args:
            amount (float): Payment amount
            currency (str): Currency code
        
        Returns:
            dict: Payment result
        
        Raises:
            NotImplementedError: If not implemented by subclass
        """
        raise NotImplementedError("Subclasses must implement process_payment")
    
    def validate_payment(self, amount, currency):
        """
        Validate payment details (common functionality).
        
        Args:
            amount (float): Payment amount
            currency (str): Currency code
        
        Returns:
            bool: True if valid, False otherwise
        """
        return amount > 0 and currency in ["USD", "EUR", "GBP", "JPY"]


class CreditCardProcessor(PaymentProcessor):
    """
    Concrete payment processor for credit cards.
    """
    
    def __init__(self, merchant_id):
        """
        Initialize credit card processor.
        
        Args:
            merchant_id (str): Merchant identifier
        """
        self.merchant_id = merchant_id
    
    def process_payment(self, amount, currency="USD"):
        """
        Process credit card payment.
        
        Args:
            amount (float): Payment amount
            currency (str): Currency code
        
        Returns:
            dict: Payment result
        """
        if not self.validate_payment(amount, currency):
            return {"status": "failed", "error": "Invalid payment details"}
        
        # Simulate credit card processing
        return {
            "status": "success",
            "transaction_id": f"CC_{self.merchant_id}_{amount}",
            "amount": amount,
            "currency": currency,
            "processor": "Credit Card"
        }


class PayPalProcessor(PaymentProcessor):
    """
    Concrete payment processor for PayPal.
    """
    
    def __init__(self, api_key):
        """
        Initialize PayPal processor.
        
        Args:
            api_key (str): PayPal API key
        """
        self.api_key = api_key
    
    def process_payment(self, amount, currency="USD"):
        """
        Process PayPal payment.
        
        Args:
            amount (float): Payment amount
            currency (str): Currency code
        
        Returns:
            dict: Payment result
        """
        if not self.validate_payment(amount, currency):
            return {"status": "failed", "error": "Invalid payment details"}
        
        # Simulate PayPal processing
        return {
            "status": "success",
            "transaction_id": f"PP_{self.api_key[:8]}_{amount}",
            "amount": amount,
            "currency": currency,
            "processor": "PayPal"
        }


def demonstrate_abstraction():
    """
    Demonstration function showing abstraction concepts.
    
    This function demonstrates:
    - Abstract base classes and methods
    - Template method pattern
    - Protocol-based interfaces
    - Polymorphism through abstraction
    """
    print("=" * 70)
    print("OBJECT-ORIENTED PROGRAMMING - LESSON 5: ABSTRACTION")
    print("=" * 70)
    
    # Abstract Base Classes
    print("\n1. ABSTRACT BASE CLASSES:")
    print("-" * 35)
    
    # Cannot instantiate abstract class
    print("Trying to create Animal instance (should fail):")
    try:
        animal = Animal("Generic", "Unknown", 5)
    except TypeError as e:
        print(f"Error: {e}")
    
    # Create concrete implementations
    dog = Dog("Buddy", "Golden Retriever", 3)
    bird = Bird("Tweety", "Canary", 2)
    
    print(f"\nCreated dog: {dog.name}")
    print(dog.get_status())
    
    print(f"\nCreated bird: {bird.name}")
    print(bird.get_status())
    
    # Demonstrate polymorphism through abstraction
    print("\n2. POLYMORPHISM THROUGH ABSTRACTION:")
    print("-" * 45)
    
    animals = [dog, bird]
    
    for animal in animals:
        print(f"\n{animal.name}'s daily routine:")
        print(animal.daily_routine())
    
    # Demonstrate abstract properties and methods
    print("\n3. ABSTRACT METHODS & PROPERTIES:")
    print("-" * 40)
    
    print("Each animal has its own implementation:")
    for animal in animals:
        print(f"{animal.name}: {animal.make_sound()}")
        print(f"{animal.name}: {animal.move()}")
        print(f"{animal.name} lives in: {animal.habitat}")
    
    # Geometric shapes abstraction
    print("\n4. GEOMETRIC SHAPES ABSTRACTION:")
    print("-" * 40)
    
    square = Square(4)
    triangle = RightTriangle(3, 4)
    
    shapes = [square, triangle]
    
    for shape in shapes:
        print(f"\n{shape.describe_shape()}")
        print(shape.draw())
    
    # Protocol-based interface
    print("\n5. PROTOCOL-BASED INTERFACES:")
    print("-" * 35)
    
    # Check if shapes implement Drawable protocol
    for shape in shapes:
        if isinstance(shape, Drawable):
            print(f"{shape.name} implements Drawable protocol")
            print(f"  Draw: {shape.draw()}")
            print(f"  Area: {shape.get_area()}")
    
    # Payment processor abstraction
    print("\n6. PAYMENT PROCESSOR ABSTRACTION:")
    print("-" * 40)
    
    cc_processor = CreditCardProcessor("MERCH123")
    paypal_processor = PayPalProcessor("API_KEY_456")
    
    processors = [cc_processor, paypal_processor]
    payment_amount = 99.99
    
    print(f"Processing payment of ${payment_amount}:")
    for processor in processors:
        result = processor.process_payment(payment_amount)
        print(f"  {result['processor']}: {result['status']}")
        if result['status'] == 'success':
            print(f"    Transaction ID: {result['transaction_id']}")
    
    # Template method pattern
    print("\n7. TEMPLATE METHOD PATTERN:")
    print("-" * 35)
    
    print("Template method defines algorithm structure:")
    print("1. Animal.daily_routine() defines the steps")
    print("2. Each step calls abstract or concrete methods")
    print("3. Subclasses provide specific implementations")
    print("4. Same algorithm, different behaviors")
    
    # Benefits of abstraction
    print("\n8. BENEFITS OF ABSTRACTION:")
    print("-" * 35)
    
    print("✓ Hides complex implementation details")
    print("✓ Provides clear interface contracts")
    print("✓ Enables polymorphic behavior") 
    print("✓ Enforces consistent interfaces")
    print("✓ Supports design by contract")
    print("✓ Makes code more maintainable")


if __name__ == "__main__":
    """
    Main execution block.
    """
    demonstrate_abstraction()


"""
KEY CONCEPTS LEARNED IN THIS LESSON:

1. ABSTRACTION: Hiding complex implementation details behind simple interfaces
   - Focus on what an object does, not how it does it
   - Provides essential features while hiding complexity
   - Defines contracts that implementations must follow

2. ABSTRACT BASE CLASSES (ABC): Classes that cannot be instantiated directly
   - Use abc.ABC as base class
   - Define interface that subclasses must implement
   - Cannot create instances of abstract classes

3. ABSTRACT METHODS: Methods declared but not implemented in base class
   - Use @abstractmethod decorator
   - Subclasses MUST implement these methods
   - Enforces consistent interface across implementations

4. ABSTRACT PROPERTIES: Properties that must be implemented by subclasses
   - Use @property and @abstractmethod together
   - Ensures subclasses provide required attributes
   - Can define computed properties

5. TEMPLATE METHOD PATTERN: Algorithm structure defined in base class
   - Base class defines sequence of steps
   - Some steps are abstract (implemented by subclasses)
   - Some steps are concrete (shared implementation)
   - Same algorithm, different behaviors

6. PROTOCOLS: Duck typing with type hints (Python 3.8+)
   - Define expected interface without inheritance
   - @runtime_checkable for runtime type checking
   - More flexible than ABC inheritance

7. INTERFACE-LIKE BEHAVIOR: Classes that define expected behavior
   - Use NotImplementedError for unimplemented methods
   - Document expected interface clearly
   - Provide common functionality where appropriate

8. DESIGN BY CONTRACT: Classes define contracts for behavior
   - Abstract methods define what must be implemented
   - Concrete methods provide guaranteed functionality
   - Clear separation of responsibilities

9. BENEFITS OF ABSTRACTION:
   - Reduces complexity by hiding details
   - Provides consistent interfaces
   - Enables polymorphic behavior
   - Makes code more maintainable
   - Supports loose coupling
   - Enforces design contracts

NEXT LESSON: We'll explore special methods (magic methods) in Python!
"""


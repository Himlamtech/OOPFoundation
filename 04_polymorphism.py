"""
Object-Oriented Programming Foundation - Lesson 4: Polymorphism

This lesson covers polymorphism concepts in OOP:
- What is polymorphism?
- Method overriding
- Method overloading (simulation in Python)
- Duck typing
- Operator overloading
- Interface-like behavior
- Runtime polymorphism

Author: AI Senior Engineer
"""

import math
from typing import Protocol


class Shape:
    """
    Base class for all shapes demonstrating polymorphism.
    
    This class provides a common interface that all shapes will implement.
    Each subclass will provide its own implementation of these methods.
    """
    
    def __init__(self, name):
        """
        Initialize a Shape object.
        
        Args:
            name (str): Name of the shape
        """
        self.name = name
    
    def area(self):
        """
        Calculate the area of the shape.
        
        Returns:
            float: Area of the shape
        
        Note:
            This is meant to be overridden by subclasses
        """
        raise NotImplementedError("Subclasses must implement area() method")
    
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        
        Returns:
            float: Perimeter of the shape
        
        Note:
            This is meant to be overridden by subclasses
        """
        raise NotImplementedError("Subclasses must implement perimeter() method")
    
    def describe(self):
        """
        Provide a description of the shape.
        
        Returns:
            str: Shape description
        """
        return f"This is a {self.name}"
    
    def get_info(self):
        """
        Get complete information about the shape.
        
        Returns:
            str: Formatted shape information
        """
        return (f"Shape: {self.name}\n"
                f"Area: {self.area():.2f}\n"
                f"Perimeter: {self.perimeter():.2f}")


class Rectangle(Shape):
    """
    Rectangle class demonstrating method overriding.
    
    This class overrides the abstract methods from Shape
    to provide rectangle-specific implementations.
    """
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle object.
        
        Args:
            width (float): Width of the rectangle
            height (float): Height of the rectangle
        """
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculate rectangle area.
        
        Returns:
            float: Area (width * height)
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Calculate rectangle perimeter.
        
        Returns:
            float: Perimeter (2 * (width + height))
        """
        return 2 * (self.width + self.height)
    
    def describe(self):
        """
        Override parent's describe method.
        
        Returns:
            str: Rectangle-specific description
        """
        return f"This is a {self.name} with width {self.width} and height {self.height}"


class Circle(Shape):
    """
    Circle class demonstrating method overriding.
    
    This class provides circle-specific implementations
    of the Shape interface.
    """
    
    def __init__(self, radius):
        """
        Initialize a Circle object.
        
        Args:
            radius (float): Radius of the circle
        """
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """
        Calculate circle area.
        
        Returns:
            float: Area (π * radius²)
        """
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """
        Calculate circle perimeter (circumference).
        
        Returns:
            float: Circumference (2 * π * radius)
        """
        return 2 * math.pi * self.radius
    
    def describe(self):
        """
        Override parent's describe method.
        
        Returns:
            str: Circle-specific description
        """
        return f"This is a {self.name} with radius {self.radius}"


class Triangle(Shape):
    """
    Triangle class demonstrating method overriding.
    
    This class provides triangle-specific implementations
    using the three sides of the triangle.
    """
    
    def __init__(self, side_a, side_b, side_c):
        """
        Initialize a Triangle object.
        
        Args:
            side_a (float): First side length
            side_b (float): Second side length  
            side_c (float): Third side length
        
        Raises:
            ValueError: If the sides don't form a valid triangle
        """
        super().__init__("Triangle")
        
        # Validate triangle inequality
        if (side_a + side_b <= side_c or 
            side_a + side_c <= side_b or 
            side_b + side_c <= side_a):
            raise ValueError("Invalid triangle: sides don't satisfy triangle inequality")
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def area(self):
        """
        Calculate triangle area using Heron's formula.
        
        Returns:
            float: Area calculated using Heron's formula
        """
        # Semi-perimeter
        s = self.perimeter() / 2
        
        # Heron's formula: √(s(s-a)(s-b)(s-c))
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def perimeter(self):
        """
        Calculate triangle perimeter.
        
        Returns:
            float: Sum of all three sides
        """
        return self.side_a + self.side_b + self.side_c
    
    def describe(self):
        """
        Override parent's describe method.
        
        Returns:
            str: Triangle-specific description
        """
        return (f"This is a {self.name} with sides "
                f"{self.side_a}, {self.side_b}, and {self.side_c}")


class MathOperations:
    """
    Class demonstrating method overloading simulation in Python.
    
    Python doesn't have true method overloading, but we can simulate it
    using default parameters, *args, **kwargs, and type checking.
    """
    
    def add(self, *args):
        """
        Add multiple numbers or concatenate strings (overloaded behavior).
        
        Args:
            *args: Variable number of arguments to add
        
        Returns:
            Various types: Sum of numbers or concatenated strings
        
        Raises:
            ValueError: If no arguments provided or mixed types
        """
        if not args:
            raise ValueError("At least one argument required")
        
        # Check if all arguments are numbers
        if all(isinstance(arg, (int, float)) for arg in args):
            return sum(args)
        
        # Check if all arguments are strings
        if all(isinstance(arg, str) for arg in args):
            return "".join(args)
        
        # Check if all arguments are lists
        if all(isinstance(arg, list) for arg in args):
            result = []
            for lst in args:
                result.extend(lst)
            return result
        
        # Mixed types - try to convert to strings and concatenate
        return "".join(str(arg) for arg in args)
    
    def multiply(self, a, b=None, repeat=1):
        """
        Multiply in different ways (overloaded behavior).
        
        Args:
            a: First operand (number, string, or list)
            b: Second operand (optional)
            repeat: Number of times to repeat (for string/list multiplication)
        
        Returns:
            Various types: Result of multiplication operation
        """
        if b is None:
            # Single argument - repeat operation
            if isinstance(a, str):
                return a * repeat
            elif isinstance(a, list):
                return a * repeat
            elif isinstance(a, (int, float)):
                return a * repeat
        else:
            # Two arguments - regular multiplication
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                return a * b
            elif isinstance(a, str) and isinstance(b, int):
                return a * b
            elif isinstance(a, list) and isinstance(b, int):
                return a * b
        
        raise ValueError(f"Cannot multiply {type(a)} and {type(b)}")


class Vector:
    """
    Vector class demonstrating operator overloading.
    
    This class shows how to overload operators like +, -, *, ==, etc.
    to work with custom objects in intuitive ways.
    """
    
    def __init__(self, x, y):
        """
        Initialize a Vector object.
        
        Args:
            x (float): X component
            y (float): Y component
        """
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """
        Overload + operator for vector addition.
        
        Args:
            other (Vector): Another vector to add
        
        Returns:
            Vector: New vector with summed components
        
        Raises:
            TypeError: If other is not a Vector
        """
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Vector")
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """
        Overload - operator for vector subtraction.
        
        Args:
            other (Vector): Another vector to subtract
        
        Returns:
            Vector: New vector with subtracted components
        """
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract Vector from Vector")
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """
        Overload * operator for scalar multiplication.
        
        Args:
            scalar (float): Scalar value to multiply by
        
        Returns:
            Vector: New vector with scaled components
        """
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        raise TypeError("Can only multiply Vector by scalar")
    
    def __rmul__(self, scalar):
        """
        Overload * operator for right-side scalar multiplication.
        
        Args:
            scalar (float): Scalar value to multiply by
        
        Returns:
            Vector: New vector with scaled components
        """
        return self.__mul__(scalar)
    
    def __eq__(self, other):
        """
        Overload == operator for vector equality.
        
        Args:
            other (Vector): Another vector to compare
        
        Returns:
            bool: True if vectors are equal, False otherwise
        """
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        """
        String representation for print().
        
        Returns:
            str: Human-readable vector representation
        """
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """
        Official string representation for debugging.
        
        Returns:
            str: Unambiguous vector representation
        """
        return f"Vector(x={self.x}, y={self.y})"
    
    def magnitude(self):
        """
        Calculate vector magnitude (length).
        
        Returns:
            float: Vector magnitude
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def dot_product(self, other):
        """
        Calculate dot product with another vector.
        
        Args:
            other (Vector): Another vector
        
        Returns:
            float: Dot product result
        """
        if not isinstance(other, Vector):
            raise TypeError("Can only calculate dot product with Vector")
        return self.x * other.x + self.y * other.y


# Duck Typing Examples
class Duck:
    """Duck class for duck typing demonstration."""
    
    def make_sound(self):
        """Make duck sound."""
        return "Quack!"
    
    def move(self):
        """Move like a duck."""
        return "Swimming"


class Dog:
    """Dog class for duck typing demonstration."""
    
    def make_sound(self):
        """Make dog sound."""
        return "Woof!"
    
    def move(self):
        """Move like a dog."""
        return "Running"


class Robot:
    """Robot class for duck typing demonstration."""
    
    def make_sound(self):
        """Make robot sound."""
        return "Beep beep!"
    
    def move(self):
        """Move like a robot."""
        return "Rolling"


# Protocol for type hints (Python 3.8+)
class SoundMaker(Protocol):
    """Protocol defining the interface for sound-making objects."""
    
    def make_sound(self) -> str:
        """Make a sound."""
        ...
    
    def move(self) -> str:
        """Move in some way."""
        ...


def animal_actions(animals):
    """
    Function demonstrating duck typing.
    
    Args:
        animals: List of objects that have make_sound() and move() methods
    
    Returns:
        list: List of action descriptions
    
    Note:
        This function doesn't care about the actual type of objects,
        only that they have the required methods (duck typing).
    """
    actions = []
    for animal in animals:
        # Duck typing: if it walks like a duck and quacks like a duck, it's a duck
        sound = animal.make_sound()
        movement = animal.move()
        actions.append(f"It says '{sound}' and is {movement.lower()}")
    return actions


def calculate_total_area(shapes):
    """
    Function demonstrating runtime polymorphism.
    
    Args:
        shapes: List of Shape objects
    
    Returns:
        float: Total area of all shapes
    
    Note:
        This function works with any object that has an area() method,
        regardless of the specific shape type.
    """
    total = 0
    for shape in shapes:
        total += shape.area()  # Polymorphic call - method depends on actual object type
    return total


def demonstrate_polymorphism():
    """
    Demonstration function showing polymorphism concepts.
    
    This function demonstrates:
    - Method overriding
    - Runtime polymorphism
    - Operator overloading
    - Duck typing
    - Method overloading simulation
    """
    print("=" * 70)
    print("OBJECT-ORIENTED PROGRAMMING - LESSON 4: POLYMORPHISM")
    print("=" * 70)
    
    # Method Overriding and Runtime Polymorphism
    print("\n1. METHOD OVERRIDING & RUNTIME POLYMORPHISM:")
    print("-" * 50)
    
    # Create different shapes
    rectangle = Rectangle(5, 3)
    circle = Circle(4)
    triangle = Triangle(3, 4, 5)
    
    shapes = [rectangle, circle, triangle]
    
    print("Different shapes, same interface:")
    for shape in shapes:
        print(f"\n{shape.describe()}")
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")
    
    print(f"\nTotal area of all shapes: {calculate_total_area(shapes):.2f}")
    
    # Method Overloading Simulation
    print("\n2. METHOD OVERLOADING SIMULATION:")
    print("-" * 40)
    
    math_ops = MathOperations()
    
    print("Adding numbers:", math_ops.add(1, 2, 3, 4))
    print("Adding strings:", math_ops.add("Hello", " ", "World"))
    print("Adding lists:", math_ops.add([1, 2], [3, 4], [5, 6]))
    
    print("Multiplying numbers:", math_ops.multiply(5, 3))
    print("Multiplying string:", math_ops.multiply("Hi", 3))
    print("Repeating list:", math_ops.multiply([1, 2], 3))
    
    # Operator Overloading
    print("\n3. OPERATOR OVERLOADING:")
    print("-" * 30)
    
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    
    print(f"Addition (v1 + v2): {v1 + v2}")
    print(f"Subtraction (v1 - v2): {v1 - v2}")
    print(f"Scalar multiplication (v1 * 2): {v1 * 2}")
    print(f"Scalar multiplication (3 * v1): {3 * v1}")
    print(f"Equality (v1 == v2): {v1 == v2}")
    
    print(f"Vector 1 magnitude: {v1.magnitude():.2f}")
    print(f"Dot product (v1 · v2): {v1.dot_product(v2)}")
    
    # Duck Typing
    print("\n4. DUCK TYPING:")
    print("-" * 20)
    
    duck = Duck()
    dog = Dog()
    robot = Robot()
    
    creatures = [duck, dog, robot]
    
    print("Duck typing in action - all objects treated the same:")
    actions = animal_actions(creatures)
    for i, action in enumerate(actions):
        creature_names = ["Duck", "Dog", "Robot"]
        print(f"{creature_names[i]}: {action}")
    
    # Polymorphic behavior with different types
    print("\n5. POLYMORPHIC COLLECTIONS:")
    print("-" * 35)
    
    # Mix different shape types in one collection
    mixed_shapes = [
        Rectangle(2, 3),
        Circle(2),
        Triangle(3, 4, 5),
        Rectangle(1, 8),
        Circle(1.5)
    ]
    
    print("Processing mixed collection of shapes:")
    for i, shape in enumerate(mixed_shapes, 1):
        print(f"{i}. {shape.name}: Area = {shape.area():.2f}")
    
    # Demonstrate isinstance with polymorphism
    print("\n6. TYPE CHECKING WITH POLYMORPHISM:")
    print("-" * 45)
    
    test_shape = Circle(3)
    print(f"test_shape is Circle: {isinstance(test_shape, Circle)}")
    print(f"test_shape is Shape: {isinstance(test_shape, Shape)}")
    print(f"test_shape type: {type(test_shape).__name__}")
    
    # Show how polymorphism enables flexible code
    print("\n7. BENEFITS OF POLYMORPHISM:")
    print("-" * 35)
    
    print("Same function works with all shape types:")
    
    def process_shape(shape):
        """Process any shape polymorphically."""
        return (f"Processing {shape.name}: "
                f"Area={shape.area():.2f}, "
                f"Perimeter={shape.perimeter():.2f}")
    
    for shape in [Rectangle(4, 2), Circle(3), Triangle(6, 8, 10)]:
        print(process_shape(shape))


if __name__ == "__main__":
    """
    Main execution block.
    """
    demonstrate_polymorphism()


"""
KEY CONCEPTS LEARNED IN THIS LESSON:

1. POLYMORPHISM: "Many forms" - same interface, different implementations
   - Objects of different types can be treated uniformly
   - Method calls resolved at runtime based on actual object type
   - Enables writing flexible, extensible code

2. METHOD OVERRIDING: Subclass provides specific implementation of parent method
   - Same method name, different behavior in each subclass
   - Runtime determines which method to call
   - Foundation of polymorphic behavior

3. METHOD OVERLOADING: Multiple methods with same name but different parameters
   - Python doesn't have true overloading (last definition wins)
   - Can simulate with default parameters, *args, **kwargs
   - Use type checking to provide different behaviors

4. OPERATOR OVERLOADING: Defining how operators work with custom objects
   - __add__ for +, __sub__ for -, __mul__ for *, etc.
   - __eq__ for ==, __lt__ for <, __str__ for str()
   - Makes custom objects behave like built-in types

5. DUCK TYPING: "If it walks like a duck and quacks like a duck, it's a duck"
   - Python's approach to polymorphism
   - Focus on object capabilities, not types
   - No need for explicit interfaces or inheritance

6. RUNTIME POLYMORPHISM: Method resolution happens during execution
   - Same code works with different object types
   - Method called depends on actual object type
   - Enables writing generic algorithms

7. PROTOCOLS: Type hints for duck typing (Python 3.8+)
   - Define expected interface without inheritance
   - Static type checkers can verify compatibility
   - Documentation of required methods

8. BENEFITS OF POLYMORPHISM:
   - Code reusability and flexibility
   - Easy to extend with new types
   - Loose coupling between components
   - Clean, readable code

NEXT LESSON: We'll explore abstraction and abstract base classes!
"""


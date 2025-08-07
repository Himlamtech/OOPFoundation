"""
Object-Oriented Programming Foundation - Lesson 6: Special Methods (Magic Methods)

This lesson covers special methods in Python:
- What are special methods (dunder methods)?
- Object creation and destruction (__init__, __del__)
- String representation (__str__, __repr__)
- Arithmetic operators (__add__, __sub__, __mul__, etc.)
- Comparison operators (__eq__, __lt__, __gt__, etc.)
- Container behavior (__len__, __getitem__, __setitem__)
- Attribute access (__getattr__, __setattr__)
- Callable objects (__call__)
- Context managers (__enter__, __exit__)

Author: AI Senior Engineer
"""

import math
from typing import Any, Iterator


class Money:
    """
    Money class demonstrating various special methods.
    
    This class shows how special methods make objects behave
    like built-in types with natural syntax.
    """
    
    def __init__(self, amount, currency="USD"):
        """
        Initialize Money object (__init__ special method).
        
        Args:
            amount (float): Monetary amount
            currency (str): Currency code (default: USD)
        
        Raises:
            ValueError: If amount is negative or currency is invalid
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        
        valid_currencies = ["USD", "EUR", "GBP", "JPY", "CAD"]
        if currency not in valid_currencies:
            raise ValueError(f"Currency must be one of: {valid_currencies}")
        
        self.amount = amount
        self.currency = currency
    
    def __str__(self):
        """
        String representation for end users (__str__ special method).
        
        This method is called by str() and print().
        
        Returns:
            str: Human-readable representation
        """
        return f"{self.currency} {self.amount:.2f}"
    
    def __repr__(self):
        """
        Official string representation (__repr__ special method).
        
        This method is called by repr() and in interactive sessions.
        Should be unambiguous and ideally eval-able.
        
        Returns:
            str: Unambiguous representation
        """
        return f"Money({self.amount}, '{self.currency}')"
    
    def __add__(self, other):
        """
        Addition operator (__add__ special method).
        
        Args:
            other (Money): Another Money object to add
        
        Returns:
            Money: New Money object with sum
        
        Raises:
            TypeError: If other is not Money
            ValueError: If currencies don't match
        """
        if not isinstance(other, Money):
            raise TypeError("Can only add Money to Money")
        
        if self.currency != other.currency:
            raise ValueError(f"Cannot add {self.currency} and {other.currency}")
        
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other):
        """
        Subtraction operator (__sub__ special method).
        
        Args:
            other (Money): Money object to subtract
        
        Returns:
            Money: New Money object with difference
        """
        if not isinstance(other, Money):
            raise TypeError("Can only subtract Money from Money")
        
        if self.currency != other.currency:
            raise ValueError(f"Cannot subtract {other.currency} from {self.currency}")
        
        result_amount = self.amount - other.amount
        if result_amount < 0:
            raise ValueError("Result would be negative")
        
        return Money(result_amount, self.currency)
    
    def __mul__(self, scalar):
        """
        Multiplication operator (__mul__ special method).
        
        Args:
            scalar (float): Number to multiply by
        
        Returns:
            Money: New Money object with multiplied amount
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply Money by number")
        
        if scalar < 0:
            raise ValueError("Cannot multiply by negative number")
        
        return Money(self.amount * scalar, self.currency)
    
    def __rmul__(self, scalar):
        """
        Right multiplication operator (__rmul__ special method).
        
        This allows scalar * money syntax.
        
        Args:
            scalar (float): Number to multiply by
        
        Returns:
            Money: New Money object with multiplied amount
        """
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        """
        Division operator (__truediv__ special method).
        
        Args:
            scalar (float): Number to divide by
        
        Returns:
            Money: New Money object with divided amount
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only divide Money by number")
        
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        if scalar < 0:
            raise ValueError("Cannot divide by negative number")
        
        return Money(self.amount / scalar, self.currency)
    
    def __eq__(self, other):
        """
        Equality comparison (__eq__ special method).
        
        Args:
            other (Money): Money object to compare
        
        Returns:
            bool: True if equal, False otherwise
        """
        if not isinstance(other, Money):
            return False
        
        return (self.amount == other.amount and 
                self.currency == other.currency)
    
    def __lt__(self, other):
        """
        Less than comparison (__lt__ special method).
        
        Args:
            other (Money): Money object to compare
        
        Returns:
            bool: True if self < other
        """
        if not isinstance(other, Money):
            raise TypeError("Can only compare Money with Money")
        
        if self.currency != other.currency:
            raise ValueError(f"Cannot compare {self.currency} with {other.currency}")
        
        return self.amount < other.amount
    
    def __le__(self, other):
        """
        Less than or equal comparison (__le__ special method).
        
        Args:
            other (Money): Money object to compare
        
        Returns:
            bool: True if self <= other
        """
        return self < other or self == other
    
    def __gt__(self, other):
        """
        Greater than comparison (__gt__ special method).
        
        Args:
            other (Money): Money object to compare
        
        Returns:
            bool: True if self > other
        """
        return not self <= other
    
    def __ge__(self, other):
        """
        Greater than or equal comparison (__ge__ special method).
        
        Args:
            other (Money): Money object to compare
        
        Returns:
            bool: True if self >= other
        """
        return not self < other
    
    def __hash__(self):
        """
        Hash function (__hash__ special method).
        
        This allows Money objects to be used in sets and as dict keys.
        
        Returns:
            int: Hash value
        """
        return hash((self.amount, self.currency))
    
    def __bool__(self):
        """
        Boolean conversion (__bool__ special method).
        
        Returns:
            bool: True if amount > 0, False otherwise
        """
        return self.amount > 0


class ShoppingCart:
    """
    Shopping cart class demonstrating container special methods.
    
    This class shows how to make objects behave like containers
    (lists, dicts) using special methods.
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []
        self.discounts = {}
    
    def __len__(self):
        """
        Length function (__len__ special method).
        
        This allows len(cart) to work.
        
        Returns:
            int: Number of items in cart
        """
        return len(self.items)
    
    def __getitem__(self, index):
        """
        Index access (__getitem__ special method).
        
        This allows cart[index] syntax.
        
        Args:
            index (int): Index of item to get
        
        Returns:
            dict: Item at the specified index
        """
        return self.items[index]
    
    def __setitem__(self, index, item):
        """
        Index assignment (__setitem__ special method).
        
        This allows cart[index] = item syntax.
        
        Args:
            index (int): Index to set
            item (dict): Item to set at index
        """
        if not isinstance(item, dict) or 'name' not in item or 'price' not in item:
            raise ValueError("Item must be dict with 'name' and 'price' keys")
        
        self.items[index] = item
    
    def __delitem__(self, index):
        """
        Index deletion (__delitem__ special method).
        
        This allows del cart[index] syntax.
        
        Args:
            index (int): Index of item to delete
        """
        del self.items[index]
    
    def __contains__(self, item_name):
        """
        Membership test (__contains__ special method).
        
        This allows 'item' in cart syntax.
        
        Args:
            item_name (str): Name of item to check
        
        Returns:
            bool: True if item is in cart
        """
        return any(item['name'] == item_name for item in self.items)
    
    def __iter__(self):
        """
        Iterator protocol (__iter__ special method).
        
        This allows for item in cart syntax.
        
        Returns:
            Iterator: Iterator over cart items
        """
        return iter(self.items)
    
    def __add__(self, other_cart):
        """
        Addition of two carts (__add__ special method).
        
        Args:
            other_cart (ShoppingCart): Another cart to combine
        
        Returns:
            ShoppingCart: New cart with combined items
        """
        if not isinstance(other_cart, ShoppingCart):
            raise TypeError("Can only add ShoppingCart to ShoppingCart")
        
        new_cart = ShoppingCart()
        new_cart.items = self.items + other_cart.items
        return new_cart
    
    def add_item(self, name, price, quantity=1):
        """
        Add item to cart.
        
        Args:
            name (str): Item name
            price (float): Item price
            quantity (int): Quantity to add
        """
        item = {
            'name': name,
            'price': price,
            'quantity': quantity
        }
        self.items.append(item)
    
    def get_total(self):
        """
        Calculate total cart value.
        
        Returns:
            float: Total value of all items
        """
        total = sum(item['price'] * item['quantity'] for item in self.items)
        
        # Apply discounts
        for item_name, discount in self.discounts.items():
            if item_name in self:
                item = next(item for item in self.items if item['name'] == item_name)
                total -= item['price'] * item['quantity'] * discount
        
        return max(0, total)  # Don't allow negative totals
    
    def __str__(self):
        """String representation of cart."""
        if not self.items:
            return "Empty shopping cart"
        
        lines = ["Shopping Cart:"]
        for item in self.items:
            lines.append(f"  {item['name']} x{item['quantity']} @ ${item['price']:.2f}")
        
        lines.append(f"Total: ${self.get_total():.2f}")
        return "\n".join(lines)


class Counter:
    """
    Counter class demonstrating callable objects and attribute access.
    
    This class shows __call__ method to make objects callable like functions,
    and attribute access methods.
    """
    
    def __init__(self, initial_value=0, step=1):
        """
        Initialize counter.
        
        Args:
            initial_value (int): Starting value
            step (int): Increment step
        """
        self._value = initial_value
        self._step = step
        self._history = [initial_value]
    
    def __call__(self, increment=None):
        """
        Make object callable (__call__ special method).
        
        This allows counter() syntax to increment and return value.
        
        Args:
            increment (int, optional): Custom increment value
        
        Returns:
            int: New counter value
        """
        if increment is None:
            increment = self._step
        
        self._value += increment
        self._history.append(self._value)
        return self._value
    
    def __getattr__(self, name):
        """
        Handle attribute access for non-existent attributes (__getattr__).
        
        This is called only when the attribute doesn't exist normally.
        
        Args:
            name (str): Attribute name
        
        Returns:
            Any: Computed attribute value
        
        Raises:
            AttributeError: If attribute cannot be computed
        """
        if name == 'current':
            return self._value
        elif name == 'history':
            return self._history.copy()  # Return copy to prevent modification
        elif name == 'total_increments':
            return len(self._history) - 1
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
    
    def __setattr__(self, name, value):
        """
        Handle attribute setting (__setattr__).
        
        This is called for ALL attribute assignments.
        
        Args:
            name (str): Attribute name
            value: Attribute value
        """
        if name.startswith('_'):
            # Allow private attributes to be set normally
            super().__setattr__(name, value)
        elif name == 'value':
            # Special handling for 'value' attribute
            self._value = value
            self._history.append(value)
        elif name in ['step', 'history', 'current']:
            # Read-only attributes
            raise AttributeError(f"'{name}' is read-only")
        else:
            # Other attributes set normally
            super().__setattr__(name, value)
    
    def reset(self):
        """Reset counter to initial value."""
        initial = self._history[0]
        self._value = initial
        self._history = [initial]
    
    def __str__(self):
        """String representation."""
        return f"Counter(value={self._value}, step={self._step})"


class FileManager:
    """
    File manager class demonstrating context manager protocol.
    
    This class shows __enter__ and __exit__ methods for use with
    'with' statements.
    """
    
    def __init__(self, filename, mode='r'):
        """
        Initialize file manager.
        
        Args:
            filename (str): File path
            mode (str): File open mode
        """
        self.filename = filename
        self.mode = mode
        self.file = None
        self.opened_successfully = False
    
    def __enter__(self):
        """
        Context manager entry (__enter__ special method).
        
        This is called when entering 'with' block.
        
        Returns:
            FileManager: Self for use in 'with' statement
        """
        try:
            self.file = open(self.filename, self.mode)
            self.opened_successfully = True
            print(f"File '{self.filename}' opened successfully")
            return self
        except Exception as e:
            print(f"Failed to open file '{self.filename}': {e}")
            raise
    
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Context manager exit (__exit__ special method).
        
        This is called when exiting 'with' block, even if an exception occurred.
        
        Args:
            exc_type: Exception type (None if no exception)
            exc_value: Exception value
            traceback: Exception traceback
        
        Returns:
            bool: True to suppress exception, False to propagate
        """
        if self.file and self.opened_successfully:
            self.file.close()
            print(f"File '{self.filename}' closed successfully")
        
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
            return False  # Don't suppress the exception
        
        return True
    
    def write(self, content):
        """
        Write content to file.
        
        Args:
            content (str): Content to write
        """
        if self.file:
            self.file.write(content)
        else:
            raise RuntimeError("File not opened")
    
    def read(self):
        """
        Read content from file.
        
        Returns:
            str: File content
        """
        if self.file:
            return self.file.read()
        else:
            raise RuntimeError("File not opened")


def demonstrate_special_methods():
    """
    Demonstration function showing special methods in action.
    
    This function demonstrates:
    - Object creation and string representation
    - Arithmetic and comparison operators
    - Container behavior
    - Callable objects
    - Context managers
    - Attribute access control
    """
    print("=" * 70)
    print("OBJECT-ORIENTED PROGRAMMING - LESSON 6: SPECIAL METHODS")
    print("=" * 70)
    
    # String representation methods
    print("\n1. STRING REPRESENTATION METHODS:")
    print("-" * 40)
    
    money1 = Money(100, "USD")
    money2 = Money(50.75, "USD")
    
    print(f"str(money1): {str(money1)}")
    print(f"repr(money1): {repr(money1)}")
    print(f"Direct print: {money1}")
    
    # Arithmetic operators
    print("\n2. ARITHMETIC OPERATORS:")
    print("-" * 30)
    
    total = money1 + money2
    print(f"{money1} + {money2} = {total}")
    
    difference = money1 - money2
    print(f"{money1} - {money2} = {difference}")
    
    doubled = money1 * 2
    print(f"{money1} * 2 = {doubled}")
    
    halved = money1 / 2
    print(f"{money1} / 2 = {halved}")
    
    # Comparison operators
    print("\n3. COMPARISON OPERATORS:")
    print("-" * 30)
    
    print(f"{money1} == {money2}: {money1 == money2}")
    print(f"{money1} > {money2}: {money1 > money2}")
    print(f"{money1} < {money2}: {money1 < money2}")
    print(f"{money1} >= {money2}: {money1 >= money2}")
    
    # Boolean conversion
    print(f"bool({money1}): {bool(money1)}")
    print(f"bool(Money(0)): {bool(Money(0))}")
    
    # Container behavior
    print("\n4. CONTAINER BEHAVIOR:")
    print("-" * 25)
    
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50, 3)
    cart.add_item("Banana", 0.75, 5)
    cart.add_item("Orange", 2.00, 2)
    
    print(f"Cart length: {len(cart)}")
    print(f"First item: {cart[0]}")
    print(f"'Apple' in cart: {'Apple' in cart}")
    print(f"'Grape' in cart: {'Grape' in cart}")
    
    print("\nIterating over cart:")
    for item in cart:
        print(f"  {item['name']}: {item['quantity']} @ ${item['price']}")
    
    print(f"\n{cart}")
    
    # Callable objects
    print("\n5. CALLABLE OBJECTS:")
    print("-" * 25)
    
    counter = Counter(0, 5)
    print(f"Initial counter: {counter}")
    
    print(f"Call counter(): {counter()}")  # Increment by step (5)
    print(f"Call counter(10): {counter(10)}")  # Increment by 10
    print(f"Call counter(): {counter()}")  # Increment by step again
    
    print(f"Current value: {counter.current}")
    print(f"Total increments: {counter.total_increments}")
    print(f"History: {counter.history}")
    
    # Attribute access control
    print("\n6. ATTRIBUTE ACCESS CONTROL:")
    print("-" * 35)
    
    print("Trying to set read-only attribute:")
    try:
        counter.history = [1, 2, 3]  # Should fail
    except AttributeError as e:
        print(f"Error: {e}")
    
    print("Setting value through special handling:")
    counter.value = 100
    print(f"New value: {counter.current}")
    
    # Context manager
    print("\n7. CONTEXT MANAGER:")
    print("-" * 25)
    
    # Create a temporary file for demonstration
    test_filename = "/tmp/test_file.txt"
    
    print("Using context manager to write file:")
    try:
        with FileManager(test_filename, 'w') as fm:
            fm.write("Hello, World!\n")
            fm.write("This is a test file.\n")
        print("File operations completed successfully")
    except Exception as e:
        print(f"Error during file operations: {e}")
    
    print("\nUsing context manager to read file:")
    try:
        with FileManager(test_filename, 'r') as fm:
            content = fm.read()
            print(f"File content:\n{content}")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    # Hash and set behavior
    print("\n8. HASH AND SET BEHAVIOR:")
    print("-" * 30)
    
    money_set = {money1, money2, Money(100, "USD")}
    print(f"Money set (duplicates removed): {len(money_set)} items")
    
    money_dict = {
        money1: "First amount",
        money2: "Second amount",
        Money(75, "USD"): "Third amount"
    }
    print(f"Money as dict keys: {len(money_dict)} entries")
    
    # Special method summary
    print("\n9. SPECIAL METHODS SUMMARY:")
    print("-" * 35)
    
    print("Object lifecycle:")
    print("  __init__: Constructor")
    print("  __del__: Destructor (rarely used)")
    
    print("\nString representation:")
    print("  __str__: Human-readable (str(), print())")
    print("  __repr__: Developer-friendly (repr(), interactive)")
    
    print("\nArithmetic operators:")
    print("  __add__, __sub__, __mul__, __truediv__")
    print("  __radd__, __rsub__, __rmul__, __rtruediv__")
    
    print("\nComparison operators:")
    print("  __eq__, __ne__, __lt__, __le__, __gt__, __ge__")
    
    print("\nContainer behavior:")
    print("  __len__, __getitem__, __setitem__, __delitem__")
    print("  __contains__, __iter__")
    
    print("\nAttribute access:")
    print("  __getattr__, __setattr__, __delattr__")
    
    print("\nOther important ones:")
    print("  __call__: Make object callable")
    print("  __bool__: Boolean conversion")
    print("  __hash__: Hash for sets/dicts")
    print("  __enter__, __exit__: Context manager")


if __name__ == "__main__":
    """
    Main execution block.
    """
    demonstrate_special_methods()


"""
KEY CONCEPTS LEARNED IN THIS LESSON:

1. SPECIAL METHODS (MAGIC METHODS): Methods with double underscores
   - Define how objects behave with built-in functions and operators
   - Make custom objects work like built-in types
   - Follow naming convention: __methodname__

2. OBJECT LIFECYCLE:
   - __init__: Constructor (object creation)
   - __del__: Destructor (object deletion, rarely used)

3. STRING REPRESENTATION:
   - __str__: Human-readable string (str(), print())
   - __repr__: Unambiguous representation (repr(), debugging)
   - __str__ for users, __repr__ for developers

4. ARITHMETIC OPERATORS:
   - __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, __pow__
   - __radd__, __rsub__, etc. for right-side operations (3 + obj)
   - __iadd__, __isub__, etc. for in-place operations (+=, -=)

5. COMPARISON OPERATORS:
   - __eq__: Equality (==)
   - __ne__: Inequality (!=) - usually not needed if __eq__ defined
   - __lt__, __le__, __gt__, __ge__: Ordering (<, <=, >, >=)

6. CONTAINER BEHAVIOR:
   - __len__: Length (len())
   - __getitem__: Index access (obj[key])
   - __setitem__: Index assignment (obj[key] = value)
   - __delitem__: Index deletion (del obj[key])
   - __contains__: Membership (item in obj)
   - __iter__: Iterator (for item in obj)

7. CALLABLE OBJECTS:
   - __call__: Make object callable like function (obj())
   - Useful for creating function-like objects with state

8. ATTRIBUTE ACCESS:
   - __getattr__: Called when attribute doesn't exist
   - __setattr__: Called for ALL attribute assignments
   - __delattr__: Called when deleting attributes
   - __getattribute__: Called for ALL attribute access (advanced)

9. CONTEXT MANAGERS:
   - __enter__: Setup when entering 'with' block
   - __exit__: Cleanup when exiting 'with' block
   - Ensures proper resource management

10. OTHER IMPORTANT METHODS:
    - __bool__: Truth value testing (bool(), if obj:)
    - __hash__: Hash value for sets/dict keys
    - __copy__, __deepcopy__: Control copying behavior
    - __sizeof__: Memory size information

11. BENEFITS OF SPECIAL METHODS:
    - Natural, intuitive syntax for custom objects
    - Integration with built-in functions and operators
    - Polymorphic behavior with built-in types
    - Clean, readable code

NEXT LESSON: We'll explore composition vs inheritance design patterns!
"""


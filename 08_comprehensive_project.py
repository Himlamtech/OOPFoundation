"""
Object-Oriented Programming Foundation - Comprehensive Project

This project demonstrates ALL OOP concepts learned:
1. Classes and Objects
2. Inheritance (Single and Multiple)
3. Encapsulation (Private/Protected members)
4. Polymorphism (Method overriding, operator overloading)
5. Abstraction (Abstract classes, interfaces)
6. Special Methods (Magic methods)
7. Composition vs Inheritance

PROJECT: E-Commerce System with Shopping Cart, Payment Processing, and User Management

Author: AI Senior Engineer
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Protocol
from datetime import datetime
import uuid
import hashlib


# ABSTRACT BASE CLASSES AND INTERFACES

class Payable(ABC):
    """
    Abstract base class for payment processing.
    
    Demonstrates: Abstraction, Abstract methods
    """
    
    @abstractmethod
    def process_payment(self, amount: float) -> Dict:
        """Process payment and return result."""
        pass
    
    @abstractmethod
    def validate_payment_info(self) -> bool:
        """Validate payment information."""
        pass


class Discountable(Protocol):
    """
    Protocol for objects that can have discounts applied.
    
    Demonstrates: Duck typing, Protocol-based interfaces
    """
    
    def apply_discount(self, percentage: float) -> float:
        """Apply discount and return new price."""
        ...
    
    def get_original_price(self) -> float:
        """Get original price before discount."""
        ...


# COMPONENT CLASSES FOR COMPOSITION

class Address:
    """
    Address component for composition.
    
    Demonstrates: Composition, Encapsulation
    """
    
    def __init__(self, street: str, city: str, state: str, zip_code: str, country: str = "USA"):
        """Initialize address."""
        self._street = street
        self._city = city
        self._state = state
        self._zip_code = zip_code
        self._country = country
    
    @property
    def street(self) -> str:
        """Get street address."""
        return self._street
    
    @property
    def full_address(self) -> str:
        """Get formatted full address."""
        return f"{self._street}, {self._city}, {self._state} {self._zip_code}, {self._country}"
    
    def __str__(self) -> str:
        """String representation."""
        return self.full_address
    
    def __eq__(self, other) -> bool:
        """Check address equality."""
        if not isinstance(other, Address):
            return False
        return (self._street == other._street and 
                self._city == other._city and 
                self._state == other._state and 
                self._zip_code == other._zip_code)


class Money:
    """
    Money class with operator overloading.
    
    Demonstrates: Special methods, Operator overloading, Encapsulation
    """
    
    def __init__(self, amount: float, currency: str = "USD"):
        """Initialize money object."""
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        
        self._amount = round(amount, 2)
        self._currency = currency.upper()
    
    @property
    def amount(self) -> float:
        """Get amount."""
        return self._amount
    
    @property
    def currency(self) -> str:
        """Get currency."""
        return self._currency
    
    def __str__(self) -> str:
        """String representation for users."""
        return f"${self._amount:.2f} {self._currency}"
    
    def __repr__(self) -> str:
        """String representation for developers."""
        return f"Money({self._amount}, '{self._currency}')"
    
    def __add__(self, other):
        """Add two Money objects."""
        if not isinstance(other, Money):
            raise TypeError("Can only add Money to Money")
        if self._currency != other._currency:
            raise ValueError(f"Cannot add {self._currency} and {other._currency}")
        
        return Money(self._amount + other._amount, self._currency)
    
    def __sub__(self, other):
        """Subtract Money objects."""
        if not isinstance(other, Money):
            raise TypeError("Can only subtract Money from Money")
        if self._currency != other._currency:
            raise ValueError(f"Cannot subtract {other._currency} from {self._currency}")
        
        result = self._amount - other._amount
        if result < 0:
            raise ValueError("Result would be negative")
        
        return Money(result, self._currency)
    
    def __mul__(self, scalar):
        """Multiply by scalar."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply Money by number")
        if scalar < 0:
            raise ValueError("Cannot multiply by negative number")
        
        return Money(self._amount * scalar, self._currency)
    
    def __rmul__(self, scalar):
        """Right multiplication."""
        return self.__mul__(scalar)
    
    def __eq__(self, other) -> bool:
        """Check equality."""
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount and self._currency == other._currency
    
    def __lt__(self, other) -> bool:
        """Less than comparison."""
        if not isinstance(other, Money):
            raise TypeError("Can only compare Money with Money")
        if self._currency != other._currency:
            raise ValueError(f"Cannot compare {self._currency} with {other._currency}")
        
        return self._amount < other._amount
    
    def __le__(self, other) -> bool:
        """Less than or equal."""
        return self < other or self == other
    
    def __gt__(self, other) -> bool:
        """Greater than."""
        return not self <= other
    
    def __ge__(self, other) -> bool:
        """Greater than or equal."""
        return not self < other
    
    def __hash__(self) -> int:
        """Hash for use in sets/dicts."""
        return hash((self._amount, self._currency))


# PRODUCT HIERARCHY WITH INHERITANCE

class Product(ABC):
    """
    Abstract base class for all products.
    
    Demonstrates: Abstraction, Inheritance, Encapsulation
    """
    
    _next_id = 1
    
    def __init__(self, name: str, price: Money, description: str = ""):
        """Initialize product."""
        self._id = Product._next_id
        Product._next_id += 1
        
        self._name = name
        self._price = price
        self._description = description
        self._in_stock = True
    
    @property
    def id(self) -> int:
        """Get product ID."""
        return self._id
    
    @property
    def name(self) -> str:
        """Get product name."""
        return self._name
    
    @property
    def price(self) -> Money:
        """Get product price."""
        return self._price
    
    @property
    def description(self) -> str:
        """Get product description."""
        return self._description
    
    @property
    def in_stock(self) -> bool:
        """Check if product is in stock."""
        return self._in_stock
    
    @in_stock.setter
    def in_stock(self, value: bool):
        """Set stock status."""
        self._in_stock = value
    
    @abstractmethod
    def get_category(self) -> str:
        """Get product category."""
        pass
    
    @abstractmethod
    def get_shipping_weight(self) -> float:
        """Get shipping weight in pounds."""
        pass
    
    def apply_discount(self, percentage: float) -> float:
        """
        Apply discount (implements Discountable protocol).
        
        Args:
            percentage: Discount percentage (0-100)
        
        Returns:
            New price after discount
        """
        if not 0 <= percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        
        discount_amount = self._price.amount * (percentage / 100)
        new_amount = self._price.amount - discount_amount
        return new_amount
    
    def get_original_price(self) -> float:
        """Get original price (implements Discountable protocol)."""
        return self._price.amount
    
    def __str__(self) -> str:
        """String representation."""
        status = "In Stock" if self._in_stock else "Out of Stock"
        return f"{self._name} - {self._price} ({status})"
    
    def __eq__(self, other) -> bool:
        """Check product equality."""
        if not isinstance(other, Product):
            return False
        return self._id == other._id


class Book(Product):
    """
    Book product class.
    
    Demonstrates: Inheritance, Method overriding
    """
    
    def __init__(self, title: str, author: str, isbn: str, price: Money, pages: int):
        """Initialize book."""
        super().__init__(title, price, f"By {author}")
        self._author = author
        self._isbn = isbn
        self._pages = pages
    
    @property
    def author(self) -> str:
        """Get book author."""
        return self._author
    
    @property
    def isbn(self) -> str:
        """Get book ISBN."""
        return self._isbn
    
    @property
    def pages(self) -> int:
        """Get number of pages."""
        return self._pages
    
    def get_category(self) -> str:
        """Get product category."""
        return "Books"
    
    def get_shipping_weight(self) -> float:
        """Calculate shipping weight based on pages."""
        return max(0.5, self._pages * 0.005)  # Minimum 0.5 lbs
    
    def __str__(self) -> str:
        """String representation for books."""
        return f'"{self._name}" by {self._author} - {self._price}'


class Electronics(Product):
    """
    Electronics product class.
    
    Demonstrates: Inheritance, Method overriding
    """
    
    def __init__(self, name: str, brand: str, model: str, price: Money, 
                 weight: float, warranty_months: int = 12):
        """Initialize electronics."""
        super().__init__(name, price, f"{brand} {model}")
        self._brand = brand
        self._model = model
        self._weight = weight
        self._warranty_months = warranty_months
    
    @property
    def brand(self) -> str:
        """Get brand."""
        return self._brand
    
    @property
    def model(self) -> str:
        """Get model."""
        return self._model
    
    @property
    def warranty_months(self) -> int:
        """Get warranty period."""
        return self._warranty_months
    
    def get_category(self) -> str:
        """Get product category."""
        return "Electronics"
    
    def get_shipping_weight(self) -> float:
        """Get actual shipping weight."""
        return self._weight
    
    def extend_warranty(self, additional_months: int):
        """Extend warranty period."""
        self._warranty_months += additional_months


class Clothing(Product):
    """
    Clothing product class.
    
    Demonstrates: Inheritance, Enumeration handling
    """
    
    SIZES = ["XS", "S", "M", "L", "XL", "XXL"]
    
    def __init__(self, name: str, brand: str, size: str, color: str, 
                 price: Money, material: str):
        """Initialize clothing."""
        if size not in self.SIZES:
            raise ValueError(f"Size must be one of: {self.SIZES}")
        
        super().__init__(name, price, f"{brand} {color} {material}")
        self._brand = brand
        self._size = size
        self._color = color
        self._material = material
    
    @property
    def size(self) -> str:
        """Get clothing size."""
        return self._size
    
    @property
    def color(self) -> str:
        """Get color."""
        return self._color
    
    def get_category(self) -> str:
        """Get product category."""
        return "Clothing"
    
    def get_shipping_weight(self) -> float:
        """Estimate shipping weight for clothing."""
        return 0.8  # Standard clothing weight


# USER MANAGEMENT WITH ENCAPSULATION

class User:
    """
    User class with proper encapsulation.
    
    Demonstrates: Encapsulation, Property decorators, Password hashing
    """
    
    def __init__(self, username: str, email: str, password: str):
        """Initialize user."""
        self._user_id = str(uuid.uuid4())
        self._username = username
        self._email = email
        self._password_hash = self._hash_password(password)
        self._addresses = []
        self._created_at = datetime.now()
        self._is_active = True
    
    @property
    def user_id(self) -> str:
        """Get user ID."""
        return self._user_id
    
    @property
    def username(self) -> str:
        """Get username."""
        return self._username
    
    @property
    def email(self) -> str:
        """Get email."""
        return self._email
    
    @email.setter
    def email(self, new_email: str):
        """Set new email with validation."""
        if "@" not in new_email or "." not in new_email.split("@")[1]:
            raise ValueError("Invalid email format")
        self._email = new_email
    
    @property
    def addresses(self) -> List[Address]:
        """Get user addresses."""
        return self._addresses.copy()  # Return copy to prevent modification
    
    @property
    def is_active(self) -> bool:
        """Check if user is active."""
        return self._is_active
    
    def _hash_password(self, password: str) -> str:
        """Hash password securely."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password: str) -> bool:
        """Verify password."""
        return self._hash_password(password) == self._password_hash
    
    def change_password(self, old_password: str, new_password: str) -> bool:
        """Change password with verification."""
        if not self.verify_password(old_password):
            return False
        
        if len(new_password) < 8:
            raise ValueError("Password must be at least 8 characters")
        
        self._password_hash = self._hash_password(new_password)
        return True
    
    def add_address(self, address: Address):
        """Add address to user."""
        if address not in self._addresses:
            self._addresses.append(address)
    
    def remove_address(self, address: Address):
        """Remove address from user."""
        if address in self._addresses:
            self._addresses.remove(address)
    
    def deactivate(self):
        """Deactivate user account."""
        self._is_active = False
    
    def activate(self):
        """Activate user account."""
        self._is_active = True
    
    def __str__(self) -> str:
        """String representation."""
        return f"User: {self._username} ({self._email})"


# PAYMENT PROCESSING WITH POLYMORPHISM

class CreditCard(Payable):
    """
    Credit card payment processor.
    
    Demonstrates: Inheritance from abstract class, Polymorphism
    """
    
    def __init__(self, card_number: str, cardholder_name: str, 
                 expiry_month: int, expiry_year: int, cvv: str):
        """Initialize credit card."""
        self._card_number = self._mask_card_number(card_number)
        self._cardholder_name = cardholder_name
        self._expiry_month = expiry_month
        self._expiry_year = expiry_year
        self._cvv = cvv  # In real app, this would be handled more securely
    
    def _mask_card_number(self, card_number: str) -> str:
        """Mask card number for security."""
        return "**** **** **** " + card_number[-4:]
    
    def validate_payment_info(self) -> bool:
        """Validate credit card information."""
        current_year = datetime.now().year
        current_month = datetime.now().month
        
        # Check expiry date
        if self._expiry_year < current_year:
            return False
        if self._expiry_year == current_year and self._expiry_month < current_month:
            return False
        
        # Check CVV
        if len(self._cvv) not in [3, 4]:
            return False
        
        return True
    
    def process_payment(self, amount: float) -> Dict:
        """Process credit card payment."""
        if not self.validate_payment_info():
            return {
                "success": False,
                "error": "Invalid payment information",
                "transaction_id": None
            }
        
        # Simulate payment processing
        transaction_id = str(uuid.uuid4())
        
        return {
            "success": True,
            "transaction_id": transaction_id,
            "amount": amount,
            "method": "Credit Card",
            "card": self._card_number
        }


class PayPal(Payable):
    """
    PayPal payment processor.
    
    Demonstrates: Polymorphism, Different implementation of same interface
    """
    
    def __init__(self, email: str, password: str):
        """Initialize PayPal account."""
        self._email = email
        self._password_hash = hashlib.sha256(password.encode()).hexdigest()
        self._is_verified = True  # Assume account is verified
    
    def validate_payment_info(self) -> bool:
        """Validate PayPal account."""
        return "@" in self._email and self._is_verified
    
    def process_payment(self, amount: float) -> Dict:
        """Process PayPal payment."""
        if not self.validate_payment_info():
            return {
                "success": False,
                "error": "Invalid PayPal account",
                "transaction_id": None
            }
        
        # Simulate PayPal processing
        transaction_id = f"PP_{str(uuid.uuid4())[:8]}"
        
        return {
            "success": True,
            "transaction_id": transaction_id,
            "amount": amount,
            "method": "PayPal",
            "account": self._email
        }


# SHOPPING CART WITH CONTAINER BEHAVIOR

class CartItem:
    """
    Shopping cart item.
    
    Demonstrates: Composition, Special methods
    """
    
    def __init__(self, product: Product, quantity: int = 1):
        """Initialize cart item."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if not product.in_stock:
            raise ValueError("Product is out of stock")
        
        self.product = product
        self.quantity = quantity
    
    @property
    def total_price(self) -> Money:
        """Calculate total price for this item."""
        return self.product.price * self.quantity
    
    def __str__(self) -> str:
        """String representation."""
        return f"{self.product.name} x{self.quantity} = {self.total_price}"
    
    def __eq__(self, other) -> bool:
        """Check item equality."""
        if not isinstance(other, CartItem):
            return False
        return self.product == other.product


class ShoppingCart:
    """
    Shopping cart with container behavior.
    
    Demonstrates: Container special methods, Composition, Aggregation
    """
    
    def __init__(self, user: User):
        """Initialize shopping cart."""
        self._user = user
        self._items: List[CartItem] = []
        self._created_at = datetime.now()
    
    @property
    def user(self) -> User:
        """Get cart owner."""
        return self._user
    
    @property
    def item_count(self) -> int:
        """Get total number of items."""
        return sum(item.quantity for item in self._items)
    
    @property
    def total_amount(self) -> Money:
        """Calculate total cart amount."""
        if not self._items:
            return Money(0)
        
        total = self._items[0].total_price
        for item in self._items[1:]:
            total = total + item.total_price
        
        return total
    
    def __len__(self) -> int:
        """Get number of unique items."""
        return len(self._items)
    
    def __getitem__(self, index: int) -> CartItem:
        """Get item by index."""
        return self._items[index]
    
    def __contains__(self, product: Product) -> bool:
        """Check if product is in cart."""
        return any(item.product == product for item in self._items)
    
    def __iter__(self):
        """Make cart iterable."""
        return iter(self._items)
    
    def add_item(self, product: Product, quantity: int = 1):
        """Add item to cart."""
        if not product.in_stock:
            raise ValueError(f"{product.name} is out of stock")
        
        # Check if product already in cart
        for item in self._items:
            if item.product == product:
                item.quantity += quantity
                return
        
        # Add new item
        self._items.append(CartItem(product, quantity))
    
    def remove_item(self, product: Product):
        """Remove item from cart."""
        self._items = [item for item in self._items if item.product != product]
    
    def update_quantity(self, product: Product, new_quantity: int):
        """Update item quantity."""
        if new_quantity <= 0:
            self.remove_item(product)
            return
        
        for item in self._items:
            if item.product == product:
                item.quantity = new_quantity
                return
        
        raise ValueError("Product not in cart")
    
    def clear(self):
        """Clear all items from cart."""
        self._items.clear()
    
    def apply_discount_to_item(self, product: Product, percentage: float):
        """Apply discount to specific item."""
        for item in self._items:
            if item.product == product:
                if isinstance(item.product, Discountable):
                    discounted_price = item.product.apply_discount(percentage)
                    # Create new discounted price
                    item.product._price = Money(discounted_price, item.product.price.currency)
                return
        
        raise ValueError("Product not in cart")
    
    def __str__(self) -> str:
        """String representation."""
        if not self._items:
            return "Empty shopping cart"
        
        lines = [f"Shopping Cart for {self._user.username}:"]
        for item in self._items:
            lines.append(f"  {item}")
        lines.append(f"Total: {self.total_amount}")
        lines.append(f"Items: {self.item_count}")
        
        return "\n".join(lines)


# ORDER PROCESSING SYSTEM

class Order:
    """
    Order class combining all concepts.
    
    Demonstrates: Composition, Encapsulation, Integration of all concepts
    """
    
    def __init__(self, user: User, cart: ShoppingCart, shipping_address: Address):
        """Initialize order."""
        if not cart._items:
            raise ValueError("Cannot create order with empty cart")
        
        self._order_id = str(uuid.uuid4())
        self._user = user
        self._items = [CartItem(item.product, item.quantity) for item in cart._items]
        self._shipping_address = shipping_address
        self._created_at = datetime.now()
        self._status = "Pending"
        self._payment_method: Optional[Payable] = None
        self._transaction_id: Optional[str] = None
    
    @property
    def order_id(self) -> str:
        """Get order ID."""
        return self._order_id
    
    @property
    def status(self) -> str:
        """Get order status."""
        return self._status
    
    @property
    def total_amount(self) -> Money:
        """Calculate total order amount."""
        subtotal = sum((item.total_price for item in self._items), Money(0))
        shipping = self._calculate_shipping()
        tax = self._calculate_tax(subtotal)
        
        return subtotal + shipping + tax
    
    def _calculate_shipping(self) -> Money:
        """Calculate shipping cost."""
        total_weight = sum(item.product.get_shipping_weight() * item.quantity 
                          for item in self._items)
        
        # Simple shipping calculation
        if total_weight <= 1:
            shipping_cost = 5.99
        elif total_weight <= 5:
            shipping_cost = 9.99
        else:
            shipping_cost = 15.99
        
        return Money(shipping_cost)
    
    def _calculate_tax(self, subtotal: Money) -> Money:
        """Calculate tax (8.5%)."""
        tax_rate = 0.085
        return Money(subtotal.amount * tax_rate)
    
    def set_payment_method(self, payment_method: Payable):
        """Set payment method."""
        self._payment_method = payment_method
    
    def process_payment(self) -> bool:
        """Process order payment."""
        if not self._payment_method:
            raise ValueError("Payment method not set")
        
        result = self._payment_method.process_payment(self.total_amount.amount)
        
        if result["success"]:
            self._transaction_id = result["transaction_id"]
            self._status = "Paid"
            return True
        else:
            self._status = "Payment Failed"
            return False
    
    def ship_order(self):
        """Ship the order."""
        if self._status != "Paid":
            raise ValueError("Cannot ship unpaid order")
        
        self._status = "Shipped"
    
    def deliver_order(self):
        """Mark order as delivered."""
        if self._status != "Shipped":
            raise ValueError("Cannot deliver unshipped order")
        
        self._status = "Delivered"
    
    def cancel_order(self):
        """Cancel the order."""
        if self._status in ["Shipped", "Delivered"]:
            raise ValueError("Cannot cancel shipped or delivered order")
        
        self._status = "Cancelled"
    
    def __str__(self) -> str:
        """String representation."""
        lines = [
            f"Order {self._order_id[:8]}... - {self._status}",
            f"Customer: {self._user.username}",
            f"Items:"
        ]
        
        for item in self._items:
            lines.append(f"  {item}")
        
        lines.extend([
            f"Subtotal: {sum((item.total_price for item in self._items), Money(0))}",
            f"Shipping: {self._calculate_shipping()}",
            f"Tax: {self._calculate_tax(sum((item.total_price for item in self._items), Money(0)))}",
            f"Total: {self.total_amount}",
            f"Ship to: {self._shipping_address}"
        ])
        
        return "\n".join(lines)


# DEMONSTRATION FUNCTION

def demonstrate_ecommerce_system():
    """
    Comprehensive demonstration of the e-commerce system.
    
    This function shows all OOP concepts working together.
    """
    print("=" * 80)
    print("COMPREHENSIVE OOP PROJECT: E-COMMERCE SYSTEM")
    print("=" * 80)
    
    # 1. Create Products (Inheritance, Polymorphism)
    print("\n1. CREATING PRODUCTS (Inheritance & Polymorphism):")
    print("-" * 55)
    
    book = Book("Python OOP Guide", "John Doe", "978-1234567890", Money(29.99), 350)
    laptop = Electronics("Gaming Laptop", "TechBrand", "GX-3000", Money(1299.99), 5.5, 24)
    shirt = Clothing("Cotton T-Shirt", "FashionCo", "L", "Blue", Money(19.99), "Cotton")
    
    products = [book, laptop, shirt]
    
    for product in products:
        print(f"{product}")
        print(f"  Category: {product.get_category()}")
        print(f"  Shipping Weight: {product.get_shipping_weight()} lbs")
        print()
    
    # 2. Create User (Encapsulation, Property decorators)
    print("2. USER MANAGEMENT (Encapsulation & Properties):")
    print("-" * 50)
    
    user = User("john_smith", "john@example.com", "securepass123")
    address = Address("123 Main St", "Anytown", "CA", "12345")
    user.add_address(address)
    
    print(f"Created user: {user}")
    print(f"User ID: {user.user_id}")
    print(f"Addresses: {len(user.addresses)}")
    
    # Test password change
    success = user.change_password("securepass123", "newsecurepass456")
    print(f"Password changed: {success}")
    
    # 3. Shopping Cart (Container behavior, Special methods)
    print("\n3. SHOPPING CART (Container Behavior & Special Methods):")
    print("-" * 60)
    
    cart = ShoppingCart(user)
    cart.add_item(book, 2)
    cart.add_item(laptop, 1)
    cart.add_item(shirt, 3)
    
    print(f"Cart length: {len(cart)}")
    print(f"Total items: {cart.item_count}")
    print(f"Book in cart: {book in cart}")
    
    print("\nCart contents:")
    for item in cart:
        print(f"  {item}")
    
    print(f"\nCart total: {cart.total_amount}")
    
    # 4. Apply Discounts (Duck typing, Protocol)
    print("\n4. DISCOUNT SYSTEM (Duck Typing & Protocols):")
    print("-" * 50)
    
    print("Applying 10% discount to book...")
    cart.apply_discount_to_item(book, 10.0)
    
    print(f"New cart total: {cart.total_amount}")
    
    # 5. Payment Processing (Polymorphism, Abstract classes)
    print("\n5. PAYMENT PROCESSING (Polymorphism & Abstract Classes):")
    print("-" * 65)
    
    # Create different payment methods
    credit_card = CreditCard("4532123456789012", "John Smith", 12, 2025, "123")
    paypal = PayPal("john@example.com", "paypalpass")
    
    payment_methods = [credit_card, paypal]
    
    for payment in payment_methods:
        print(f"Payment method valid: {payment.validate_payment_info()}")
        result = payment.process_payment(100.00)
        print(f"Payment result: {result['success']} - {result.get('method', 'Unknown')}")
    
    # 6. Order Processing (Composition, Integration)
    print("\n6. ORDER PROCESSING (Composition & Integration):")
    print("-" * 50)
    
    # Create order
    order = Order(user, cart, address)
    order.set_payment_method(credit_card)
    
    print("Order created:")
    print(order)
    
    # Process payment
    print(f"\nProcessing payment...")
    payment_success = order.process_payment()
    print(f"Payment successful: {payment_success}")
    print(f"Order status: {order.status}")
    
    # Ship order
    if payment_success:
        order.ship_order()
        print(f"Order shipped. Status: {order.status}")
        
        order.deliver_order()
        print(f"Order delivered. Status: {order.status}")
    
    # 7. Money Operations (Operator overloading)
    print("\n7. MONEY OPERATIONS (Operator Overloading):")
    print("-" * 50)
    
    price1 = Money(25.99)
    price2 = Money(15.50)
    
    print(f"Price 1: {price1}")
    print(f"Price 2: {price2}")
    print(f"Addition: {price1 + price2}")
    print(f"Subtraction: {price1 - price2}")
    print(f"Multiplication: {price1 * 2}")
    print(f"Comparison: {price1 > price2}")
    
    # 8. Error Handling
    print("\n8. ERROR HANDLING:")
    print("-" * 20)
    
    try:
        # Try to add out of stock product
        out_of_stock_product = Book("Rare Book", "Unknown", "123", Money(99.99), 100)
        out_of_stock_product.in_stock = False
        cart.add_item(out_of_stock_product, 1)
    except ValueError as e:
        print(f"Error adding out of stock product: {e}")
    
    try:
        # Try to create negative money
        negative_money = Money(-10.00)
    except ValueError as e:
        print(f"Error creating negative money: {e}")
    
    # 9. Summary of OOP Concepts Used
    print("\n9. OOP CONCEPTS DEMONSTRATED:")
    print("-" * 35)
    
    concepts = [
        "✓ Classes and Objects - Product, User, Order, etc.",
        "✓ Inheritance - Product -> Book/Electronics/Clothing",
        "✓ Multiple Inheritance - Not used (favor composition)",
        "✓ Encapsulation - Private attributes with properties",
        "✓ Polymorphism - Different payment methods, product types",
        "✓ Abstraction - Abstract Product and Payable classes",
        "✓ Special Methods - Money class operator overloading",
        "✓ Composition - Order contains User, Cart, Address",
        "✓ Aggregation - Cart contains Products (products exist independently)",
        "✓ Duck Typing - Discountable protocol",
        "✓ Error Handling - Validation and exceptions",
        "✓ Property Decorators - User email validation",
        "✓ Container Behavior - ShoppingCart with __len__, __iter__, etc."
    ]
    
    for concept in concepts:
        print(f"  {concept}")
    
    print(f"\n🎉 Complete E-Commerce System Demonstration Complete!")
    print("This project showcases all major OOP concepts working together")
    print("in a real-world application scenario.")


if __name__ == "__main__":
    """
    Main execution block.
    """
    demonstrate_ecommerce_system()


"""
COMPREHENSIVE PROJECT SUMMARY:

This e-commerce system demonstrates ALL major OOP concepts:

1. CLASSES & OBJECTS:
   - User, Product, Order, ShoppingCart, Money, Address classes
   - Object creation and interaction

2. INHERITANCE:
   - Product -> Book, Electronics, Clothing
   - Payable -> CreditCard, PayPal
   - Method overriding in subclasses

3. ENCAPSULATION:
   - Private attributes with underscore prefix
   - Property decorators for controlled access
   - Data validation in setters

4. POLYMORPHISM:
   - Different product types with same interface
   - Different payment methods with same interface
   - Method overriding for specialized behavior

5. ABSTRACTION:
   - Abstract Product class with abstract methods
   - Abstract Payable class for payment processing
   - Discountable protocol for duck typing

6. SPECIAL METHODS:
   - Money class with full operator overloading
   - ShoppingCart with container behavior
   - String representations for all classes

7. COMPOSITION vs INHERITANCE:
   - Order HAS-A User, Cart, Address (composition)
   - Cart HAS-A Products (aggregation)
   - Favored composition over deep inheritance

8. ADVANCED CONCEPTS:
   - Protocol-based interfaces
   - Property decorators
   - Context management (could be added)
   - Error handling and validation

REAL-WORLD APPLICABILITY:
- Scalable architecture
- Maintainable code structure
- Extensible design
- Proper error handling
- Security considerations (password hashing)
- Business logic separation

This project serves as a complete reference for applying OOP principles
in a practical, real-world application.
"""


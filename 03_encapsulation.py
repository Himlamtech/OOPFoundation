"""
Object-Oriented Programming Foundation - Lesson 3: Encapsulation

This lesson covers encapsulation concepts in OOP:
- What is encapsulation?
- Public, protected, and private attributes/methods
- Name mangling in Python
- Property decorators (@property, @setter, @deleter)
- Getters and setters
- Data validation and access control
- Information hiding principles

Author: AI Senior Engineer
"""


class BankAccount:
    """
    A BankAccount class demonstrating encapsulation principles.
    
    This class shows:
    - Private attributes (information hiding)
    - Public interface methods
    - Data validation
    - Controlled access to sensitive data
    """
    
    # Class variable for generating account numbers
    _next_account_number = 1000
    
    def __init__(self, owner_name, initial_balance=0):
        """
        Initialize a BankAccount object.
        
        Args:
            owner_name (str): Name of the account owner
            initial_balance (float, optional): Starting balance. Defaults to 0
        
        Raises:
            ValueError: If initial_balance is negative
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        # Public attributes (accessible from outside)
        self.owner_name = owner_name
        self.account_creation_date = "2024-01-01"  # Simplified for demo
        
        # Protected attributes (convention: single underscore prefix)
        # Should not be accessed directly from outside, but can be in subclasses
        self._account_number = BankAccount._next_account_number
        BankAccount._next_account_number += 1
        
        # Private attributes (double underscore prefix - name mangling)
        # Cannot be accessed directly from outside the class
        self.__balance = initial_balance
        self.__pin = None
        self.__is_locked = False
        self.__transaction_history = []
    
    def set_pin(self, new_pin):
        """
        Set a PIN for the account (public method for controlled access).
        
        Args:
            new_pin (str): 4-digit PIN
        
        Returns:
            str: Success/error message
        """
        if self.__is_locked:
            return "Account is locked. Cannot change PIN."
        
        if not isinstance(new_pin, str) or len(new_pin) != 4 or not new_pin.isdigit():
            return "PIN must be a 4-digit string."
        
        self.__pin = new_pin
        self.__add_transaction("PIN_SET", 0, "PIN has been set")
        return "PIN set successfully."
    
    def verify_pin(self, entered_pin):
        """
        Verify the entered PIN (private method for internal use).
        
        Args:
            entered_pin (str): PIN to verify
        
        Returns:
            bool: True if PIN is correct, False otherwise
        """
        if self.__pin is None:
            return False
        return self.__pin == entered_pin
    
    def deposit(self, amount, pin=None):
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
            pin (str, optional): PIN for verification
        
        Returns:
            str: Transaction result message
        """
        if self.__is_locked:
            return "Account is locked. Please contact customer service."
        
        if amount <= 0:
            return "Deposit amount must be positive."
        
        # PIN verification for large deposits
        if amount > 10000 and not self.verify_pin(pin):
            return "PIN required for deposits over $10,000."
        
        self.__balance += amount
        self.__add_transaction("DEPOSIT", amount, f"Deposited ${amount:.2f}")
        return f"Successfully deposited ${amount:.2f}. New balance: ${self.__balance:.2f}"
    
    def withdraw(self, amount, pin):
        """
        Withdraw money from the account.
        
        Args:
            amount (float): Amount to withdraw
            pin (str): PIN for verification
        
        Returns:
            str: Transaction result message
        """
        if self.__is_locked:
            return "Account is locked. Please contact customer service."
        
        if not self.verify_pin(pin):
            return "Invalid PIN. Withdrawal denied."
        
        if amount <= 0:
            return "Withdrawal amount must be positive."
        
        if amount > self.__balance:
            return f"Insufficient funds. Available balance: ${self.__balance:.2f}"
        
        self.__balance -= amount
        self.__add_transaction("WITHDRAWAL", -amount, f"Withdrew ${amount:.2f}")
        return f"Successfully withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}"
    
    def get_balance(self, pin):
        """
        Get account balance (requires PIN).
        
        Args:
            pin (str): PIN for verification
        
        Returns:
            str: Balance information or error message
        """
        if self.__is_locked:
            return "Account is locked. Please contact customer service."
        
        if not self.verify_pin(pin):
            return "Invalid PIN. Access denied."
        
        return f"Current balance: ${self.__balance:.2f}"
    
    def lock_account(self):
        """
        Lock the account (emergency measure).
        
        Returns:
            str: Lock status message
        """
        self.__is_locked = True
        self.__add_transaction("LOCK", 0, "Account has been locked")
        return "Account has been locked for security."
    
    def __add_transaction(self, transaction_type, amount, description):
        """
        Add a transaction to the history (private method).
        
        Args:
            transaction_type (str): Type of transaction
            amount (float): Transaction amount
            description (str): Transaction description
        
        Note:
            This is a private method (double underscore prefix)
            Cannot be called directly from outside the class
        """
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "description": description,
            "timestamp": "2024-01-01 12:00:00"  # Simplified for demo
        }
        self.__transaction_history.append(transaction)
    
    def get_transaction_history(self, pin):
        """
        Get transaction history (requires PIN).
        
        Args:
            pin (str): PIN for verification
        
        Returns:
            str: Transaction history or error message
        """
        if self.__is_locked:
            return "Account is locked. Please contact customer service."
        
        if not self.verify_pin(pin):
            return "Invalid PIN. Access denied."
        
        if not self.__transaction_history:
            return "No transactions found."
        
        history = "Transaction History:\n"
        for i, transaction in enumerate(self.__transaction_history[-10:], 1):  # Last 10 transactions
            history += (f"{i}. {transaction['timestamp']} - {transaction['type']}: "
                       f"{transaction['description']}\n")
        
        return history
    
    # Protected method (single underscore - convention only)
    def _get_account_number(self):
        """
        Get account number (protected method).
        
        Returns:
            int: Account number
        
        Note:
            Protected method - should only be used by subclasses or internal methods
        """
        return self._account_number
    
    def get_public_info(self):
        """
        Get public account information (no PIN required).
        
        Returns:
            str: Public account information
        """
        return (f"Account Owner: {self.owner_name}\n"
                f"Account Number: {self._account_number}\n"
                f"Account Created: {self.account_creation_date}\n"
                f"Account Status: {'Locked' if self.__is_locked else 'Active'}")


class SecureBankAccount(BankAccount):
    """
    Enhanced bank account with additional security features.
    
    This class demonstrates:
    - Inheritance with encapsulation
    - Accessing protected members from subclass
    - Adding new private attributes
    - Overriding methods while maintaining encapsulation
    """
    
    def __init__(self, owner_name, initial_balance=0, security_question=None, security_answer=None):
        """
        Initialize a SecureBankAccount object.
        
        Args:
            owner_name (str): Name of the account owner
            initial_balance (float, optional): Starting balance. Defaults to 0
            security_question (str, optional): Security question
            security_answer (str, optional): Security answer
        """
        super().__init__(owner_name, initial_balance)
        
        # Additional private attributes for enhanced security
        self.__security_question = security_question
        self.__security_answer = security_answer.lower() if security_answer else None
        self.__failed_attempts = 0
        self.__max_attempts = 3
    
    def set_security_question(self, question, answer, pin):
        """
        Set security question and answer.
        
        Args:
            question (str): Security question
            answer (str): Security answer
            pin (str): PIN for verification
        
        Returns:
            str: Success/error message
        """
        if not self.verify_pin(pin):
            return "Invalid PIN. Cannot set security question."
        
        if not question or not answer:
            return "Both question and answer are required."
        
        self.__security_question = question
        self.__security_answer = answer.lower()
        return "Security question set successfully."
    
    def reset_pin_with_security(self, new_pin, security_answer):
        """
        Reset PIN using security question (when PIN is forgotten).
        
        Args:
            new_pin (str): New 4-digit PIN
            security_answer (str): Answer to security question
        
        Returns:
            str: Reset result message
        """
        if self.__failed_attempts >= self.__max_attempts:
            self.lock_account()
            return "Too many failed attempts. Account locked."
        
        if not self.__security_question or not self.__security_answer:
            return "No security question set for this account."
        
        if security_answer.lower() != self.__security_answer:
            self.__failed_attempts += 1
            remaining = self.__max_attempts - self.__failed_attempts
            return f"Incorrect security answer. {remaining} attempts remaining."
        
        # Reset failed attempts on successful verification
        self.__failed_attempts = 0
        
        # Validate new PIN
        if not isinstance(new_pin, str) or len(new_pin) != 4 or not new_pin.isdigit():
            return "PIN must be a 4-digit string."
        
        # Access the private PIN attribute from parent class (through public method)
        result = self.set_pin(new_pin)
        if "successfully" in result:
            return "PIN reset successfully using security question."
        return result
    
    def get_security_question(self):
        """
        Get the security question (without revealing answer).
        
        Returns:
            str: Security question or message if not set
        """
        if self.__security_question:
            return f"Security Question: {self.__security_question}"
        return "No security question set for this account."


class PropertyDemo:
    """
    Class demonstrating Python property decorators for encapsulation.
    
    This class shows:
    - @property decorator for getters
    - @setter decorator for setters
    - @deleter decorator for deleters
    - Data validation in setters
    - Computed properties
    """
    
    def __init__(self, name, age):
        """
        Initialize PropertyDemo object.
        
        Args:
            name (str): Person's name
            age (int): Person's age
        """
        self._name = name  # Protected attribute
        self._age = age    # Protected attribute
        self._email = None
    
    @property
    def name(self):
        """
        Getter for name property.
        
        Returns:
            str: Person's name
        """
        return self._name
    
    @name.setter
    def name(self, value):
        """
        Setter for name property with validation.
        
        Args:
            value (str): New name value
        
        Raises:
            ValueError: If name is empty or not a string
        """
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip().title()  # Capitalize properly
    
    @property
    def age(self):
        """
        Getter for age property.
        
        Returns:
            int: Person's age
        """
        return self._age
    
    @age.setter
    def age(self, value):
        """
        Setter for age property with validation.
        
        Args:
            value (int): New age value
        
        Raises:
            ValueError: If age is not valid
        """
        if not isinstance(value, int):
            raise ValueError("Age must be an integer")
        if value < 0:
            raise ValueError("Age cannot be negative")
        if value > 150:
            raise ValueError("Age seems unrealistic")
        self._age = value
    
    @property
    def email(self):
        """
        Getter for email property.
        
        Returns:
            str: Person's email or generated email if not set
        """
        if self._email:
            return self._email
        # Generate email if not set
        return f"{self._name.lower().replace(' ', '.')}@example.com"
    
    @email.setter
    def email(self, value):
        """
        Setter for email property with validation.
        
        Args:
            value (str): New email value
        
        Raises:
            ValueError: If email format is invalid
        """
        if value is None:
            self._email = None
            return
        
        if not isinstance(value, str):
            raise ValueError("Email must be a string")
        
        # Simple email validation
        if "@" not in value or "." not in value.split("@")[1]:
            raise ValueError("Invalid email format")
        
        self._email = value.lower()
    
    @email.deleter
    def email(self):
        """
        Deleter for email property.
        """
        self._email = None
        print("Email has been deleted")
    
    @property
    def is_adult(self):
        """
        Computed property to check if person is adult.
        
        Returns:
            bool: True if age >= 18, False otherwise
        """
        return self._age >= 18
    
    @property
    def description(self):
        """
        Computed property for description.
        
        Returns:
            str: Formatted description
        """
        adult_status = "adult" if self.is_adult else "minor"
        return f"{self.name} is a {self._age}-year-old {adult_status} with email {self.email}"


def demonstrate_encapsulation():
    """
    Demonstration function showing encapsulation concepts.
    
    This function demonstrates:
    - Private attribute access control
    - Public interface methods
    - Protected attribute conventions
    - Property decorators
    - Data validation
    - Information hiding
    """
    print("=" * 70)
    print("OBJECT-ORIENTED PROGRAMMING - LESSON 3: ENCAPSULATION")
    print("=" * 70)
    
    # Basic encapsulation with BankAccount
    print("\n1. BASIC ENCAPSULATION - BANK ACCOUNT:")
    print("-" * 45)
    
    # Create a bank account
    account = BankAccount("Alice Johnson", 1000)
    
    print("Public information (no PIN required):")
    print(account.get_public_info())
    
    print("\nSetting PIN:")
    print(account.set_pin("1234"))
    
    print("\nTrying to access balance without PIN:")
    print(account.get_balance("wrong_pin"))
    
    print("\nAccessing balance with correct PIN:")
    print(account.get_balance("1234"))
    
    print("\nMaking transactions:")
    print(account.deposit(500))
    print(account.withdraw(200, "1234"))
    print(account.get_balance("1234"))
    
    # Demonstrate private attribute protection
    print("\n2. PRIVATE ATTRIBUTE PROTECTION:")
    print("-" * 40)
    
    print("Trying to access private attributes directly:")
    try:
        # This will raise an AttributeError
        print("Balance:", account.__balance)
    except AttributeError as e:
        print(f"Error: {e}")
    
    print("Accessing protected attribute (by convention):")
    print(f"Account number: {account._get_account_number()}")
    
    # Name mangling demonstration
    print("\nName mangling with private attributes:")
    print("Private attributes are mangled to: _ClassName__attributename")
    print("Available attributes:", [attr for attr in dir(account) if 'balance' in attr.lower()])
    
    # Enhanced security example
    print("\n3. ENHANCED SECURITY ACCOUNT:")
    print("-" * 35)
    
    secure_account = SecureBankAccount("Bob Smith", 2000, 
                                     "What is your pet's name?", "Fluffy")
    
    print(secure_account.get_public_info())
    print(secure_account.set_pin("5678"))
    print(secure_account.get_security_question())
    
    print("\nForgotten PIN scenario:")
    print("Trying to reset PIN with wrong security answer:")
    print(secure_account.reset_pin_with_security("9999", "wrong_answer"))
    
    print("Resetting PIN with correct security answer:")
    print(secure_account.reset_pin_with_security("9999", "fluffy"))
    
    # Property decorators demonstration
    print("\n4. PROPERTY DECORATORS:")
    print("-" * 30)
    
    person = PropertyDemo("john doe", 25)
    
    print(f"Name (auto-capitalized): {person.name}")
    print(f"Age: {person.age}")
    print(f"Email (auto-generated): {person.email}")
    print(f"Is adult: {person.is_adult}")
    print(f"Description: {person.description}")
    
    print("\nSetting custom email:")
    person.email = "john.doe@company.com"
    print(f"Custom email: {person.email}")
    
    print("\nValidation in action:")
    try:
        person.age = -5  # Should raise ValueError
    except ValueError as e:
        print(f"Age validation error: {e}")
    
    try:
        person.email = "invalid_email"  # Should raise ValueError
    except ValueError as e:
        print(f"Email validation error: {e}")
    
    print("\nDeleting email:")
    del person.email
    print(f"Email after deletion: {person.email}")
    
    # Demonstrate access levels
    print("\n5. ACCESS LEVELS SUMMARY:")
    print("-" * 32)
    
    print("PUBLIC (no prefix): Accessible from anywhere")
    print("  Example: account.owner_name")
    
    print("\nPROTECTED (single _): Should not be accessed outside class/subclasses")
    print("  Example: account._account_number (convention only)")
    
    print("\nPRIVATE (double __): Cannot be accessed directly outside class")
    print("  Example: account.__balance (name mangling)")
    
    print("\nACCESS THROUGH PROPERTIES: Controlled access with validation")
    print("  Example: person.age = 30 (calls setter with validation)")


if __name__ == "__main__":
    """
    Main execution block.
    """
    demonstrate_encapsulation()


"""
KEY CONCEPTS LEARNED IN THIS LESSON:

1. ENCAPSULATION: Bundling data and methods together while controlling access
   - Hide internal implementation details
   - Provide public interface for interaction
   - Protect data integrity through controlled access

2. ACCESS LEVELS IN PYTHON:
   - PUBLIC (no prefix): Accessible from anywhere
   - PROTECTED (single _): Convention - should not access outside class/subclasses  
   - PRIVATE (double __): Name mangling - cannot access directly outside class

3. NAME MANGLING: Python's mechanism for private attributes
   - __attribute becomes _ClassName__attribute
   - Prevents accidental access from outside class
   - Not true privacy, but strong discouragement

4. PROPERTY DECORATORS: Pythonic way to create getters/setters
   - @property: Creates getter method
   - @property_name.setter: Creates setter method with validation
   - @property_name.deleter: Creates deleter method
   - Allows method-like behavior with attribute-like syntax

5. DATA VALIDATION: Ensuring data integrity
   - Validate inputs in setters
   - Raise appropriate exceptions for invalid data
   - Maintain object state consistency

6. INFORMATION HIDING: Principle of keeping internal details private
   - Only expose what's necessary through public interface
   - Hide complex implementation details
   - Allow internal changes without affecting external code

7. CONTROLLED ACCESS: Managing how data is accessed and modified
   - Require authentication (PIN) for sensitive operations
   - Log all transactions for audit trail
   - Implement business rules in access methods

8. COMPUTED PROPERTIES: Properties calculated from other attributes
   - Read-only properties that derive values
   - Always up-to-date based on current state
   - Examples: is_adult, full_name, etc.

NEXT LESSON: We'll explore polymorphism and method overriding in detail!
"""


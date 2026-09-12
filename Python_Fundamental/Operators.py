# Basic Operators

x = 10
y = 3

print(x + y)   # Addition: 13
print(x - y)   # Subtraction: 7
print(x * y)   # Multiplication: 30
print(x / y)   # Division: 3.3333...

print(x // y)  # Floor Division (drops the decimal): 3
print(x % y)   # Modulo (shows only the remainder): 1
print(x ** y)  # Exponent (10 to the power of 3): 1000

#Logical Operators

has_computer = True
has_internet = False

# AND (Both must be True)
print(has_computer and has_internet)  # False (because internet is missing)

# OR (At least one must be True)
print(has_computer or has_internet)   # True (because you have a computer)

# NOT (Inverts the value)
print(not has_computer)               # False


# debug.py

from customer import Customer

try:
    c1 = Customer("Alice")
    print("Valid:", c1.name)
except ValueError as e:
    print("Error:", e)

try:
    c2 = Customer("A very long name indeed")
except ValueError as e:
    print("Too long:", e)

try:
    c3 = Customer(100)
except ValueError as e:
    print("Not a string:", e)
from coffee import Coffee

try:
    c1 = Coffee("Latte")
    print("Valid coffee name:", c1.name)
except ValueError as e:
    print("Error:", e)

try:
    c2 = Coffee("AB")
except ValueError as e:
    print("Too short:", e)

try:
    c3 = Coffee(123)
except ValueError as e:
    print("Not a string:", e)
from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Cappuccino")

# Valid order
o1 = Order(c1, coffee1, 3.5)
print("Order created:", o1.customer.name, "->", o1.coffee.name, "at $", o1.price)

# Invalid price
try:
    o2 = Order(c2, coffee2, 0.5)
except ValueError as e:
    print("Price too low:", e)

# Invalid customer
try:
    o3 = Order("not a customer", coffee1, 4.0)
except ValueError as e:
    print("Wrong customer:", e)

# Invalid coffee
try:
    o4 = Order(c1, "not coffee", 4.0)
except ValueError as e:
    print("Wrong coffee:", e)

from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
latte = Coffee("Latte")
order1 = alice.create_order(latte, 5.0)

print(alice.coffees())  # Should show [latte]
print(latte.customers())  # Should show [alice]

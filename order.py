
from customer import Customer
from coffee import Coffee

class Order:
    all_orders = []  # class-level list to store all orders

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("customer must be an instance of Customer")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise ValueError("coffee must be an instance of Coffee")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and 1.0 <= value <= 10.0:
            self._price = float(value)
        else:
            raise ValueError("price must be a number between 1.0 and 10.0")
        def __repr__(self):
            return f"<Order: {self.customer.name} ordered {self.coffee.name} for ${self.price:.2f}>"

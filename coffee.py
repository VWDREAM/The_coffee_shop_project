from order import Order

class Coffee:
    def __init__(self, name):
        self.name= name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        from order import Order  # avoid circular import issues if needed

        def orders(self):
            return [order for order in Order.all_orders if order.coffee == self]

        def customers(self):
            return list({order.customer for order in self.orders()})
        # coffee.py

    def num_orders(self):
        return len(self.orders())
    # coffee.py

    def average_price(self):
        orders = self.orders()
        if orders:
            total = sum(order.price for order in orders)
            return total / len(orders)
        return 0

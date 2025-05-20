class Customer:
    def _init_(self, name):
        self.name = name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Customer name must be a string between 1 and 15 characters.")
        from order import Order  # avoid circular import issues if needed

        def orders(self):
            return [order for order in Order.all_orders if order.customer == self]

        def coffees(self):
            return list({order.coffee for order in self.orders()})
    # customer.py

        from order import Order  # add this if not already present

        def create_order(self, coffee, price):
          return Order(self, coffee, price)
    # customer.py

class Customer:
    _all_customers = []

    # existing init and methods...

    @classmethod
    def most_aficionado(cls, coffee):
        customer_spending = {}

        for order in coffee.orders():
            customer = order.customer
            customer_spending[customer] = customer_spending.get(customer, 0) + order.price

        if not customer_spending:
            return None

        return max(customer_spending, key=customer_spending.get)

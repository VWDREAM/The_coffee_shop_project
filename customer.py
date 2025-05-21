class Customer:
    _all_customers = []  # to keep track of all customers if needed

    def __init__(self, name):
        self.name = name
        Customer._all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Customer name must be a string between 1 and 15 characters.")
    def orders(self):
        from order import Order
        # Returns list of orders made by this customer
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        # Returns unique list of Coffee instances ordered by this customer
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from order import Order
        # Creates an Order linked to this customer and given coffee
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        # Returns the Customer who spent the most money on the given coffee
        customer_spending = {}

        for order in coffee.orders():
            customer = order.customer
            customer_spending[customer] = customer_spending.get(customer, 0) + order.price

        if not customer_spending:
            return None

        # Return the customer with max total spending
        return max(customer_spending, key=customer_spending.get)
        def _repr_(self):
         return f"<Customer name={self.name}>"

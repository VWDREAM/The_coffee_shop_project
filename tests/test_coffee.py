import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name_setter_valid():
    coffee = Coffee()
    coffee.name = "Latte"
    assert coffee.name == "Latte"

def test_coffee_name_setter_invalid():
    coffee = Coffee()
    with pytest.raises(ValueError):
        coffee.name = "Hi"  # less than 3 chars should raise

def test_orders_and_customers_methods():
    # Setup
    cust1 = Customer("Alice")
    cust2 = Customer("Bob")
    coffee = Coffee()
    coffee.name = "Espresso"

    order1 = Order(cust1, coffee, 3.5)
    order2 = Order(cust2, coffee, 4.0)
    order3 = Order(cust1, coffee, 3.0)

    # Test orders() returns all orders for this coffee
    coffee_orders = coffee.orders()
    assert len(coffee_orders) == 3
    assert order1 in coffee_orders and order2 in coffee_orders and order3 in coffee_orders

    # Test customers() returns unique customers who ordered this coffee
    coffee_customers = coffee.customers()
    assert cust1 in coffee_customers and cust2 in coffee_customers
    assert len(coffee_customers) == 2

def test_num_orders_and_average_price():
    cust = Customer("Charlie")
    coffee = Coffee()
    coffee.name = "Mocha"

    Order(cust, coffee, 5.0)
    Order(cust, coffee, 7.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 6.0

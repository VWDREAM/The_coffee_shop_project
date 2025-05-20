# tests/test_customer.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer

def test_customer_has_name():
    customer = Customer("Alice")
    assert customer.name == "Alice"

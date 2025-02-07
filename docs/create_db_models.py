import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Customer(Base):
    """description: Table storing customer data."""
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Address(Base):
    """description: Table storing addresses for customers."""
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    country = Column(String, nullable=False)

class Product(Base):
    """description: Table storing product data."""
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Order(Base):
    """description: Table storing order data."""
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    shipped_date = Column(DateTime, nullable=True)
    status = Column(String, nullable=False)

class OrderDetail(Base):
    """description: Table storing details of each order."""
    __tablename__ = 'order_details'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)

class Payment(Base):
    """description: Table storing payment details for orders."""
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, default=datetime.datetime.utcnow)
    method = Column(String, nullable=False)

class Supplier(Base):
    """description: Table storing supplier data."""
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    contact_name = Column(String, nullable=True)

class Stock(Base):
    """description: Table for managing product stock."""
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, default=0, nullable=False)

class Category(Base):
    """description: Table storing product categories."""
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)

class ProductCategory(Base):
    """description: Association table for products and categories."""
    __tablename__ = 'product_categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

class Employee(Base):
    """description: Table storing employee information."""
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    hire_date = Column(DateTime, default=datetime.datetime.utcnow)

class CustomerServiceTicket(Base):
    """description: Table storing customer service tickets."""
    __tablename__ = 'customer_service_tickets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    issue_description = Column(Text, nullable=False)
    opened_date = Column(DateTime, default=datetime.datetime.utcnow)
    closed_date = Column(DateTime, nullable=True)

# Create the engine and session
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add sample data to the database
# Add customers
customer1 = Customer(first_name="John", last_name="Doe", email="john.doe@example.com", phone="123-456-7890")
session.add(customer1)
session.add(Address(customer_id=1, street="123 Elm St", city="Anytown", state="AZ", zip_code="85001", country="USA"))

customer2 = Customer(first_name="Jane", last_name="Smith", email="jane.smith@example.com")
session.add(customer2)

# Add products
product1 = Product(name="Widget", description="A useful widget", price=19.99)
session.add(product1)

product2 = Product(name="Gadget", description="A fancy gadget", price=29.99)
session.add(product2)

# Add suppliers
supplier1 = Supplier(name="Supplier Co", contact_name="Alice Johnson", phone="987-654-3210", email="alice.j@supplierco.com")
session.add(supplier1)

# Add orders and order details
order1 = Order(customer_id=1, status="Processing")
session.add(order1)

order_detail1 = OrderDetail(order_id=1, product_id=1, quantity=2, unit_price=19.99)
session.add(order_detail1)

# Add payments
payment1 = Payment(order_id=1, amount=39.98, method="Credit Card")
session.add(payment1)

# Add stock
stock1 = Stock(product_id=1, quantity=100)
session.add(stock1)

# Add categories
category1 = Category(name="Electronics", description="Electronic devices and gadgets")
session.add(category1)

# Add product categories
product_category1 = ProductCategory(product_id=1, category_id=1)
session.add(product_category1)

# Add employees
employee1 = Employee(first_name="Michael", last_name="Johnson", email="michael.johnson@xyzcorp.com")
session.add(employee1)

# Add customer service tickets
ticket1 = CustomerServiceTicket(customer_id=1, issue_description="Problem with the order processing")
session.add(ticket1)

session.commit()

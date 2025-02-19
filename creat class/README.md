# Car Management System

## Overview

This project implements a car management system using object-oriented programming in Python. It includes classes for managing car records, including subclasses for specific types of cars.

## Classes

### Car

Represents a car with the following attributes and methods:

- **Attributes:**
  - `company` (string): The company of the car.
  - `model` (string): The model of the car.
  - `year` (integer): The manufacturing year of the car.
  - `price` (integer): The price of the car.

- **Methods:**
  - `__init__(self, company=None, model=None, year=None, price=None)`: Initializes the car's details.
  - `display_info(self)`: Prints out the car's details in a formatted manner.
  - `calculate_depreciation(self, current_year)`: Calculates and returns the car's depreciation value based on the current year.

### Petrol

A subclass of `Car` with an additional attribute:

- **Attributes:**
  - `expenses` (float): The expenses of the petrol car.

- **Methods:**
  - `__init__(self, company=None, model=None, year=None, price=None, expenses=None)`: Initializes the petrol car's details.
  - `display_info(self)`: Prints out the petrol car's details in a formatted manner.

### Coupe

A subclass of `Car` with an additional attribute:

- **Attributes:**
  - `seats` (integer): The number of seats in the coupe car.

- **Methods:**
  - `__init__(self, company=None, model=None, year=None, price=None, seats=None)`: Initializes the coupe car's details.
  - `display_info(self)`: Prints out the coupe car's details in a formatted manner.


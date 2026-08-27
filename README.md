# Vehicle Management System 🚗🏍️⚡

## Overview

This is a Python Object-Oriented Programming (OOP) project that demonstrates the three main pillars of OOP:

* **Encapsulation**
* **Inheritance**
* **Polymorphism**

The project manages different types of vehicles, including Cars, Bikes, and Electric Cars.

## Classes Used

### 1. Vehicle

`Vehicle` is the parent class. It contains common vehicle attributes such as:

* Brand
* Speed
* Fuel

It also uses private attributes with getter and setter methods for controlled access.

### 2. Car

`Car` inherits from the `Vehicle` class and adds:

* Number of doors
* Car-specific information
* Overridden `start()` method

### 3. Bike

`Bike` inherits from `Vehicle` and adds:

* Bike type
* Its own `start()` method

### 4. ElectricCar

`ElectricCar` inherits from `Car` and adds:

* Battery level
* Its own `start()` method

## OOP Concepts Demonstrated

### Encapsulation

Private attributes such as speed and fuel are accessed and updated through getter and setter methods.

### Inheritance

`Car` and `Bike` inherit from `Vehicle`, while `ElectricCar` inherits from `Car`.

### Polymorphism

The `start()` method is overridden in different classes, so each vehicle type starts differently.

## Features

* Create different types of vehicles
* Display vehicle information
* Update speed and fuel using setters
* Count the total number of vehicles
* Demonstrate method overriding
* Demonstrate inheritance and encapsulation

## Technologies Used

* **Python**
* **Object-Oriented Programming (OOP)**

## Project Structure

```text
Vehicle-Management-System/
│
├── vehicle_management_system.py
└── README.md
```

## Author

**Kinza Khalid**

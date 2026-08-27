# OOP with it three pillars (inheritance, polymorphism, encapsulation) in a single program 

# parent class 
class Vehicle:
    total_vehicles = 0

    def __init__(self, brand, speed, fuel):
        self.brand = brand
        self.__speed = speed #-private: restricted (can't access directly)
        self.__fuel = fuel  #-private

        Vehicle.total_vehicles += 1 # adds + 1 vehicle when a new object is created 

    # --Getter function: controlled way to fetch private data
    def get_speed(self):
        return self.__speed

    # -- setter function: controlled way to update private data
    def set_speed(self, new_speed):
        if  new_speed <= 0:
            print('Speed must be greater than zero')
        else:
            self.__speed = new_speed

    #--Getter function for fuel
    def get_fuel(self):
        return self.__fuel

    #--Setter function for fuel
    def set_fuel(self, new_fuel):
        if new_fuel <= 0:
            print('Fuel must be greater than zero')
        else:
            self.__fuel = new_fuel

    # -- methods
    def vehicle_info(self):
        print(f'Vehicle Brand: {self.brand}')
        print(f'Vehicle Speed: {self.__speed}')
        print(f'Vehicle Fuel: {self.__fuel}')

    def start(self):
        print(f'{self.brand} vehicle is starting.')



# --child class / derived class speed
class Car(Vehicle):
    # -- CAR'S own instructor function
    def __init__(self,  brand, speed, fuel, doors):
        super().__init__(brand, speed, fuel)
        self.doors = doors

    # Car's own method
    def car_info(self):
        self.vehicle_info()
        print(f'Doors: {self.doors}')

    # --polymorphism: Overriding parent class's start function
    def start(self):
        print(f'{self.brand} car is starting with a key.')

# --child class / derived class
class Bike(Vehicle):
    def __init__(self, brand, fuel, speed,  bike_type):
        super().__init__(brand, speed, fuel)
        self.bike_type = bike_type

    def start(self):
        print(f'{self.brand} Bike started with kick')

    def bike_info(self):
        self.vehicle_info()
        print(f'Bike Type: {self.bike_type}')
        
# --child class / derived class
class ElectricCar(Car):
    def __init__(self, brand, fuel, speed, battery_level,doors):
        super().__init__(brand,speed,fuel,doors)
        self.battery_level = battery_level

    def ec_info(self):
        self.car_info()
        print(f'Battery level: {self.battery_level}')

    def start(self):
        print(f'{self.brand} is starting silently.')

# -- creating objects for each of the class
c = Car('Honda', 120, 'Petrol', 4)
b = Bike('Suzuki', 'Petrol', 60, 'sport')
ev = ElectricCar('BYD','Electric', 90 , 2, 4 )

print('\n --- Car info ---')
c.car_info()

print('\n --- Bike info ---')
b.bike_info()

print('\n --- Electric car info ---')
ev.ec_info()

# --accessing class atributes 
print(f'\n --- Total number of vehicles: {Vehicle.total_vehicles}')

vehicles = [c, b, ev]

for vehicle in vehicles:
    vehicle.start()

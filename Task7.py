from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def __str__(self):
        return f'{self.make} {self.model}, {self.year}, {self.speed}'

    @abstractmethod
    def info(self):
        print("Some vehicle")


class Ship(Vehicle):
    def __init__(self, make, model, year, speed, size, ship_class):
        super().__init__(make, model, year, speed)
        self.size = size
        self.ship_class = ship_class

    def __str__(self):
        return super().__str__() + f', {self.size}, {self.ship_class}'

    def info(self):
        print("Some ship")


class WheeledVehicle(Vehicle):
    def __init__(self, make, model, year, speed, num_wheels):
        super().__init__(make, model, year, speed)
        self.num_wheels = num_wheels

    def __str__(self):
        return super().__str__() + f', {self.num_wheels}'

    @abstractmethod
    def info(self):
        print("Some wheeled vehicle")


class Car(WheeledVehicle):
    def __init__(self, make, model, year, speed, num_wheels, color, engine, seat):
        super().__init__(make, model, year, speed, num_wheels)
        self.color = color
        self.engine = engine
        self.seat = seat

    def __str__(self):
        return super().__str__() + f', {self.color}, {self.engine}, {self.seat}'

    def info(self):
        print("Some car")


class Bicycle(WheeledVehicle):
    def __init__(self, make, model, year, speed, num_wheels, bike_type):
        super().__init__(make, model, year, speed, num_wheels)
        self.bike_type = bike_type

    def __str__(self):
        return super().__str__() + f', {self.bike_type}'

    def info(self):
        print("Some bicycle")


car = Car("Subaru", "Outback", 2019, 200, 4, "blue", 3.6, 4)
bicycle = Bicycle("some make", "some model", 2010, 20, 2, "road")
ship = Ship("some make", "some model", 2010, 60, 100, "sailing")

car.info()
print(car)

bicycle.info()
print(bicycle)

ship.info()
print(ship)

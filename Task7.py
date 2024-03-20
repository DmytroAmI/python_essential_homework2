from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Describe abstract base parent class"""
    def __init__(self, make, model, year, speed):
        """Initialize the attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def __str__(self):
        """Return a string representation of the attributes"""
        return f'{self.make} {self.model}, {self.year}, {self.speed}'

    @abstractmethod
    def info(self):
        """Print some information"""
        print("Some vehicle")


class Ship(Vehicle):
    """Describe child class Ship"""
    def __init__(self, make, model, year, speed, size, ship_class):
        """Override and initialize the attributes"""
        super().__init__(make, model, year, speed)
        self.size = size
        self.ship_class = ship_class

    def __str__(self):
        """Return a string representation of the attributes"""
        return super().__str__() + f', {self.size}, {self.ship_class}'

    def info(self):
        """Override parent method, print some information"""
        print("Some ship")


class WheeledVehicle(Vehicle):
    """Describe child abstract class WheeledVehicle"""
    def __init__(self, make, model, year, speed, num_wheels):
        """Initialize the attributes"""
        super().__init__(make, model, year, speed)
        self.num_wheels = num_wheels

    def __str__(self):
        """Return a string representation of the attributes"""
        return super().__str__() + f', {self.num_wheels}'

    @abstractmethod
    def info(self):
        """Print some information, override"""
        print("Some wheeled vehicle")


class Car(WheeledVehicle):
    """Describe child class Car"""
    def __init__(self, make, model, year, speed, num_wheels, color, engine, seat):
        """Initialize the attributes"""
        super().__init__(make, model, year, speed, num_wheels)
        self.color = color
        self.engine = engine
        self.seat = seat

    def __str__(self):
        """Return a string representation of the attributes"""
        return super().__str__() + f', {self.color}, {self.engine}, {self.seat}'

    def info(self):
        """Print some information, override"""
        print("Some car")


class Bicycle(WheeledVehicle):
    """Describe child class Bicycle"""
    def __init__(self, make, model, year, speed, num_wheels, bike_type):
        """Initialize the attributes"""
        super().__init__(make, model, year, speed, num_wheels)
        self.bike_type = bike_type

    def __str__(self):
        """Return a string representation of the attributes"""
        return super().__str__() + f', {self.bike_type}'

    def info(self):
        """Print some information, override"""
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

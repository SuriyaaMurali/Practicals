from car import Car
from random import randint


class UnreliableCar(Car):
    """"""

    def __init__(self, name, fuel, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return super().__str__()

    def drive(self, distance):
        random_number = randint(1, 100)
        distance_driven = 0
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
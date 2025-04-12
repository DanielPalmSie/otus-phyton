from abc import ABC
from .exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):

        if not self.started:
            if self.fuel <= 0:
                raise LowFuelError("No fuel to start the vehicle.")
            self.started = True

    def move(self, distance):

        required_fuel = distance * self.fuel_consumption
        if self.fuel < required_fuel:
            raise NotEnoughFuel("Not enough fuel to move.")
        self.fuel -= required_fuel

from .base import Vehicle
from .exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo):
        if self.cargo + cargo > self.max_cargo:
            raise CargoOverload("Cargo overload!")
        self.cargo += cargo

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo

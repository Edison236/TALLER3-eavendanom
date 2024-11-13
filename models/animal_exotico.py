from abc import ABC, abstractmethod
from models.animal import Animal

class AnimalExotico(Animal):
    def __init__(self, name, weight, age, country_origin, tax):
        super().__init__(name, weight, age)
        self.country_origin = country_origin
        self.tax = tax

    @abstractmethod
    def make_sound(self):
        pass
    
    def calculate_freight(self, weight: float ):
        return self.tax * weight
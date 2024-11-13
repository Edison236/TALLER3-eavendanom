from models.animal_exotico import AnimalExotico

class Huron(AnimalExotico):

    def __init__(self, name, weight, age, country_origin, tax):
        super().__init__(name, weight, age, country_origin, tax)

    def make_sound(self):
        return "¡Eek Eek!"
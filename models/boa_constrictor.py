from models.animal_exotico import AnimalExotico

class Boa(AnimalExotico):

    def __init__(self, name, weight, age, country_origin, tax):
        super().__init__(name, weight, age, country_origin, tax)
        self.eaten_mice = 0

    def make_sound(self):
        return "¡Tsss!"
    
    def add_mouse(self):
        if self.eaten_mice == 10:
            raise ValueError("Demasiados Ratones!.")
        self.eaten_mice += 1

    def feed_boa(self) -> str:
        if self.eaten_mice == 10:
            return "La boa está llena"
        self.eaten_mice += 1
        return "Exito"
    
    def get_eaten_mice(self):
        return self.eaten_mice
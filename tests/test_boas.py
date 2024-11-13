import unittest 
from models.boa_constrictor import Boa

class TestBoas(unittest.TestCase):

    def setUp(self):
        self.boa = Boa("Soy una boa", 15.47, 4, "Durango", 8450.23)
        self.boa.add_mouse()
    
    def tearDown(self):
        pass

    def test_make_sound(self):
        print("Esto es el sonido de una boa")
        sound = self.boa.make_sound()
        print(sound)
    
    def test_calculate_freight(self):
        print("El flete vale:")
        freight = self.boa.calculate_freight(15.47)
        print(freight)

    def test_Feed(self):
        print("Alimentar boa")
        self.boa.add_mouse()
        count = self.boa.get_eaten_mice()
        print(f"Se ha comido {count} ratones")

    def test_validate_adden_mice(self):
        print("validar comida de las boas")
        for i in range(10):
            print(i)
            self.boa.add_mouse()
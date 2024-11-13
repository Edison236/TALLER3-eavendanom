import unittest
from models.huron import Huron

class TestHurones(unittest.TestCase):

    def setUp(self):
        self.hurones = Huron("Axel",15.2,4,"Brasil",9500.25)
    
    def tearDown(self):
        pass
    
    def test_make_sound(self):
        print("Esto es el sonido de un Huron")
        sound = self.hurones.make_sound()
        print(sound)
    
    def test_calculate_freight(self):
        print("El flete vale:")
        freight = self.hurones.calculate_freight(1.2)
        self.assertEqual(freight,11400.3)

import unittest
from models.guarderia import Guarderia
from models.huron import Huron

class TestGuarderia(unittest.TestCase):

    def setUp(self):
        self.guarderia = Guarderia()
    
    def tearDown(self):
        pass

    def test_feed_boa(self):
        for i in range(12):
            response = self.guarderia.feed_boa(1)
            print(response)
        response_two = self.guarderia.feed_boa(5)
        print(response_two)
        response_three = self.guarderia.feed_boa(None)
        print(response_three)

    def test_show_huron(self):
        print(self.guarderia.huron[0].__dict__)
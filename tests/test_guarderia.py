import unittest
from models.guarderia import Guarderia

class TestGuarderia(unittest.TestCase):

    def setUp(self):
        self.boas = Guarderia()
    
    def tearDown(self):
        pass

    def test_feed_boa(self):
        for i in range(12):
            response = self.boas.feed_boa(1)
            print(response)
        response_two = self.boas.feed_boa(5)
        print(response_two)
        response_three = self.boas.feed_boa(None)
        print(response_three)
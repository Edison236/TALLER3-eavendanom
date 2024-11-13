from models.boa_constrictor import Boa
from models.huron import Huron

class Guarderia:
    def __init__(self):
        self.huron = [Huron("Axel",15.2,5,"Brasil",4500.45),Huron("Casper",10.2,4,"Argentina",9500.25)]
        self.boa = [Boa("Boa grande", 12.17, 5, "California", 8450.23),Boa("Boa ", 9.27, 2, "Durango", 15800.23)]

    def feed_boa(self, boa_index):
        try:
            if boa_index is None or boa_index < 0 or boa_index > len(self.boa):
                raise ValueError("Esta Boa no existe!")            
            response = self.boa[boa_index].feed_boa()
            return response
        except ValueError as e:
            return str(e)
        

from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self, name:str, weight:float, age:int ) -> None:
        self.name = name
        self.weight = weight
        self.age = age 

    @abstractmethod
    def make_sound(self):
        pass

    #Get and set
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value:str) -> None:
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError('Expected str')
    
    @property
    def weight(self) -> float:
        return self.__weight
    
    @weight.setter
    def weight(self, value:float) -> None:
        if isinstance(value, float):
            self.__weight = value
        else:
            raise ValueError('Expected float')
        
    @property
    def age(self) -> int:
        return self.__age
    
    @age.setter
    def age(self, value:int) -> None:
        if isinstance(value, int):
            self.__age = value
        else:
            raise ValueError('Expected int')
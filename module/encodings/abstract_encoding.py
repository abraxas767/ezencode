from abc import ABC, abstractmethod

class Encoding(ABC):

    @abstractmethod
    def encode(self, data:str):
        pass

    @abstractmethod
    def decode(self, data:str):
        pass

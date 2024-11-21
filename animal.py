# abstractmethod
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
        
    def set_marca(self, nome):
        self.__nome = nome

    def set_modelo(self, idade):
        self.__idade = idade

    @abstractmethod
    def mostrar(self):
        pass
# Importa a classe Animal de 'animal'
from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, porte, raca):
        super().__init__(nome, idade)
        self.__porte = porte
        self.__raca = raca

    def set_porte(self, porte):
        self.__porte = porte

    def set_raca(self, raca):
        self.__raca = raca

    def get_porte(self):
        return self.__porte
    
    def get_raca(self):
        return self.__raca

    def mostrar(self):
        return(f'''
            . Cachorro:
            Nome: {self.get_nome()}
            Idade: {self.get_idade()}
            Porte: {self.get_porte()}
            Raça: {self.get_raca()}
            ''')

# Teste
c = Cachorro("Pelutinho", 13, "Pequeno", "Pooddle Toy")
print(c.mostrar())
# Importa a classe Animal de 'animal'
from animal import Animal

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca = raca

    def set_raca(self, raca):
        self.__raca = raca

    def get_raca(self):
        return self.__raca
    
    def mostrar(self):
        return(f'''
            . Gato:
            Nome: {self.get_nome()}
            Idade: {self.get_idade()}
            Raça: {self.get_raca()}
            ''')

# Teste
g = Gato("Neguinho", 12, "Persa")
print(g.mostrar())
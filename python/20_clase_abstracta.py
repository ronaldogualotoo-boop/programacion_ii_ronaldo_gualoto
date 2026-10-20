from abc import ABC, abstractmethod

class NaveEspacial(ABC):
    modelo: str
    
    def __init__(self, modelo: str):
        self.modelo = modelo

    @abstractmethod
    def despegar(self):
        pass

class NaveCapsula(NaveEspacial):
    modelo: str
    
    def __init__(self, modelo: str):
        self.modelo = modelo

    
    def despegar(self):
        print(self.modelo,"despegar motores de Capsule Corp")

class NaveSaiyayin(NaveEspacial):
    
    def __init__(self, modelo: str):
            self.modelo = modelo
    
        
    def despegar(self):
        print(self.modelo,"despegar imendiatamente")


nave_bulma = NaveCapsula("Nave de Bulma")
nave_vegeta = NaveSaiyayin("Capsula Saiyajin")
nave_bulma.despegar()
nave_vegeta.despegar()

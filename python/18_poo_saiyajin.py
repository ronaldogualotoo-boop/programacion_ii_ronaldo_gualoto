from poo_guerrero import Guerrero

class Saiyajin(Guerrero):
    def __init__(self, nombre: str):
        super().__init__(nombre)

    def transformarse(self):
        print(self.nombre, "se transforma en Super Saiyajin")

goku = Saiyajin("Goku")
goku.presentarse()
goku.transformarse() 

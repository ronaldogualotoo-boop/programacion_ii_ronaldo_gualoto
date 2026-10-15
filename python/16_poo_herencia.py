class Guerrero:
    nombre: str

    def __init__(self, nombre: str):
        self.nombre = nombre

    def presentarse(self):
        print("Mi poderoso nombre es: ", self.nombre)


class Saiyajin(Guerrero):

    def __init__(self, nombre: str):
        super().__init__(nombre)

    def transformarse(self):
        print(self.nombre, "se transforma en Super Saiyajin")


goku = Saiyajin("Goku")
goku.presentarse()
goku.transformarse()

class Androide:
    nombre: str
    energia: int

    def __init__(self, nombre: str, energia: int):
        self.nombre = nombre
        self.energia = energia

    def mostrar_energia(self):
        print("Androide: ", self.nombre)
        print("Energia: ", self.energia)

class AndroideRecargable(Androide):
    def __init__(self, nombre: str, energia: int):
        super().__init__(nombre, energia)

    def recargar(self, cantidad: int):
        if cantidad > 0:
            self.energia += cantidad

androide17 = AndroideRecargable("Numero 17", 600)
print("========== ANTES DE REACARGAR ===========")
androide17.mostrar_energia()
androide17.recargar(100)
print("========= DESPUES DE RECARGAR ==========")
androide17.mostrar_energia()
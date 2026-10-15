class Guerrero:
    nombre: str
    poder: int
    
    def __init__(self, nombre: str, poder: int):
        self.nombre = nombre
        self.poder = poder

    def saludar(self):
        print("Hola, soy : ", self.nombre)

    def entrenar(self):
        aumento = 200
        self.poder += aumento

    def atacar(selt, cantidad):
        danio = self.poder*cantidad
        print ("Gerrero",self.nombre)
        print("Daño causado: " , danio)



goku = Guerrero("Goku", 9000)


goku.saludar()

print ("nombre del personaje: ", goku.nombre)
print ("Poder del personaje: ", goku.poder)
goku.entrenar()
print ("poder del personaje: ", goku.poder)
goku.atacar(3)



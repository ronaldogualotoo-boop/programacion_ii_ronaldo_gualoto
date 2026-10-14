print("===== CONTROL DE ENERGIA =====")
energia_texto = "ochenta"

try:
    energia = int(energia_texto)
    print(energia)
except ValueError:
    print("error :debe ser numerico")

print("Findel sistema")

"""
valvueError
TypeError
KeyError
ZeroDivisionError
"""
def calcular_energia(total,cantidad):
    try:
        resultado = total / cantidad
    except ZeroDivisionError:
        print("error: division entre cero")
        return None
    except TypeError:
        print("error: tipo de dato no valido")
        return None
print("Caso 1: ", calcular_energia(100,4))
print("Caso 2: ", calcular_energia(100,0))
print("Caso 3: ", calcular_energia(100,"cuatro"))
print("======== Dianostico R2-D2 ========")
try:
    energia = int(90)
    print("energia" ,energia)
except ValueError:
    print("error: error de lectura")
else:
    print("diagnostico completado")
finally:
    print("Cerrando diagnostico")

def validar_energia(energia):
    if type(energia) is not int:
        raise TypeError("La enrgia debe ser un numero entero")
    if energia < 0 or energia > 100:
        raise ValueError("La energia debe estar entre 0 y 100")
    return energia

try:
    resultado = validar_energia(150)
    print("Energia", resultado)
except (TypeError, ValueError) as error:
    print("Error:", error)















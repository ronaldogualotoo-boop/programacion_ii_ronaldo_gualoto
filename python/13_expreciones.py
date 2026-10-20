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



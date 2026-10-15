##funciones
def activar_sistema():
    print("==sisema de naboo ==") 
    print("==sistema de control activo ==")

activar_sistema()         

def saludar_jedi(nombre):
    print(f"que la fuerza te acompañe {nombre}")

saludar_jedi("quigon jinn")
saludar_jedi("Obi-Wan Kenobi")

def mostrar_nave(nombre,combustible):
    print(f"nombre: {nombre}")
    print(f"combustible cantidad: {combustible}")

mostrar_nave("Caza N-1",80)

# funbciones con retorno 
# return yo reinicio de rezero


def calcular_combustible(inicial, consumo):
    return inicial - consumo

resultado = calcular_combustible(100,25)
print(f"Combustible : {resultado}" )

resultado = calcular_combustible(100,35)
print(f"Combustible : {resultado}" )

print(f"Combustible : {calcular_combustible(100,15)}" )

def nave_preparada(combustible):
    return combustible>= 50

if nave_preparada(80):
    print("La nave está preparada para despegar.")
else:
    print("La nave no está preparada para despegar.")
        
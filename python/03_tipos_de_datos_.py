nave = "Caza estelar N-1"
planeta = "Naboo"
velocidad = 850.0
cantidad_motores = 2
escudos_activados = True
piloto_asignado = None

print("Nave:", nave)
print("Planeta:", planeta)
print("Velocidad:", velocidad)
print("Cantidad de motores:", cantidad_motores)
print("Escudos activados:", escudos_activados)
print("Piloto asignado:", piloto_asignado)
# comprobamos tipos
print("Tipo de Nave:", type(nave))
print("Tipo de Planeta:", type(planeta))
print("Tipo de Velocidad:", type(velocidad))
print("Tipo de Cantidad de motores:", type(cantidad_motores))
print("Tipo de Escudos activados:", type(escudos_activados))
print("Tipo de Piloto asignado:", type(piloto_asignado))

droide = "R2-D2"
print("Droide:", droide)
print("Tipo de Droide:", type(droide))

droide = 42
print("Droide:", droide)
print("Tipo de Droide:", type(droide))

droide = True
print("Droide:", droide)
print("Tipo de Droide:", type(droide))
velocidad_anakin = 950
velocidad_sebulba = 900

print("¿Anakin es más rápido que Sebulba?", velocidad_anakin > velocidad_sebulba)
print("¿Anakin es más lento que Sebulba?", velocidad_anakin < velocidad_sebulba)
print("¿Anakin es igual de rápido que Sebulba?", velocidad_anakin == velocidad_sebulba)
print("¿Anakin es distinto de Sebulba?", velocidad_anakin != velocidad_sebulba)
print("¿Anakin es más rápido o igual que Sebulba?", velocidad_anakin >= velocidad_sebulba)
print("¿Anakin es más lento o igual que Sebulba?", velocidad_anakin <= velocidad_sebulba)

resultado = velocidad_anakin > velocidad_sebulba
print("Resultado de la comparación:", resultado)
print("tipo de resuldado:", (resultado))

#operadores logicos

"""
# - and (y)
# - or (o)
# - not (no)
"""

motores_funcionando = True
escudos_funcionando = False
combustible = 80

print("¿Todos los sistemas están funcionando?", motores_funcionando and escudos_funcionando)
print("¿Algunos sistemas están funcionando?", motores_funcionando or escudos_funcionando)
print("¿Los motores no están funcionando?", not motores_funcionando)

cantidad_motores = 2
cantidad_alas = 4
combustible = 80

print("¿La nave tiene al menos 2 motores y 4 alas?")
print(cantidad_motores >= 2 and cantidad_alas >= 4 and combustible >= 50)
print("¿La nave tiene al menos 2 motores o 4 alas?")
print(cantidad_motores >= 2 or cantidad_alas >= 4 or combustible >= 50)
print("¿La nave no tiene al menos 2 motores?")
print(not cantidad_motores >= 2 and combustible >= 50 and cantidad_alas >= 4)


# Operadores de asignación:
"""
- = (asignación)
- += (suma y asignación)
- -= (resta y asignación)
- *= (multiplicación y asignación)
- /= (división y asignación)
- %= (módulo y asignación)
- **= (potencia y asignación)
"""

velocidad = 100
print("Velocidad inicial:", velocidad)
velocidad += 50
print("Velocidad después de acelerar:", velocidad)
velocidad -= 30
print("Velocidad después de frenar:", velocidad)
multiplicador = 2
velocidad *= multiplicador
print("Velocidad después de multiplicar:", velocidad)
divisor = 4
velocidad /= divisor
print("Velocidad después de dividir:", velocidad)
modulo = 7
velocidad %= modulo
print("Velocidad después de aplicar módulo:", velocidad)
velocidad **= 2
print("Velocidad después de aplicar potencia:", velocidad)


# PRECEDENCIA DE OPERADORES
"""
1. ()
2. ** (potencia)
3. * / % (multiplicación, división, módulo)
4. + - (suma, resta)
"""
resultado_1 = 10 + 5 * 2
print("Resultado 1:", resultado_1)
resultado_2 = (10 + 5) * 2
print("Resultado 2:", resultado_2)


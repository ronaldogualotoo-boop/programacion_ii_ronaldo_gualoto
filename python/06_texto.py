# string cadenas de caracteres
jedi = "Qui-gon Jinn"
aprendiz = "Obi-Wan Kenobi"
droide = "R2-D2"
planeta = "Naboo"
codigo = "327"

print("El Jedi es: " + jedi)
print("El jedi", type(jedi))
print("El aprendiz es: " + aprendiz)
print("El aprendiz", type(aprendiz))
print("El droide es: " + droide)
print("El droide", type(droide))
print("El planeta es: " + planeta)
print("El planeta", type(planeta))
print("El código es: " + codigo)
print("El código", type(codigo))

longitud_jedi = len(jedi)
print("La longitud del nombre del Jedi es: " + str(longitud_jedi))
longitud_aprendiz = len(aprendiz)
print("La longitud del nombre del aprendiz es: " + str(longitud_aprendiz))

mensaje = "La Federación de Comercio ha establecido un bloqueo en Naboo."
print("El mensaje es: " + mensaje)
mensaje_mayusculas = mensaje.upper()
print("El mensaje en mayúsculas es: " + mensaje_mayusculas)
mensaje_minusculas = mensaje.lower()
print("El mensaje en minúsculas es: " + mensaje_minusculas)
comunicado = "Los Jedi son enviados a Naboo."
print("El comunicado es: " + comunicado)
nuevo_comunicado = comunicado.replace("Naboo", "Tatooine")
print("El nuevo comunicado es: " + nuevo_comunicado)

planetas = "Naboo, Tatooine, Coruscant, Alderaan"
planetas_lista = planetas.split(", ")
print(planetas_lista)
print("La lista de planetas es: " + str(planetas_lista))
# ciclo for

naves=[
    "Caza N-1",
    "Nave real de Naboo",
    "Transporte"
]
for nave in naves:
    print("Inspeccionando ", nave)

print("Inspección realizada")

rondas = range(1,6)

print("Tipo de Rondas: ", type(rondas))
for ronda in rondas:
    print(f"Ronda de vigilancia: {ronda}")
    print(f"Tipo de dato ronda : {type(ronda)}")

driodes = range(1,17,3)

print("Tipo de Rondas: ", type(driodes))
for droide in driodes:
    print(f"Reparar : driode B1 - {droide}")
    print(f"Tipo de dato droide : {type(droide)}")

planestas = [
    "naboo",
    "tatooine",
    "coruscant"
]
recorrido = enumerate(planestas, start=5)

for posicion, planeta in recorrido:
    print(f"destino {posicion} : {planeta}")
    print(f"Tipo de dato {type(posicion)}:{type(planeta)}")

paises = [
    "Ecuador",
    "Venezuela",
    "Chile",
    "Colombia",
    "Brasil",
    "Estados Unidos"
]

for pais in paises:
    if pais == "Chile":
        continue
    if pais == "Brasil":
        break
    print(f"País visitado: {pais}")

jedi = {}
jedi_activo={

    "nombre": "Obi-Wan Kenobi",
    "fuerza": "120",
    "estilo_pelea": "Samurai",
    "misiones": ["Rescate de la princesa", "Derrotar al lado oscuro"]
    "descripcion": {
        "estatura": "1.82 m",
        "especie": "Humano",    
    }  
}     



print(jedi_activo)
nave = dict(nombre="AZ-1", capacidad = 8, turbo_laser=2) 
print(nave)

jedi["nombre"] = "darth vader"
jedi["fuerza"] = 180
print(jedi)
for clave, valor in jedi.items():
    print(f"{clave} : {valor}")


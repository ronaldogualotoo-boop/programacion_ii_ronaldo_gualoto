"""
control de flota de naboo
"""

naves = [
    {
        "nombre": "Caza N-1",
        "combustible": 100,
        "driodes":["R2-D2, R2-A5"]
    },
    {
        "nombre": "Caza Real",
        "combustible": 150,
        "driodes":["R2-D2"]
    },
    {   "nombre": "TRANSPORTE",
        "combustible": 200,
        "driodes":["R2-D2,A2-A6"]
    }

]

naves_listas = 0
naves_recarga = 0
total_droides = 0
for numero, nave in enumerate(naves, start=1):
    print(f"--- Nave : {numero}-{nave}")
    if nave["combustible"]>=50:
        print("Estado inicial: LISTA")
        naves_listas+=1
    else:
        print("Estado inicial: RECARGA")
        naves_recarga+=1
        ciclo = 0
        while nave["combustible"] < 50:
            ciclo += 1
            nave["combustible"] += 10
        total_ciclos +=ciclo
        print("recarga completada")
        print("Estado final: LISTA")
    total_driodes=len(nave["driodes"])
    for droide in nave["driodes"]:
        print(f"droide: {droide}")

print("=================================")
print("Resumen")
print("=================================")
print(f"Total de naves: {len(naves)}")
print(f"Naves listas: {naves_listas}")
print(f"Naves en recarga: {naves_recarga}")
print(f"Total de driodes: {total_droides}")
print(f"Total de ciclos de recarga: {naves_recarga}")




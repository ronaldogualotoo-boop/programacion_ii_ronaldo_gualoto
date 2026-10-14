flota= [
    {
    "N1-001": {
        "nombre": "Caza N-1",
        "combustible": 80,
        }
    },
    {
        "NR-002": {
            "nombre": "Nave real de Naboo",
            "combustible": 35,
        }
    }
]
def create_nave (nave):
    flota.append(nave)
    print(f"nave agregada: {nave}")

def update_nave(nave_update, index):
    flota[index].update(nave_update)

def read_nave(index):
    return flota[index]

def delete_nave(index):
    return flota.pop(index)

print(flota)
new_nave = {
        "NR-006": {
        "nombre": "nave real NR6",
        "combustible": 80,
        }
}
create_nave(new_nave)
print(flota)
nave_updated = {
    "NR-006": {
        "nombre": "Nave Real NR6",
        "combustible": 85
    }
}
update_nave(nave_updated, 2)
print(flota)
print(read_nave(2))
print(delete_nave(2))
print(flota)




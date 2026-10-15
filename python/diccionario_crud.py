droides=[
    {
        "codigo":"B1-001",
        "modelo":"b1",
        "enegia":90,
        "activo":True
    },
    {
        "codigo":"B1-002",
        "modelo":"b1",
        "enegia":50,
        "activo":True
    },
    {
        "codigo":"DRO-001",
        "modelo":"Droideka",
        "enegia":80,
        "activo":False
    }          
]
cantidad_droides = len(droides)
print(cantidad_droides)
print(droides)
nuevo_droide = {
    "codigo":"B1-004",
    "modelo":"B1",
    "enegia":100,
    "activo":True
}
# CRUD
# Create
droides.append(nuevo_droide)
print(droides)
# Read
driode = droides[2]
print(f"codigo: {driode['codigo']}")
print(f"modelo: {driode['modelo']}")    
print(f"energia: {driode['enegia']}")    
print(f"activo: {driode['activo']}")    
#Update
driode = droides[2]
driode["codigo"] = "DRO-002"
driode["enegia"] = 85
driode["activo"] = False
print(f"droides: {driode}")
#Delete
elimidano = droides.pop(2)
print(f"droides: {droides}")




combustible = 100
vuelta = 1

while combustible >= 20:
    print(f"vuelta {vuelta}")
    print(f"Combustible inicial: {combustible}")
    
    combustible -= 20
    print(f"Combustible restante: {combustible}")
    vuelta += 1
print("carrera finalizada")
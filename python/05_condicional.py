# Condicional if
# Simple

combustible = 10
if combustible >= 10:
    print("Puedes despegar")
    
# Condicional if-else

creditos = int(input("Ingresa la cantidad de créditos que tienes: "))
precio_repuesto = int(input("Ingresa el precio del repuesto: "))
if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
else:
    print("No tienes suficientes créditos para comprar el repuesto")



# if anidado
if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
    if creditos > precio_repuesto:
        print("Te me sobran créditos")
    else:
        print("Te quedas justo con los créditos necesarios")
else:
    print("No tienes suficientes créditos para comprar el repuesto")


tipo_repuesto = input("Ingresa el tipo de repuesto (motor, ala, escudo): ")
if tipo_repuesto == "motor" and creditos >= precio_repuesto and tipo_repuesto == "ala":
    print("Puedes comprar el repuesto y te sobran créditos")
elif tipo_repuesto == "ala" and creditos >= precio_repuesto:
    print("Puedes comprar el repuesto y te sobran créditos")
elif tipo_repuesto == "escudo" and creditos >= precio_repuesto:
    print("Puedes comprar el repuesto y te sobran créditos")
else:
    print("Tipo de repuesto no válido")

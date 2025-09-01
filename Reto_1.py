print("Deteccion de enfermedades tempranas")
print("Ingrese el valor de hemoglobina en g/dL:")
hemoglobina = float(input())

print("Ingrese el genero (1: Masculino, 2: Femenino):")
genero = int(input())

if genero == 1:
    if hemoglobina < 12.2:
        print("Resultado: Baja")
    elif hemoglobina <= 16.6:
        print("Resultado: Normal")
    else:
        print("Resultado: Alta")
elif genero == 2:
    if hemoglobina < 12.6:
        print("Resultado: Baja")
    elif hemoglobina <= 15:
        print("Resultado: Normal")
    else:
        print("Resultado: Alta")
else:
    print("No es posible generar la alerta (genero invalido)")
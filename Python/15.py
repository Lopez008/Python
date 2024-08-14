def calcular_promedio(*args):
    if not args:
        raise ValueError("No se proporcionaron notas.")
    
    suma_notas = sum(args)
    
    promedio = suma_notas / len(args)
    
    return promedio

promedio = calcular_promedio(85, 90, 78, 92)
print(f"El promedio de las notas es: {promedio:.2f}")

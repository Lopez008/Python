def procesar_ventas(ventas_diarias):
    if not ventas_diarias:
        raise ValueError("El array de ventas está vacío.")

    total_ventas = sum(ventas_diarias)

    promedio_ventas = total_ventas / len(ventas_diarias)
    
    return total_ventas, promedio_ventas

ventas_diarias = [200, 450, 300, 400, 350, 500, 600]
total, promedio = procesar_ventas(ventas_diarias)

print(f"Total de ventas: ${total:.2f}")
print(f"Promedio de ventas por día: ${promedio:.2f}")

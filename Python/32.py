def simular_ventas(*ventas):
    total_ingresos = 0.0

    for producto, cantidad, precio_unitario in ventas:
        ingresos_venta = cantidad * precio_unitario
        total_ingresos += ingresos_venta
    
    return total_ingresos
    
ingresos_totales = simular_ventas(
    ("Producto A", 10, 15.0),
    ("Producto B", 5, 25.0),
    ("Producto C", 3, 50.0)
)

print(f"Total de ingresos generados: ${ingresos_totales:.2f}")

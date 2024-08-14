def analizar_ventas(ventas_mensuales):
    total_ventas = sum(ventas_mensuales)
    
    promedio_mensual = total_ventas / len(ventas_mensuales)
    
    max_ventas = max(ventas_mensuales)
    mes_max_ventas = ventas_mensuales.index(max_ventas) + 1 
    
    resultados = {
        "Total de Ventas": total_ventas,
        "Promedio Mensual": promedio_mensual,
        "Mes con Mayores Ventas": mes_max_ventas
    }
    
    return resultados

ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]
resultados = analizar_ventas(ventas_mensuales)
print(resultados)

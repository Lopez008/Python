def calcular_totales(resultados):
    total_goles_anotados = 0
    total_goles_recibidos = 0
    
    for goles_anotados, goles_recibidos in resultados.values():
        total_goles_anotados += goles_anotados
        total_goles_recibidos += goles_recibidos
    
    return (total_goles_anotados, total_goles_recibidos)

resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

totales = calcular_totales(resultados)
print("Total de goles anotados:", totales[0])
print("Total de goles recibidos:", totales[1])

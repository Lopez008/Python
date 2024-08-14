def calcular_promedios(estudiantes):
    promedios = {}
    
    for estudiante_id, materias in estudiantes.items():
        calificaciones_totales = []
        
        for calificaciones in materias.values():
            calificaciones_totales.extend(calificaciones)
        
        promedio_general = sum(calificaciones_totales) / len(calificaciones_totales)

        promedios[estudiante_id] = promedio_general
    
    return promedios

def ranking_estudiantes(estudiantes):
    promedios = calcular_promedios(estudiantes)

    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
    
    return ranking

estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

ranking = ranking_estudiantes(estudiantes)
print(ranking)

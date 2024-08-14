def PromedioGral(estudiantes):
    promedios = {}

    for estudiante_id, materias in estudiantes.items():
        totalCalificaciones = 0
        totalMaterias = 0

        for calificaciones in materias.values():
            totalCalificaciones += sum(calificaciones)
            totalMaterias += len(calificaciones)

        promedio = totalCalificaciones / totalMaterias
        promedios[estudiante_id] = promedio
 
    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
    
    return ranking

estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

rankingEstudiantes = PromedioGral(estudiantes)
print("Ranking de estudiantes basado en el promedio general:")
for estudiante_id, promedio in rankingEstudiantes:
    print(f"ID Estudiante {estudiante_id}: Promedio {promedio:.2f}")

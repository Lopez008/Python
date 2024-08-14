def promedio_estudiante(estudiantes, matricula):
    if matricula not in estudiantes:
        return "Estudiante no encontrado"
    
    calificaciones = estudiantes[matricula]["calificaciones"]
    if not calificaciones:
        return "No hay calificaciones registradas"
    
    promedio = sum(calificaciones.values()) / len(calificaciones)
    return round(promedio, 2)

# Diccionario
estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

matricula = 101
promedio = promedio_estudiante(estudiantes, matricula)
print(f"El promedio de calificaciones del estudiante con matrícula {matricula} es: {promedio}")
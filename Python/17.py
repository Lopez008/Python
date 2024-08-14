def filtrar_empleados_por_salario(empleados, salario_umbral):
    empleados_filtrados = {}
    
    for id_empleado, (nombre, edad, salario) in empleados.items():
        if salario > salario_umbral:
            empleados_filtrados[id_empleado] = (nombre, edad, salario)
    
    return empleados_filtrados

empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

salario_umbral = 2800
empleados_filtrados = filtrar_empleados_por_salario(empleados, salario_umbral)

print("Empleados con salario mayor a", salario_umbral, ":")
for id_empleado, (nombre, edad, salario) in empleados_filtrados.items():
    print(f"ID: {id_empleado}, Nombre: {nombre}, Edad: {edad}, Salario: {salario}")

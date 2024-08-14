def registro_empleado(nombre, edad, salario, **kwargs):
    empleado_info = {
        "Nombre": nombre,
        "Edad": edad,
        "Salario": salario
    }
    
    empleado_info.update(kwargs)
    
    return empleado_info

info_empleado = registro_empleado(
    "Ana", 
    30, 
    3000, 
    direccion="AA", 
    telefono="1234"
)

print(info_empleado)

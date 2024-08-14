def haceReserva(reservas, fecha, nombre_huesped, habitacion, precio):
    if fecha not in reservas:
        reservas[fecha] = []
    
    reservas_fecha = reservas[fecha]

    for _, habitacion_asignada, _ in reservas_fecha:
        if habitacion_asignada == habitacion:
            return "La habitación ya está ocupada en esta fecha."

    reservas_fecha.append((nombre_huesped, habitacion, precio))
    
    return "Reserva realizada con éxito."

reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

resultado = haceReserva(reservas, "2024-08-15", "María", 103, 200)
print(resultado)

resultado = haceReserva(reservas, "2024-08-15", "Pedro", 101, 160)
print(resultado) 

resultado = haceReserva(reservas, "2024-08-17", "Luis", 101, 150)
print(resultado) 

print(reservas)

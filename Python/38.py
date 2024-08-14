def actualizar_suscripcion(suscripciones, usuario, suscripcion, **opciones_adicionales):
    if usuario not in suscripciones:
        suscripciones[usuario] = []

    suscripciones[usuario].append(suscripcion)

    if opciones_adicionales:
        print(f"Opciones adicionales para {usuario}: {opciones_adicionales}")
    
    return suscripciones

suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

estado_actualizado = actualizar_suscripcion(suscripciones, usuario="Luis", suscripcion="mensual", auto_renovacion=True)
print(estado_actualizado)

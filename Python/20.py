def configurar_app(**kwargs):
    configuraciones_predeterminadas = {
        "modo_oscuro": False,
        "idioma": "en",
        "notificaciones": True
    }
    
    configuraciones_predeterminadas.update(kwargs)
    
    return configuraciones_predeterminadas

config = configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)
print(config)

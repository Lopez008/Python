def analizar_temperaturas(temperaturas):
    if not temperaturas:
        raise ValueError("El array de temperaturas está vacío.")
    
    temperatura_media = sum(temperaturas) / len(temperaturas)
    
    temperatura_maxima = max(temperaturas)
    
    temperatura_minima = min(temperaturas)
    
    return temperatura_media, temperatura_maxima, temperatura_minima

temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]
media, maxima, minima = analizar_temperaturas(temperaturas)

print(f"Temperatura media del mes: {media:.2f}°C")
print(f"Temperatura máxima del mes: {maxima:.2f}°C")
print(f"Temperatura mínima del mes: {minima:.2f}°C")

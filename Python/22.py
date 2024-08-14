def calcular_precios_totales(paquetes):
    precios_totales = {}
    
    for destino, precio_por_dia, duracion in paquetes:
        precio_total = precio_por_dia * duracion
        precios_totales[destino] = precio_total
    
    return precios_totales

paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

precios = calcular_precios_totales(paquetes)
print(precios)

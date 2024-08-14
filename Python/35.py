def filtraRutas(rutas, distanciasMax):
    rutasValidas = []
    
    for i in range(len(rutas)):
        origen, destino, distancia = rutas[i]
        distanciaMax = distanciasMax[i]

        if distancia <= distanciaMax:
            rutasValidas.append(rutas[i])
    
    return rutasValidas

rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distanciasMax = [600, 400, 500]

rutasFiltradas = filtraRutas(rutas, distanciasMax)
print(rutasFiltradas)

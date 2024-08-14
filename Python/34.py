def calcularFrecuencias(encuestas):
    frecuencias = {}
    
    for pregunta, respuestas in encuestas.items():

        conteoRespuestas = {}

        for respuesta in respuestas:
            if respuesta in conteoRespuestas:
                conteoRespuestas[respuesta] += 1
            else:
                conteoRespuestas[respuesta] = 1

        frecuencias[pregunta] = conteoRespuestas
    
    return frecuencias

encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

resultadosFrecuencias = calcularFrecuencias(encuestas)
print(resultadosFrecuencias)

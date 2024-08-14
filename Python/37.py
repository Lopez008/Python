def analizar_tendencias(hashtags, tendencias):
    from collections import Counter

    frecuencia_hashtags = Counter(hashtags)

    hashtags_validos = set()

    for hashtag, frecuencia_minima in tendencias:
        if frecuencia_hashtags[hashtag] > frecuencia_minima:
            hashtags_validos.add(hashtag)
    
    return list(hashtags_validos)

hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 1), ("#moda", 1), ("#tecnologia", 100)]

resultados_tendencias = analizar_tendencias(hashtags, tendencias)
print(resultados_tendencias)

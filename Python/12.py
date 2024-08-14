def producto_mas_caro(productos):
    return max(productos, key=lambda x: x[1])

productos = [("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30)]

mas_caro = producto_mas_caro(productos)

print(f"El producto más caro es {mas_caro[0]} con un precio de ${mas_caro[1]}")
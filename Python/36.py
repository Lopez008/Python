def actualizar_inventario(inventario, nombre_tienda, **kwargs):
    if nombre_tienda not in inventario:
        inventario[nombre_tienda] = {}

    productos = inventario[nombre_tienda]
    
    for producto, cantidad in kwargs.items():
        productos[producto] = cantidad
    
    return inventario


inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}

inventario_actualizado = actualizar_inventario(inventario, "Tienda A", producto_1=55, producto_3=10)
print(inventario_actualizado)

inventario_actualizado = actualizar_inventario(inventario, "Tienda C", producto_1=15, producto_4=25)
print(inventario_actualizado)

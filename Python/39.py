def simularMercadoBursatil(preciosDiarios, operaciones):
    saldo = 0
    precioCompra = None
    
    for operacion, dia in operaciones:

        precioActual = preciosDiarios[dia]
        
        if operacion == "compra":
            precioCompra = precioActual
        
        elif operacion == "venta":

            if precioCompra is not None:
                beneficioPerdida = precioActual - precioCompra
                saldo += beneficioPerdida
                precioCompra = None
            else:
                print(f"Venta en el día {dia} sin compra previa.")
    
    return saldo

precioDiarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

beneficioTotal = simularMercadoBursatil(precioDiarios, operaciones)
print(f"Beneficio o perdida total: {beneficioTotal}")

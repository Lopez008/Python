def analizar_finanzas(**kwargs):
    balance_final = sum(kwargs.values())
    
    return balance_final

balance = analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)
print(f"El balance final es: {balance}")

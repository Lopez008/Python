def crear_perfil(**kwargs):
    return kwargs

perfil_usuario = crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza")

print("Perfil del usuario:")
for clave, valor in perfil_usuario.items():
    print(f"{clave}: {valor}")

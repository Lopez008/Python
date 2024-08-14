def libros_post_2000(biblioteca):
    librosRecientes = []

    for titulo, info in biblioteca.items():
        anioPublicacion = info.get("año")
        
        if anioPublicacion > 2000:
            librosRecientes.append(titulo)
    
    return librosRecientes

biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

librosRecientes = libros_post_2000(biblioteca)
print(librosRecientes)

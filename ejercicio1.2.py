def xd():
    valor = input("¿Desea continuar agregando más libros? S(si) N(no): ").upper()
    return False if valor == "N" else True

biblioteca = {
    '001': {"titulo": "la biblia de los caidos", "autor": "Fernando Trujillo", "año": 2011},
    '002': {"titulo": "psicologia oscura", "autor": "Steven Turner", "año": 2019},
    '003': {"titulo": "el arte de la seduccion", "autor": "Robert Greene", "año": 2001},
    '004': {"titulo": "las 48 leyes del poder", "autor": "Robert Greene", "año": 1998},
    '005': {"titulo": "El arte de la persuacion", "autor": "Jason Harris", "año": 2021}
}

Menu = True
while Menu:
    print("==" * 20, "\n")
    print("Bienvenido a la biblioteca \nActualmente presentamos nuestro menú de opciones.\n")
    print("==" * 20, "\n")

    print("1.) Añadir libro")    
    print("2.) Buscar/Listar libros")
    print("3.) Actualizar libros")
    print("4.) Eliminar un libro")
    print("5.) Salir\n")

    escoger = int(input("¿Qué opción eliges?: \n"))
    
    if escoger == 1:  # Añadir libro
        continuar = True
        while continuar:
            IdLibro = input("Ingresa el ID del libro que deseas crear: ")
            if IdLibro in biblioteca:
                print("Este ID ya existe, ingresa un nuevo ID por favor.")
            else:                     
                titulo = input("Por favor ingresa el título del libro: ")
                autor = input("Por favor ingrese el autor del libro: ")
                año = input("Por favor ingresa el año de publicación: ")
                
                biblioteca[IdLibro] = {
                    "titulo": titulo,
                    "autor": autor,
                    "año": año
                }
                print("\n¡Libro añadido correctamente!")
                continuar = xd()

    elif escoger == 2:  # Buscar/Listar libros
        print("\n=== BUSCAR/LISTAR LIBROS ===")
        print("1. Mostrar todos los libros")
        print("2. Buscar por ID")
        print("3. Buscar por Título")
        sub_opcion = int(input("Elige una opción de búsqueda: "))
        
        if sub_opcion == 1:  # Mostrar todos
            print("\n=== LISTA COMPLETA ===")
            for id_libro, info in biblioteca.items():
                print(f"\nID: {id_libro}")
                print(f"Título: {info['titulo']}")
                print(f"Autor: {info['autor']}")
                print(f"Año: {info['año']}")
        
        elif sub_opcion == 2:  # Buscar por ID
            id_buscar = input("\nIngresa el ID del libro: ")
            if id_buscar in biblioteca:
                print("\n=== LIBRO ENCONTRADO ===")
                print(f"ID: {id_buscar}")
                print(f"Título: {biblioteca[id_buscar]['titulo']}")
                print(f"Autor: {biblioteca[id_buscar]['autor']}")
                print(f"Año: {biblioteca[id_buscar]['año']}")
            else:
                print("\nNo se encontró ningún libro con ese ID.")
        
        elif sub_opcion == 3:  # Buscar por Título
            titulo_buscar = input("\nIngresa el título (o parte de él): ").lower()
            encontrados = False
            print("\n=== RESULTADOS ===")
            for id_libro, info in biblioteca.items():
                if titulo_buscar in info['titulo'].lower():
                    print(f"\nID: {id_libro}")
                    print(f"Título: {info['titulo']}")
                    print(f"Autor: {info['autor']}")
                    print(f"Año: {info['año']}")
                    encontrados = True
            if not encontrados:
                print("\nNo se encontraron libros con ese título.")
        
        else:
            print("\nOpción no válida.")
        input("\nPresiona Enter para volver al menú...")

    elif escoger == 3:  # Actualizar libro
        print("\n=== ACTUALIZAR LIBRO ===")
        IdLibro = input("Ingresa el ID del libro a actualizar: ")
        if IdLibro in biblioteca:
            print("\nDatos actuales del libro:")
            print(f"Título: {biblioteca[IdLibro]['titulo']}")
            print(f"Autor: {biblioteca[IdLibro]['autor']}")
            print(f"Año: {biblioteca[IdLibro]['año']}")

            print("\nIngresa los nuevos datos (deja en blanco si no quieres modificar):")
            nuevo_titulo = input("Nuevo título: ") or biblioteca[IdLibro]['titulo']
            nuevo_autor = input("Nuevo autor: ") or biblioteca[IdLibro]['autor']
            nuevo_año = input("Nuevo año: ") or biblioteca[IdLibro]['año']

            biblioteca[IdLibro] = {
                "titulo": nuevo_titulo,
                "autor": nuevo_autor,
                "año": nuevo_año
            }
            print("\n¡Libro actualizado correctamente!")
        else:
            print("\nError: El ID no existe.")
        input("\nPresiona Enter para volver al menú...")

    elif escoger == 4:  # Eliminar libro
        print("\n=== ELIMINAR LIBRO ===")
        IdLibro = input("Ingresa el ID del libro a eliminar: ")
        if IdLibro in biblioteca:
            print(f"\nLibro a eliminar: {biblioteca[IdLibro]['titulo']}")
            confirmar = input("¿Estás seguro? (S/N): ").upper()
            if confirmar == "S":
                del biblioteca[IdLibro]
                print("\n¡Libro eliminado correctamente!")
            else:
                print("\nOperación cancelada.")
        else:
            print("\nError: El ID no existe.")
        input("\nPresiona Enter para volver al menú...")

    elif escoger == 5:  # Salir
        print("\n¡Gracias por usar el sistema! Hasta luego. 👋")
        Menu = False

    else:
        print("\nOpción no válida. Intenta de nuevo.")
        input("\nPresiona Enter para continuar...")
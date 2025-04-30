contacto = {}

Menu=True

while Menu:
    print("==" * 20, "\n")
    print("Bienvenido a lista de contactos \nActualmente presentamos nuestro menú de opciones.\n")
    print("==" * 20, "\n")

    print("1.) Crear contacto")
    print("2.) leer contactos")
    print("3.) Actualizar contacto")
    print("4.) Eliminar contacto")

    escoger= int (input("¿cual opcion eliijes?: "))

    if escoger==1: #estamos creando un contacto
        continuar=True
        while continuar:
            nombreConta= input("Por favor ingresa el nombre del contacto: ")
            telefonoConta = int(input("Por favor ingrese el numero de telefono: "))
            emailConta= input("Por favor ingresa el correo electronico del contacto: ")

            contacto[nombreConta] = {                
                "Telefono": telefonoConta,
                "email": emailConta
            }
            print("Contacto añadido correctamente")
            valor = input("Deseas continuar agregando contactos?: S(si) N(no): ").upper()
            continuar = False if valor == "N" else True

        volver = int(input("para volver al menu anterior, digita 1, o 2 para finalizar: "))
        if volver==2:
            print ("exitoso ")
            Menu = False
    
    if escoger == 2:
        print("\n=== LISTA DE CONTACTOS===")
        print("la lista de usuario es: ")
        contador = 0
        for nombre, datos in contacto.items():  # Usamos las variables del ciclo
            print(f"\nNombre de Contacto: {nombre}")
            print(f"Teléfono: {datos['Telefono']}")  # Accedemos al diccionario interno
            print(f"Email: {datos['email']}")
            print("")
            
        volver = int(input("para volver al menu anterior, digita 1, o 2 para finalizar: "))
        if volver==2:
            print ("exitoso ")
            Menu = False
    if escoger ==3:
        print("Actualizar contacto \n")
        nombreConta=input("Ingresa el nombre del contacto que deseas actualizar: ")
        if nombreConta in contacto:
            print("\nDatos actuales de los contactos")
            print(f"Nombre: {contacto[nombreConta]['nombre']}")
            print(f"telefono: {contacto[nombreConta]['telefono']}")
            print(f"correo: {contacto[nombreConta]['email']}")

            print("\nIngresa los nuevos datos (deja en blanco si no quieres modificar):")
            nuevo_Nombre = input("Nuevo nombre: ") or contacto[nombreConta]['nombre']
            nuevo_telefono = input("Nuevo telefono: ") or contacto[nombreConta]['telefono']
            nuevo_corre = input("Nuevo correo: ") or contacto[nombreConta]['correo']



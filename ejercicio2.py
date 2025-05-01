contacto = {}


Menu = True


while Menu:

    print("==" * 20, "\n")

    print("Bienvenido a lista de contactos \nActualmente presentamos nuestro menú de opciones.\n")

    print("==" * 20, "\n")


    print("1.) Crear contacto")

    print("2.) Leer contactos")

    print("3.) Actualizar contacto")

    print("4.) Eliminar contacto")

    print("5.) Salir")


    escoger = int(input("¿Cuál opción eliges?: "))


    if escoger == 1:  # Estamos creando un contacto

        continuar = True

        while continuar:

            nombreConta = input("Por favor ingresa el nombre del contacto: ")

            telefonoConta = input("Por favor ingrese el número de teléfono: ")  # Cambiado a input

            emailConta = input("Por favor ingresa el correo electrónico del contacto: ")


            contacto[nombreConta] = {                

                "Telefono": telefonoConta,  # Guardamos como string

                "email": emailConta

            }

            print("Contacto añadido correctamente")

            valor = input("¿Deseas continuar agregando contactos?: S(si) N(no): ").upper()

            continuar = False if valor == "N" else True


        volver = int(input("Para volver al menú anterior, digita 1, o 2 para finalizar: "))

        if volver == 2:

            print("Exitoso ")

            Menu = False

    

    elif escoger == 2:

        print("\n=== LISTA DE CONTACTOS ===")

        print("La lista de usuarios es: ")

        for nombre, datos in contacto.items():

            print(f"\nNombre de Contacto: {nombre}")

            print(f"Teléfono: {datos['Telefono']}")

            print(f"Email: {datos['email']}")

            print("")

            

        volver = int(input("Para volver al menú anterior, digita 1, o 2 para finalizar: "))

        if volver == 2:

            print("Exitoso ")

            Menu = False


    elif escoger == 3:

        print("Actualizar contacto \n")

        nombreConta = input("Ingresa el nombre del contacto que deseas actualizar: ")

        if nombreConta in contacto:

            print("\nDatos actuales de los contactos")

            print(f"Nombre: {nombreConta}")

            print(f"Teléfono: {contacto[nombreConta]['Telefono']}")

            print(f"Correo: {contacto[nombreConta]['email']}")


            print("\nIngresa los nuevos datos (deja en blanco si no quieres modificar):")

            nuevo_Nombre = input("Nuevo nombre: ") or nombreConta

            nuevo_telefono = input("Nuevo teléfono: ") or contacto[nombreConta]['Telefono']

            nuevo_email = input("Nuevo correo: ") or contacto[nombreConta]['email']


            # Actualizar el contacto

            contacto[nuevo_Nombre] = {

                "Telefono": nuevo_telefono,

                "email": nuevo_email

            }

            if nuevo_Nombre != nombreConta:

                del contacto[nombreConta]  # Eliminar el antiguo nombre si se cambió

            print("Contacto actualizado correctamente.")

        else:

            print("Error: El contacto no existe.")


    elif escoger == 4:

        print("\n== ELIMINAR CONTACTO ===")

        nombreConta = input("Ingresa el nombre del contacto a eliminar: ")

        if nombreConta in contacto:

            print(f"\nContacto a eliminar: {nombreConta}")

            confirmar = input("¿Estás seguro? (S/N): ").upper()

            if confirmar == "S":

                del contacto[nombreConta]

                print("\nEl contacto ha sido eliminado correctamente!")

            else:

                print("\nOperación cancelada.")

        else:

            print("\nError: El contacto no existe.")

        input("\nPresiona Enter para volver al menú...")
    
    elif escoger == 5:  # Salir

        print("\n¡Gracias por usar el sistema! Hasta luego.")

        Menu = False


    else:

        print("\nOpción no válida. Intenta de nuevo.")

        input("\nPresiona Enter para continuar...")
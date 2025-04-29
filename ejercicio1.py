biblioteca ={
'001':{"la biblia de los caidos","Fernando Trujullo", 2011,"\n"},
'002':{"psicologia oscura", "Steven Turner", 2019,"\n"},
'003':{"el arte de la seduccion","Robert Greene",2001,"\n"},
'004':{"las 48 leyes del poder","Robert Greene",1998,"\n"},
'005':{"El arte de la persuacion","Jason Harris",2021,"\n"}
}

def Add_Book():
    IdLibro=input("ingresa el id del libro que deseas crear: ")
    if IdLibro in biblioteca:
        print("Este ID ya existe, ingresa un nuevo ID por favor")
        return
    titulo=input("ingresa el titulo del libro: ")
    autor=input("ingresa el autor del libro: ")
    try:
         año = input("Ingresa el año de la publicacion del libro: ")
    except ValueError:
        print("el año debe de ser numero entero.")
        return
    biblioteca[Add_Book] = {
        "titulo":titulo,
        "autor":autor,
        "año":año
    }
    print("libro guardado con exito.")
Add_Book()

def Read_book():
   if not biblioteca:
       print("el libro no se encuentra en la biblioteca")
       return
   print("listado de libros: \n")
   for Id_libros, info in biblioteca.items():
       print (f"ID:{Id_libros},titulo:{info['titulo']},autor:{info['autor']},año:{info['año']}")
print(biblioteca)

peliculas=[]
def add_movie():
    print("\n--AGREGAR PELICULA--")
    how=int(input("Ingrese cuantas películas desea agregar: "))
    for i in range(how):
        print(f"\nIngrese la información de la película no.{i+1}")
        name=input("Titulo:").lower()
        year=input("Año:")
        gender=input("Genero:").lower()
        pelicula=[name, year,gender]
        peliculas.append(pelicula)

    print(f"{how} peliculas fueron agregadas correctamente")

def show():
    if peliculas:
        print("\n--PELÍCULAS--")
        for p in peliculas:
            print(f"Titulo:{p[0]} ,Año:{p[1]} , Genero:{p[2]}")
    else:
        print("La lista esta vacía")

def search():
    print("\n--BUSCADOR--")
    encontradas=[]
    genero=input("Ingrese el genero que desea buscar:").lower()
    for p in peliculas:
        if p[2]==genero:
            encontradas.append(p)

    if encontradas:
        print(f"\nPelículas del género {genero}:")
        for p in encontradas:
            print(f"Título: {p[0]}, Año: {p[1]}")
    else:
        print("No se encontraron películas con ese género.")

def delete():
    if peliculas:
        print(peliculas)
        name_dos=input("Ingrese el nombre exacto de la película que desea eliminar ").lower()
        for p in peliculas:
            if p[0]==name_dos.lower():
                peliculas.remove(p)
                print(f"La pelicula '{name_dos}' fue eliminada correctamente")
    else:
        print("\nEL catalogo de películas esta vacío")

def registradas():
    if peliculas:
        print("\n--ESTADÍSTICAS--")
        print(f"Existen {len(peliculas)} películas registradas")
        generos_unicos=[]
        for p in peliculas:
            if p[2] not in generos_unicos:
                generos_unicos.append(p[2])

        for genero in generos_unicos:
            contador=0
            for p in peliculas:
                if p[2]==genero:
                    contador+=1
            print(f"{genero}:{contador}")

    else:
        print("\nEL catalogo de películas esta vacío")

def old():
    if peliculas:
        years=[]
        for p in peliculas:
            years.append(p[1])

        minimo=min(years)
        for p in peliculas:
            if p[1] == minimo:
                print(f"La pelicula mas antigua es: Titulo:{p[0]}, Género: {p[2]} , Año:{minimo}")
    else:
        print("\nEL catalogo de películas esta vacío")


while True:
    print("\n--MENÚ--")
    print("1.Agregar Películas")
    print("2.Mostrar películas agregadas")
    print("3.Buscar películas por genero")
    print("4.Eliminar una película por titulo")
    print("5.Ver estadísticas del catálogo")
    print("6.Salir")
    option=input("Seleccione una opción del menú (1-6): ")

    match option:
        case "1":
            add_movie()
        case "2":
            show()
        case "3":
            search()
        case "4":
            delete()
        case "5":
            registradas()
            old()
        case "6":
            print("Saliendo del programa...")
            break
        case _:
            print("Error al seleccionar una opción, inténtelo de nuevo")

peliculas=[]
def add_movie():
    how=int(input("Ingrese cuantas películas desea agregar: "))
    for i in range(how):
        print(f"\nIngrese la informacion de la pelicula no.{i+1}")
        name=input("Titulo:")
        year=input("Año:")
        gender=input("Genero:")
        pelicula=[name, year,gender]
        peliculas.append(pelicula)

    print(f"{how} peliculas fueron agregadas correctamente")

def mostrar():
    if peliculas:
        print("\n--PELÍCULAS--")
        for p in peliculas:
            print(f"Titulo:{p[0]} ,Año:{p[1]} , Genero:{p[2]}")
    else:
        print("La lista esta vacía")

while True:
    print("\n1.Agregar Películas")
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
            mostrar()
        case "3":
            print()
        case "4":
            print()
        case "5":
            print()
        case "6":
            print("Saliendo del programa...")
            break
        case _:
            print("Error al seleccionar una opción, inténtelo de nuevo")

while True:
    print("1.Agregar Películas")
    print("2.Mostrar películas agregadas")
    print("3.Buscar películas por genero")
    print("4.Eliminar una película por titulo")
    print("5.Ver estadísticas del catálogo")
    print("6.Salir")
    option=input("Seleccione una opción del menú (1-6): ")

    match option:
        case "1":
            print()
        case "2":
            print()
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

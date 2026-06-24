#Sistema de Gestión de Películas de Cine

print("\n Bienvenido al Sistema de Gestión de Películas de Cine\n")

print("MENÜ")
print("====\n")
print("Seleccione una opción del menú:")
print("1. Agregar película")
print("2. Buscar películas")
print("3. Eliminar película")
print("4. Actualizar disponibilidad")
print("5. Mostrar películas")
print("6. Salir")
i = 0
agregar_pelicula = 0
buscar_peliculas = 0
eliminar_pelicula = 0
actualizar_disponibilidad = 0
mostrar_pelicula = 0


lista_peliculas = [[nombre, duracion, calificacion, disponible] for nombre, duracion, calificacion, disponible in []]

while i < 6:
    opcion = int(input("Ingrese una opción del menú: \n"))
    if opcion == 1:
        agregar_pelicula += 1
        print("Agregar película")
        nombre = input("Ingrese el nombre de la película: ")
        duracion = int(input("Ingrese la duración de la película en minutos: "))
        calificacion = float(input("Ingrese la calificación de la película (0.0 - 10.0): "))
        disponible = False
        lista_peliculas.append([nombre, duracion, calificacion, disponible])
    elif opcion == 2:
        buscar_peliculas += 1
        print("Buscar películas")
        nombre_buscar = input("Ingrese el nombre de la película a buscar: ")
        encontrado = False
        for pelicula in lista_peliculas:
            if pelicula[0] == nombre_buscar:
                print(f"Película encontrada: {pelicula}")
                encontrado = True
                break
        if not encontrado:
            print(f"La película '{nombre_buscar}' no se encuentra registrada.")
    elif opcion == 3:
        eliminar_pelicula += 1
        print("Eliminar película")
        nombre_eliminar = input("Ingrese el nombre de la película a eliminar: ")
        encontrado = False
        for pelicula in lista_peliculas:
            if pelicula[0] == nombre_eliminar:
                lista_peliculas.remove(pelicula)
                print(f"La película '{nombre_eliminar}' ha sido eliminada.")
                encontrado = True
                break
        if not encontrado:
            print(f"La película '{nombre_eliminar}' no se encuentra registrada.")
    elif opcion == 4:
        actualizar_disponibilidad += 1
        print("Actualizar disponibilidad")
        for pelicula in lista_peliculas:
            if pelicula[2] >= 7.0:
                pelicula[3] = True
            else:
                pelicula[3] = False
    elif opcion == 5:
        mostrar_pelicula += 1
        print("\n===LISTA DE PELÍCULAS===\n")
        for pelicula in lista_peliculas:
            estado = "DISPONIBLE" if pelicula[3] else "NO RECOMENDADA"
            print(f"Título: {pelicula[0]}\nDuración: {pelicula[1]}\nCalificación: {pelicula[2]}\nEstado: {estado}\n")

            print("********************************************")
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")




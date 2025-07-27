movies_cine = [[], [], []]
def saludar():
    print("Bienvenido al catalogo de peliculas")
def agregar_peliculas():
    movie_entry = int(input("Ingrese la cantidad de peliculas que desea agregar "))
    for i in range (movie_entry):
        title_movie = input("Ingrese el titulo de la pelicula ").lower().strip()
        year_of_release = int(input("Ingrese el año de la pelicula "))
        movie_genre = input("Ingrese el genero de la pelicula ").lower().strip()
        movies_cine[0].append(title_movie)
        movies_cine[1].append(year_of_release)
        movies_cine[2].append(movie_genre)
def mostrar_peliculas():
    if not movies_cine[0]:
        print("No se ha echo ningun registro de pelicula")
    else:
        print("\n Peliculas registradas")
        for i in range(len(movies_cine[0])):
            print(f"Titulo {movies_cine[0][i]}")
            print(f"Año {movies_cine[1][i]}")
            print(f"Genero {movies_cine[2][i]}")
def buscar_pelicula_por_genero():
    if not movies_cine[0]:
        print("No hay películas registradas.")
        return
    search_by_genre = input(" Ingrese el género de la pelicula que desea encontrar: ").strip().lower()
    encontrado = False
    print(f"\n Películas del género {search_by_genre}:")
    for i in range(len(movies_cine[2])):
        if movies_cine[2][i].strip().lower() == search_by_genre:
            print(f"- Título: {movies_cine[0][i]}, Año: {movies_cine[1][i]}")
            encontrado = True
    if not encontrado:
        print(" No se encontraron películas de ese género.")
def eliminar_una_pelicula_por_titulo():
    if movies_cine:
        delete_movie =input("Ingrese el nombre de la pelicula que desea borrar: ").lower().strip()
        if delete_movie in movies_cine[0]:
            indice_name_movie = movies_cine[0].index(delete_movie)
            movies_cine[0].pop(indice_name_movie)
            movies_cine[1].pop(indice_name_movie)
            movies_cine[2].pop(indice_name_movie)
            print(f"La pelicula con el nombre {delete_movie} ha sido eliminda en su totalidad")
        else:
            print(f"no se encontro ningunapelicula con el nombre {delete_movie}")
    else:
        print("no se ha registrado ninguna pelicula")
def mostrar_cantidad_peliculas():
    if movies_cine and movies_cine[0]:
        print(f"Se registraron {len(movies_cine[0])} peliculas")
    else:
        print("No se ha echo ningun registro")
def mostrar_peliculas_por_genero():
    if movies_cine and movies_cine[2]:
        counter_genre ={}
        for genre in movies_cine[2]:
            if genre in counter_genre:
                counter_genre[genre] +=1
            else:
                counter_genre[genre] =1
                print("Cantidad de peliculas por genero")
                for genre,cantidad in counter_genre.items():
                    print(f"{genre.capitalize()}: {cantidad}")
    else:
        print("no hay ninguna pelicula registrada")
def mostrar_la_pelicula_mas_antigua ():
    if movies_cine and movies_cine[1]:
        year_antiguo = min(movies_cine[1])
        indice = movies_cine.index(year_antiguo)
        print("\n -La pelicula mas reciente-")
        print(f"Nombre {movies_cine[0][indice]}")
        print(f"Año de estreno: {movies_cine[1][indice]}")
        print(f"Genero: {movies_cine[2][indice]}")
    else:
        print("No hay ninguna pelicula registrada")
saludar()
while True:
    print("\n ---MENU---")
    print("1. Agregar peliculas")
    print("2. Mostrar Peliculas registradas")
    print("3. Buscar una pelicula por su genero")
    print("4. Eliminar una pelicula")
    print("5. Ver la estadistica del catalogo")
    print("6. Salir del programa")
    option = input("ingrese una opcion (1-6) ")
    match option:
        case "1":
            agregar_peliculas()
        case "2":
            mostrar_peliculas()
        case "3":
            buscar_pelicula_por_genero()
        case "4":
            eliminar_una_pelicula_por_titulo()
        case "5":
            mostrar_cantidad_peliculas()
            mostrar_peliculas_por_genero()
            mostrar_la_pelicula_mas_antigua()
        case "6":
            print("Gracias por utilizar el programa")
            break
        case _:
            print("Error dato invalido, vuelva a intentarlo")
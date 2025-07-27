movies_cine = [[], [], []]
def saludar():
    print("Bienvenido al catalogo de peliculas")
def agregar_peliculas():
    movie_entry = int(input("Ingrese la cantidad de peliculas que desea agregar "))
    for i in range (movie_entry):
        title_movie = input("Ingrese el titulo de la pelicula ")
        year_of_release = int(input("Ingrese el año de la pelicula "))
        movie_genre = input("Ingrese el genero de la pelicula ")
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
        print("📭 No hay películas registradas.")
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
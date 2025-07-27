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
saludar()
while True:
    print("\n ---MENU---")
    print("1. Agregar peliculas")
    print("2. Mostrar Peliculas registradas")
    print("3. Buscar una pelicula por su genero")
    print("4. Eliminar una pelicula")
    print("5. Ver la estadistica del catalogo")
    print("6. Salir del programa")
    option = input("ingrese una opcion (1-6)")
    match option:
        case "1":
            agregar_peliculas()
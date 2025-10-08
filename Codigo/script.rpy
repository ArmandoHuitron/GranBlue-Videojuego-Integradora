# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define Entrenador = Character("Sim",color="#6b270086")
define Jugador_1 = Character("Clara",color="#03bdc486")
define Protagonista = Character("Mateo",color="#5c8d0086")
define Jugador_3 = Character("Sara",color="#0113b686")
define Jugador_4 = Character("Luis",color="#86140086")
define Jugador_5 = Character("Andrea",color="#8803bd86")

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene fondo1
    "Como olvidar aquella vez.. ese momento de nuestra juventud donde estabamos cerca de nuestro mejor momento"
    "Teniamos un grupo de amigos.. y eramos un equipo de futbol paralimpico.. con nuestros esfuerzos llegamos y apuntamos al mundial"
    "Estabamos listos para finalmente llegar a la meta.. cuando de la nada"
    "..."
    "El entrenador Sim desaparecio"
    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy

    # Presenta las líneas del diálogo.

    e "Has creado un nuevo juego Ren'Py."

    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:

    return

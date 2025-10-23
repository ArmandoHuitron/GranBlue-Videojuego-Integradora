# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define p = Character("Protagonista")
define ps1 = Character("Andrea")
define ps2 = Character("Luis")
define ps3 = Character("Sara")
define ps4 = Character("Mateo")
define ps5 = Character("Clara")
define e = Character("Entrenador Sim", color="#FFD700")

# El juego comienza aquí.
# ==========================================
#   Misterio sobre ruedas
#   Novela visual por el equipo Grand Blue
# ==========================================

# Variable inicial para medir las decisiones correctas
default team_points = 0

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene fondo1
    with fade
    "Como olvidar aquella vez.. ese momento de nuestra juventud donde estabamos cerca de nuestro mejor momento"
    "Teniamos un grupo de amigos.. y eramos un equipo de futbol paralimpico.. con nuestros esfuerzos llegamos y apuntamos al mundial"
    "Estabamos listos para finalmente llegar a la meta.. cuando de la nada"
    "..."
    "El entrenador Sim desaparecio"

    play music "bgm_office.mp3" fadein 1.0
    "Oficina del profesor - tarde"

    p "Qué raro... el maestro nos citó aquí para contarnos algo importante."
    ps1 "No lo he visto, pero recuerdo que dijo algo sobre una noticia importante."
    ps2 "Sí, últimamente nos ha exigido bastante en los entrenamientos."
    ps3 "Toda la semana pasada llegué a casa muerto del cansancio."
    ps4 "Quizá deberíamos buscarlo. ¿Dónde creen que esté?"
    ps5 "Últimamente nos hablaba sobre prepararnos académicamente... tal vez dejó algo aquí."

    p "Veamos si encontramos alguna pista..."

    menu:
        "¿Qué hacer primero?"
        "Mirar sobre el escritorio":
            jump oficina_escritorio
        "Revisar el estante de trofeos":
            jump oficina_trofeos
        "Preguntar a Andrea si vio algo raro":
            jump oficina_ps1

label oficina_escritorio:
    $ team_points += 1
    p "Hmm... hay una carta sobre el escritorio."
    "Carta del entrenador" "Mis queridos jóvenes, estoy maravillado por su esfuerzo. Han demostrado que son dignos de representar cualquier equipo. Por eso he encontrado una oportunidad de oro... se trata de—"
    p "La carta está incompleta..."
    ps2 "¿Otra parte, quizá?"
    ps4 "Entonces debemos buscarlo. Lo vi por última vez en la cancha o en la biblioteca."
    ps5 "¿A dónde vamos primero?"
    jump elegir_destino

label oficina_trofeos:
    p "Solo veo trofeos polvosos... aunque es lindo verlos todos juntos."
    ps3 "¡Mira! Mi nombre está mal escrito en este."
    ps2 "No hay pistas aquí, intentemos en otro lado."
    jump elegir_destino

label oficina_ps1:
    ps1 "Raro... vi que el escritorio estaba abierto hace un rato, quizá alguien dejó algo ahí."
    p "Entonces revisaré el escritorio."
    jump oficina_escritorio

label elegir_destino:
    menu:
        "¿A dónde ir?"
        "Cancha":
            jump cancha
        "Biblioteca":
            jump biblioteca

# =======================
#     NIVEL 2: CANCHA
# =======================

label cancha:
    scene field_day
    with fade
    play music "bgm_field.mp3" fadein 1.0

    "Cancha - tarde"
    p "Aquí estamos. Si el maestro vino, debe haber dejado algo."
    ps3 "Quizá deberíamos revisar donde solía sentarse a vernos entrenar."
    ps4 "Sí, su asiento favorito. Decía que desde ahí podía observar mejor todo."

    menu:
        "¿Dónde revisar?"
        "Primera fila de gradas":
            jump gradas_correctas
        "Última fila":
            jump gradas_erroneas
        "Banca":
            jump banca_erronea

label gradas_correctas:
    $ team_points += 1
    p "Hay algo brillando debajo de uno de los asientos..."
    ps2 "¡Es su reloj!"
    ps3 "El que usaba para medir los entrenamientos."
    ps5 "Pero está detenido... marca las 4:00 PM."
    ps4 "A esa hora siempre salía el autobús cuando teníamos viajes."
    p "Entonces, si el reloj se detuvo a las 4, quizás esa sea la siguiente pista."
    jump autobus

label gradas_erroneas:
    p "Nada por aquí..."
    ps3 "No era en la última fila, él prefería estar cerca del campo."
    jump gradas_correctas

label banca_erronea:
    p "Solo hay botellas vacías y conos viejos."
    ps2 "Nada útil aquí."
    jump gradas_correctas

# =======================
#   NIVEL 3: AUTOBÚS
# =======================

label autobus:
    scene bus_interior
    with fade
    play music "bgm_bus.mp3" fadein 1.0

    "Autobús escolar - interior"

    ps1 "Hace tiempo que no subía aquí... me trae recuerdos."
    ps3 "El maestro siempre se sentaba adelante, cerca del conductor."
    ps2 "Si dejó algo aquí, debe ser importante."

    menu:
        "¿Dónde buscar?"
        "Asiento del conductor":
            jump bus_conductor
        "Compartimentos superiores":
            jump bus_superior
        "Fondo del autobús":
            jump bus_fondo

label bus_conductor:
    p "Solo hay papeles viejos y un silbato oxidado."
    ps5 "Nada útil aquí."
    jump bus_fondo

label bus_superior:
    p "Nada más que mochilas olvidadas y polvo."
    jump bus_fondo

label bus_fondo:
    $ team_points += 1
    p "Aquí hay algo entre los asientos traseros..."
    ps2 "¿Una foto?"
    ps5 "Sí... es el equipo, con el maestro. Detrás hay una nota."
    "Nota" "Los verdaderos campeones no solo corren… también piensan, estudian y se apoyan."
    ps4 "Eso suena a una pista. 'Piensan y estudian'... debe referirse a la biblioteca."
    p "Vamos allá."
    jump biblioteca

# =======================
#   NIVEL 4: BIBLIOTECA
# =======================

label biblioteca:
    scene library_day
    with fade
    play music "bgm_library.mp3" fadein 1.0

    "Biblioteca - tarde"
    ps1 "Si el maestro dejó una pista, estará entre los libros que usamos."
    ps3 "Espero que no nos toque leer toda la enciclopedia otra vez..."
    p "Busquemos entre los libros de estrategia o historia del fútbol."

    menu:
        "¿Dónde buscar?"
        "Libros de historia del fútbol":
            jump biblioteca_correcta
        "Escritorio de la bibliotecaria":
            jump biblioteca_erronea1
        "Juegos de mesa":
            jump biblioteca_erronea2

label biblioteca_correcta:
    $ team_points += 1
    p "Aquí hay algo doblado entre las páginas..."
    "Carta del entrenador" "Viajarán juntos a representar a nuestra nación en el Mundial Paralímpico. Pero antes, deben demostrar que pueden pensar como un solo equipo."
    ps2 "Entonces todo esto fue una prueba."
    ps4 "Una forma de ver si estábamos listos."
    ps5 "Solo falta encontrarlo."
    p "Debe esperarnos donde todo empezó… en el pasillo principal."
    jump pasillo

label biblioteca_erronea1:
    p "Solo formularios y registros. Nada útil."
    jump biblioteca_correcta

label biblioteca_erronea2:
    p "Solo fichas viejas de ajedrez y dominó."
    jump biblioteca_correcta

# =======================
#   NIVEL 5: PASILLO FINAL
# =======================

label pasillo:
    scene hallway_evening
    with fade
    play music "bgm_endtheme.mp3" fadein 1.0

    "Pasillo principal - atardecer"
    ps2 "No puedo creerlo… todo este tiempo nos estuvo guiando."
    ps3 "Y yo que pensaba que solo quería hacernos correr más."
    ps1 "Fue más que eso. Nos entrenó para pensar, no solo para jugar."
    ps5 "Para confiar los unos en los otros."
    ps4 "Para no rendirnos, ni siquiera cuando no sabemos qué hacer."
    p "Y al final… lo hicimos. No solo lo buscamos, lo comprendimos."

    "Se escuchan pasos acercándose..."

    if team_points >= 4:
        jump final_bueno
    else:
        jump final_malo

# =======================
#     FINALES
# =======================

label final_bueno:
    show coach_smile
    with dissolve
    e "No buscaban una carta… buscaban lo que siempre tuvieron: unión, inteligencia y confianza."
    e "Estoy orgulloso de ustedes. Han demostrado que están listos para representar lo que significa el espíritu del deporte."
    ps2 "¿Entonces... pasamos la prueba?"
    e "Más que eso. Ustedes ya son campeones."
    stop music fadeout 2.0
    play music "bgm_victory.mp3"
    "El verdadero partido apenas comienza..."
    return

label final_malo:
    "El grupo se reúne, pero el entrenador no aparece."
    p "Tal vez aún nos falta algo..."
    "Algunos partidos no se ganan, se aprenden."
    stop music fadeout 2.0
    return

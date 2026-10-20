define prota = Character("[nombre] [apellido]")

label start:

    $ prota = renpy.input("Ingresa tu nombre en la aventura", length=32)
    $ prota = prota.strip()
    $ apellido = renpy.input("Ingresa tu apellido", length = 32)
    $ apellido = apellido.strip()
    $ edad = ""
    while edad < "16" and edad > "19" or not edad:
        $ edad = renpy.input("Ingresa tu edad en el juego (entre 16 y 19 años)", length = 2)
        $ edad = edad.strip()
    $ curso = renpy.menu:
        "Elige el curso en el que estarás"
        "3ro medio A (EcoClub)":
            #block of code to run
        "3ro medio B (ArtClub)":
            #block of code to run
        

    if not prota and not apellido and not edad:
        $ prota = "Jane"
        $ apellido = "Doe"
        $ edad = "17"
    return

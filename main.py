#importacione de clases


#para que este codigo funcione se debe tener instalado mongodb  y su dns
#en la consola "python -m pip install pymongo"
#en la consola "python -m pip install dnspython"
from jugador import Jugador
from juego import Juego
from exportarCSV import exportToCsv

#menu principal con opciones seleccionables segun el numero de la opcion deseeada
juego=Juego()
while True:
    juego.cargarDB()
    opt= input('''Ingrese el numero para la accion seleccionada :
1. Para iniciar una partida
2. Ver estadisticas de jugadores
3. Imprimir preguntas
4. Admin
5. Para salir
''')
    if opt== '1':
        nombre=input("Ingresa el nombre del participante: ")
        nuevoJugador=Jugador(nombre)
        juego.rondas(nuevoJugador)
    elif opt== '2':
       opt=int(input("Selecciona 1.Para imprimir por consola 2.Para imprimir en .csv :   "))
       if (opt ==1):
            juego.recordJugadores() 
       elif (opt==2):
            exportToCsv().exportarJugadoresCsv()
    elif opt== '3':
       opt=int(input("Selecciona 1.Para imprimir por consola 2.Para imprimir en .csv :   "))
       if (opt ==1):
            juego.imprimirPreguntas()    
       elif (opt==2):
           exportToCsv().exportarPreguntasCsv()
    elif opt== '4':
       opt=int(input("1.Agregar una nueva pregunta 2.Salir :     "))
       if (opt ==1):
            juego.ingresarPregunta()    
       
    elif opt== '5':
       break
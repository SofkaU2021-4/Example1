class Jugador():
    def __init__(self,nombre):
        self.nombre=nombre
        self.categoria=1
        self.acomulado=0

    def __str__(self):
        cadena = "nombre: "+ self.nombre + "  nivel: "+str(self.nivel) + "   acomulado: " + str(self.acomulado)
        return cadena
 #objeto jugador
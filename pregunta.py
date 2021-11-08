
#objeto pregunta
class Pregunta():
    def __init__(self,categoria,enunciado,opt1,opt2,opt3,opt4,correcta):
        self.categoria=categoria
        self.enunciado=enunciado
        self.opt1=opt1
        self.opt2=opt2
        self.opt3=opt3
        self.opt4=opt4
        self.correcta=correcta  
   
    def __str__(self):
        ver= self.enunciado
        return ver


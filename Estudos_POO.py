#"SELF" e uma variavel global, faz referencia dentro de algum metodo a variavel criada posteriormente!
#Ex: p1.nome ==> self.nome --- p1(nome de variavel) e self(referencia a p1) são a mesma coisa!

class Lampada:
    def __init__(self,estado=False):
        self.estado = estado

    def estadolp(self):
        if self.estado == False:
            print('A lampada esta desligada!')
        else:
            print('A lampada esta ligada!')
    
    def interruptor(self):
        if self.estado == False:
            print('Ligando a lampada')
            self.estado = True
        else:
            print('Desligando a lampada')
            self.estado = False
        return
    
#Parte de teste:

dr = Lampada()
dr.estadolp()
dr.interruptor()
dr.estadolp()
dr.interruptor()
dr.estadolp()
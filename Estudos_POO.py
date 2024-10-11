#PARTE 1

#"SELF" e uma variavel global, faz referencia dentro de algum metodo a variavel criada posteriormente!
#Ex: p1.nome ==> self.nome --- p1(nome de variavel) e self(referencia a p1) são a mesma coisa!

# class Lampada:
#     def __init__(self,estado=False):
#         self.estado = estado

#     def estadolp(self):
#         if self.estado == False:
#             print('A lampada esta desligada!')
#         else:
#             print('A lampada esta ligada!')
    
#     def interruptor(self):
#         if self.estado == False:
#             print('Ligando a lampada')
#             self.estado = True
#         else:
#             print('Desligando a lampada')
#             self.estado = False
#         return
    
#Parte de teste:

# dr = Lampada()
# dr.estadolp()
# dr.interruptor()
# dr.estadolp()
# dr.interruptor()
# dr.estadolp()


# PARTE 2

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def desconto(self,percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    #GETTER
    @property
    def preco(self):
        return self._preco
    
    @property
    def nome(self):
        return self._nome
    
    #SETTER
    @preco.setter
    def preco(self,valor):
        if isinstance(valor,str):
            valor = float(valor.replace('R$',''))
        self._preco = valor

    @nome.setter
    def nome(self,valor):
        self._nome = valor.title()



p1 = Produto('Camiseta',50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('caneca', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)